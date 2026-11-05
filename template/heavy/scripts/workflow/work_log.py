#!/usr/bin/env python3
"""Append one validated work-log event to a local JSONL file."""

import argparse
import json
import math
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

try:
    import fcntl
except ImportError:
    fcntl = None


DEFAULT_LOG = Path(__file__).resolve().parents[2] / "docs/workflow/work-log.jsonl"
ROLES = ("HUMAN", "LEAD", "DISPATCHER", "DEVELOPER", "REVIEWER")
EVENTS = (
    "start",
    "complete",
    "transition",
    "return",
    "blocked",
    "park",
    "resume",
    "check_result",
    "allowance",
    "correction",
)
CAUSES = ("product", "test", "launch", "capture", "environment", "approval", "unknown")
KINDS = (
    "work",
    "coordination",
    "test_runtime",
    "agent_wait",
    "tool_wait",
    "user_wait",
    "unclassified",
)
MEASUREMENTS = ("tool_reported", "utc_elapsed")
ACTIVITIES = ("none_known", "present", "unknown")
TIMING_REQUIRED = frozenset(
    ("kind", "started_at", "ended_at", "duration_ms", "measurement")
)
TIMING_OPTIONAL = frozenset(("parent_span",))
ALLOWANCE_REQUIRED = frozenset(
    (
        "observed_at",
        "source",
        "limit_id",
        "window_minutes",
        "reset_at_unix",
        "remaining_percent",
        "other_activity",
    )
)
UTC_TIMESTAMP = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|\+00:00)$")


def nonempty(value, name):
    if type(value) is not str or not value.strip():
        raise ValueError(name + " must be a nonempty string")
    return value


def timestamp(value, name):
    if type(value) is not str or not UTC_TIMESTAMP.fullmatch(value):
        raise ValueError(name + " must be RFC3339 UTC")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(name + " must be RFC3339 UTC") from error
    if parsed.utcoffset().total_seconds() != 0:
        raise ValueError(name + " must be UTC")
    return parsed


def number(value, name, *, integer=False, minimum=None, maximum=None):
    good_type = type(value) is int if integer else type(value) in (int, float)
    if not good_type or type(value) is float and not math.isfinite(value):
        raise ValueError(
            name + " must be a finite " + ("integer" if integer else "number")
        )
    if (
        minimum is not None
        and value < minimum
        or maximum is not None
        and value > maximum
    ):
        raise ValueError(name + " is outside its allowed range")
    return value


def object_fields(value, name, required, optional=frozenset()):
    if type(value) is not dict:
        raise ValueError(name + " must be an object")
    missing = required - value.keys()
    unknown = value.keys() - required - optional
    if missing or unknown:
        raise ValueError(
            name
            + " has missing or unknown fields: "
            + ", ".join(sorted(missing | unknown))
        )


def choice(value, name, allowed):
    if type(value) is not str or value not in allowed:
        raise ValueError(name + " must be one of: " + ", ".join(allowed))
    return value


def validate_timing(value):
    object_fields(value, "timing", TIMING_REQUIRED, TIMING_OPTIONAL)
    choice(value["kind"], "timing.kind", KINDS)
    start = timestamp(value["started_at"], "timing.started_at")
    end = value["ended_at"]
    if end is not None:
        end = timestamp(end, "timing.ended_at")
        if end < start:
            raise ValueError("timing end precedes start")
    duration = value["duration_ms"]
    if duration is not None:
        number(duration, "timing.duration_ms", minimum=0)
    if end is None and duration is not None:
        raise ValueError("open timing must have null duration")
    measurement = choice(value["measurement"], "timing.measurement", MEASUREMENTS)
    if measurement == "utc_elapsed" and end is not None:
        if duration is None or round((end - start).total_seconds() * 1000) != round(
            duration
        ):
            raise ValueError(
                "utc_elapsed duration must match UTC boundaries to a millisecond"
            )
    if "parent_span" in value:
        nonempty(value["parent_span"], "timing.parent_span")
    return value


def validate_allowance(value):
    object_fields(value, "allowance", ALLOWANCE_REQUIRED)
    timestamp(value["observed_at"], "allowance.observed_at")
    nonempty(value["source"], "allowance.source")
    nonempty(value["limit_id"], "allowance.limit_id")
    number(value["window_minutes"], "allowance.window_minutes", integer=True, minimum=1)
    number(value["reset_at_unix"], "allowance.reset_at_unix", integer=True, minimum=0)
    number(
        value["remaining_percent"],
        "allowance.remaining_percent",
        minimum=0,
        maximum=100,
    )
    choice(value["other_activity"], "allowance.other_activity", ACTIVITIES)
    return value


def load_nested(path, name):
    if path is None:
        return None
    try:
        with open(path, encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(name + " could not be read as JSON: " + str(error)) from error


def existing_ids(raw):
    def reject_constant(value):
        raise ValueError("nonstandard JSON constant: " + value)

    ids = set()
    if raw and not raw.endswith(b"\n"):
        raise ValueError("work log has an unterminated tail; inspect without repair")
    for line in raw.splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line, parse_constant=reject_constant)
        except (UnicodeError, ValueError) as error:
            raise ValueError(
                "work log contains malformed JSON; inspect without repair"
            ) from error
        if (
            type(item) is not dict
            or type(item.get("v")) is not int
            or item["v"] not in (1, 2)
        ):
            raise ValueError("work log contains an unsupported record version/object")
        identity = nonempty(item.get("id"), "existing id")
        if identity in ids:
            raise ValueError("work log contains duplicate IDs; inspect without repair")
        ids.add(identity)
    return ids


def build(args, ids):  # noqa: C901 - preserve the ported validation sequence
    recorded_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    identity = nonempty(args.id if args.id is not None else uuid.uuid4().hex, "id")
    if identity in ids:
        raise ValueError("duplicate id: " + identity)
    at = args.at if args.at is not None else recorded_at
    timestamp(at, "at")
    record = {
        "v": 2,
        "id": identity,
        "at": at,
        "recorded_at": recorded_at,
        "task": nonempty(args.task, "task"),
        "stage": nonempty(args.stage, "stage"),
        "role": choice(args.role, "role", ROLES),
        "agent": nonempty(args.agent, "agent"),
        "event": choice(args.event, "event", EVENTS),
        "result": nonempty(args.result, "result"),
        "allowance": None,
    }
    if args.ref:
        record["refs"] = [nonempty(ref, "ref") for ref in args.ref]
    if args.note is not None:
        if type(args.note) is not str:
            raise ValueError("note must be a string")
        record["note"] = args.note
    if args.cause is not None:
        record["cause"] = choice(args.cause, "cause", CAUSES)
    if args.event in ("return", "blocked") and "cause" not in record:
        raise ValueError("return/blocked requires cause")
    if args.event == "correction":
        target = nonempty(args.supersedes, "supersedes")
        if target not in ids:
            raise ValueError("correction target does not exist")
        record["supersedes"] = target
    elif args.supersedes is not None:
        raise ValueError("supersedes is valid only for correction")
    if args.span is not None:
        record["span"] = nonempty(args.span, "span")
    timing = load_nested(args.timing_file, "timing file")
    if args.timing_file is not None:
        record["timing"] = validate_timing(timing)
    allowance = load_nested(args.allowance_file, "allowance file")
    if args.allowance_file is not None:
        record["allowance"] = validate_allowance(allowance)
    return record


def append(args):
    if fcntl is None or not hasattr(fcntl, "flock"):
        raise ValueError("exclusive local file locking is unsupported on this platform")
    flags = os.O_RDWR | os.O_CREAT
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(args.log, flags, 0o600)
    with os.fdopen(fd, "r+b") as stream:
        try:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        except OSError as error:
            raise ValueError(
                "exclusive local file locking failed: " + str(error)
            ) from error
        raw = stream.read()
        ids = existing_ids(raw)
        record = build(args, ids)
        line = (
            json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        try:
            stream.seek(0, os.SEEK_END)
            if stream.write(line) != len(line):
                raise OSError("short append")
            stream.flush()
            os.fsync(stream.fileno())
        except OSError as error:
            raise ValueError(
                "append may be partial; inspect log before retry: " + str(error)
            ) from error
    return record


def schema():
    return {
        "version": 2,
        "commands": ["append", "schema"],
        "required_flags": ["task", "stage", "role", "agent", "event", "result"],
        "optional_flags": [
            "log",
            "at",
            "id",
            "ref (repeatable)",
            "note",
            "cause",
            "supersedes",
            "span",
            "timing-file",
            "allowance-file",
        ],
        "record": {
            "required": [
                "v",
                "id",
                "at",
                "recorded_at",
                "task",
                "stage",
                "role",
                "agent",
                "event",
                "result",
                "allowance",
            ],
            "optional": ["refs", "note", "cause", "supersedes", "span", "timing"],
            "fields": {
                "v": "integer 2",
                "id": "nonempty unique string",
                "at": "RFC3339 UTC string",
                "recorded_at": "current RFC3339 UTC string",
                "task": "nonempty string",
                "stage": "nonempty string",
                "role": "listed role",
                "agent": "nonempty string",
                "event": "listed event",
                "result": "nonempty string",
                "allowance": "null or supplied allowance-file object",
                "refs": "list of nonempty strings",
                "note": "string",
                "cause": "listed cause",
                "supersedes": "existing ID, correction only",
                "span": "nonempty string",
                "timing": "supplied timing-file object",
            },
            "roles": ROLES,
            "events": EVENTS,
            "causes": CAUSES,
            "correction_requires_existing_supersedes": True,
            "return_and_blocked_require_cause": True,
            "timestamp": "RFC3339 UTC (Z or +00:00)",
        },
        "timing_file": {
            "required": sorted(TIMING_REQUIRED),
            "optional": sorted(TIMING_OPTIONAL),
            "kind": KINDS,
            "measurement": MEASUREMENTS,
            "span_location": "top-level --span",
            "parent_span_location": "timing.parent_span",
            "started_at": "RFC3339 UTC string",
            "ended_at": "RFC3339 UTC string or null; cannot precede start",
            "parent_span": "nonempty string when supplied",
            "duration_ms": "finite nonnegative number or null; null when ended_at is null",
            "utc_elapsed": "closed duration matches UTC boundaries rounded to milliseconds",
        },
        "allowance_file": {
            "required": sorted(ALLOWANCE_REQUIRED),
            "optional": [],
            "other_activity": ACTIVITIES,
            "observed_at": "RFC3339 UTC string",
            "source": "nonempty string",
            "limit_id": "nonempty string",
            "window_minutes": "positive integer",
            "reset_at_unix": "nonnegative integer",
            "remaining_percent": "finite number from 0 to 100",
        },
        "history_admission": "JSON objects with unique nonempty IDs and v=1 or v=2; old fields are not revalidated",
    }


def parser():
    top = argparse.ArgumentParser(description=__doc__)
    commands = top.add_subparsers(dest="command", required=True)
    commands.add_parser(
        "schema", help="print the exact record, timing and allowance schema as JSON"
    )
    write = commands.add_parser("append", help="validate and append one event")
    write.add_argument(
        "--log",
        type=Path,
        default=DEFAULT_LOG,
        help="local JSONL file (default: repository work log)",
    )
    for name in ("task", "stage", "role", "agent", "event", "result"):
        write.add_argument("--" + name, required=True)
    write.add_argument(
        "--at", help="known event time in RFC3339 UTC; default: recorded_at"
    )
    write.add_argument("--id", help="unique event ID; generated when omitted")
    write.add_argument(
        "--ref", action="append", help="reference; repeat for multiple values"
    )
    write.add_argument("--note")
    write.add_argument(
        "--cause", help="required for return/blocked and caller-reported failures"
    )
    write.add_argument("--supersedes", help="existing ID, required only for correction")
    write.add_argument("--span", help="optional top-level span ID")
    write.add_argument(
        "--timing-file", type=Path, help="JSON object with supplied timing data"
    )
    write.add_argument(
        "--allowance-file", type=Path, help="JSON object with supplied allowance sample"
    )
    return top


def main(argv=None):
    args = parser().parse_args(argv)
    if args.command == "schema":
        print(json.dumps(schema(), indent=2, sort_keys=True))
        return 0
    try:
        record = append(args)
    except (OSError, ValueError) as error:
        print("work_log: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
