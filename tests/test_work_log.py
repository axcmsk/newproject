#!/usr/bin/env python3
"""CLI-level focused checks for the local work-log writer."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1] / "template/heavy/scripts/workflow/work_log.py"
)
BASE = (
    "--task",
    "work-log-cli",
    "--stage",
    "implementation",
    "--role",
    "DEVELOPER",
    "--agent",
    "/root/developer",
    "--event",
    "check_result",
    "--result",
    "passed",
)


class WorkLogCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="work-log-test-")
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        self.log = self.dir / "log.jsonl"

    def command(self, *args, log=None):
        return [
            sys.executable,
            str(SCRIPT),
            "append",
            "--log",
            str(log or self.log),
            *BASE,
            *args,
        ]

    def run_cli(self, *args, log=None, ok=True):
        result = subprocess.run(  # noqa: S603 - controlled test command
            self.command(*args, log=log), capture_output=True, text=True
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, "")
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        return result.stderr

    def rows(self):
        return [json.loads(line) for line in self.log.read_text().splitlines()]

    def file(self, name, value):
        path = self.dir / name
        path.write_text(json.dumps(value))
        return path

    def unchanged_refusal(self, *args):
        before = self.log.read_bytes() if self.log.exists() else b""
        self.run_cli(*args, ok=False)
        self.assertEqual(self.log.read_bytes(), before)

    def test_schema_and_help(self):
        schema = subprocess.run(  # noqa: S603 - controlled test command
            [sys.executable, str(SCRIPT), "schema"], capture_output=True, text=True
        )
        self.assertEqual(schema.returncode, 0)
        data = json.loads(schema.stdout)
        self.assertEqual(data["version"], 2)
        self.assertIn("return", data["record"]["events"])
        self.assertEqual(
            data["timing_file"]["parent_span_location"], "timing.parent_span"
        )
        help_result = subprocess.run(  # noqa: S603 - controlled test command
            [sys.executable, str(SCRIPT), "append", "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(help_result.returncode, 0)
        for flag in ("--timing-file", "--allowance-file", "--supersedes", "--ref"):
            self.assertIn(flag, help_result.stdout)

    def test_now_explicit_time_and_unique_ids(self):
        first = self.run_cli(
            "--ref", "source-sha", "--ref", "report.md", "--note", "observed"
        )
        self.assertEqual(first["v"], 2)
        self.assertEqual(first["at"], first["recorded_at"])
        self.assertEqual(first["refs"], ["source-sha", "report.md"])
        self.assertEqual(first["allowance"], None)
        explicit = "2026-10-31T13:00:01.123Z"
        second = self.run_cli("--at", explicit, "--id", "explicit-event")
        self.assertEqual(second["at"], explicit)
        self.assertNotEqual(second["recorded_at"], explicit)
        self.assertNotEqual(first["id"], second["id"])
        self.assertEqual(
            [row["id"] for row in self.rows()], [first["id"], "explicit-event"]
        )
        self.unchanged_refusal("--id", "explicit-event")

    def test_corrections_cause_and_no_span_management(self):
        first = self.run_cli("--id", "original", "--span", "span-a", "--cause", "test")
        self.assertEqual(first["span"], "span-a")
        correction = self.run_cli(
            "--id", "fix", "--event", "correction", "--supersedes", "original"
        )
        self.assertEqual(correction["supersedes"], "original")
        self.unchanged_refusal("--event", "correction", "--supersedes", "missing")
        self.unchanged_refusal("--supersedes", "original")
        self.unchanged_refusal("--event", "return")
        self.unchanged_refusal("--event", "blocked")
        blocked = self.run_cli(
            "--id", "blocked", "--event", "blocked", "--cause", "environment"
        )
        self.assertEqual(blocked["cause"], "environment")
        # Reusing a span is deliberately not a cross-record lifecycle error.
        self.run_cli("--id", "complete", "--event", "complete", "--span", "span-a")

    def test_invalid_ordinary_fields_leave_bytes(self):
        self.run_cli("--id", "seed")
        for arguments in (
            ("--task", " "),
            ("--stage", ""),
            ("--role", "COORDINATOR"),
            ("--event", "unknown"),
            ("--ref", ""),
            ("--id", ""),
            ("--at", "2026-10-31T13:00:00+01:00"),
            ("--at", "not-a-time"),
        ):
            with self.subTest(arguments=arguments):
                self.unchanged_refusal(*arguments)

    def test_timing_supplied_and_rejected(self):
        open_timing = {
            "kind": "work",
            "started_at": "2026-10-31T13:00:00Z",
            "ended_at": None,
            "duration_ms": None,
            "measurement": "tool_reported",
            "parent_span": "parent",
        }
        path = self.file("timing.json", open_timing)
        row = self.run_cli(
            "--id", "open", "--span", "span-1", "--timing-file", str(path)
        )
        self.assertEqual(row["timing"], open_timing)
        self.assertEqual(row["span"], "span-1")
        closed = dict(
            open_timing,
            ended_at="2026-10-31T13:00:01.250Z",
            duration_ms=1250,
            measurement="utc_elapsed",
        )
        path = self.file("closed.json", closed)
        self.assertEqual(
            self.run_cli("--timing-file", str(path))["timing"]["duration_ms"], 1250
        )
        for name, invalid in (
            ("extra", dict(open_timing, extra=True)),
            ("bool", dict(open_timing, duration_ms=True)),
            ("negative", dict(open_timing, duration_ms=-1)),
            ("reversed", dict(closed, ended_at="2026-10-31T12:59:59Z")),
            ("mismatch", dict(closed, duration_ms=1249)),
            ("nonfinite", dict(closed, duration_ms=float("nan"))),
            ("missing", {"kind": "work"}),
        ):
            with self.subTest(name=name):
                self.unchanged_refusal(
                    "--timing-file", str(self.file(name + ".json", invalid))
                )
        reported = dict(closed, measurement="tool_reported", duration_ms=345)
        self.assertEqual(
            self.run_cli("--timing-file", str(self.file("reported.json", reported)))[
                "timing"
            ]["duration_ms"],
            345,
        )

    def test_allowance_sample_preserved_and_rejected(self):
        sample = {
            "observed_at": "2026-10-31T13:47:49Z",
            "source": "supplied observation",
            "limit_id": "codex",
            "window_minutes": 10080,
            "reset_at_unix": 1793892106,
            "remaining_percent": 21,
            "other_activity": "unknown",
        }
        row = self.run_cli("--allowance-file", str(self.file("allowance.json", sample)))
        self.assertEqual(row["allowance"], sample)
        self.assertNotEqual(row["allowance"]["observed_at"], row["recorded_at"])
        for name, invalid in (
            ("extra", dict(sample, extra="x")),
            ("bool", dict(sample, remaining_percent=True)),
            ("negative", dict(sample, reset_at_unix=-1)),
            ("range", dict(sample, remaining_percent=101)),
            ("bad-time", dict(sample, observed_at="yesterday")),
            ("nonfinite", dict(sample, remaining_percent=float("inf"))),
            ("missing", {"source": "x"}),
        ):
            with self.subTest(name=name):
                self.unchanged_refusal(
                    "--allowance-file", str(self.file(name + ".json", invalid))
                )

    def test_existing_history_refusal_and_correction_target(self):
        self.log.write_text('{"v":1,"id":"old"}\n')
        self.assertEqual(
            self.run_cli("--event", "correction", "--supersedes", "old")["supersedes"],
            "old",
        )
        good = self.log.read_bytes()
        for tail in (
            b'{"v":1,"id":"cut"',
            b"{bad}\n",
            b'{"v":1,"id":"old"}\n',
            b'{"v":3,"id":"new"}\n',
        ):
            self.log.write_bytes(good + tail)
            before = self.log.read_bytes()
            self.run_cli(ok=False)
            self.assertEqual(self.log.read_bytes(), before)
        for token in (b"NaN", b"Infinity", b"-Infinity"):
            with self.subTest(nonstandard_constant=token):
                self.log.write_bytes(
                    good + b'{"v":1,"id":"nonfinite","unused":' + token + b"}\n"
                )
                before = self.log.read_bytes()
                error = self.run_cli(
                    ok=False
                )  # also asserts no success record on stdout
                self.assertIn("malformed JSON", error)
                self.assertEqual(self.log.read_bytes(), before)
        self.log.write_bytes(good)

    def test_concurrent_whole_lines_and_duplicate_race(self):
        children = [
            subprocess.Popen(  # noqa: S603 - controlled test command
                self.command("--id", "parallel-" + str(i)),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for i in range(8)
        ]
        for child in children:
            stdout, stderr = child.communicate(timeout=20)
            self.assertEqual(child.returncode, 0, stderr.decode())
            self.assertTrue(json.loads(stdout)["id"].startswith("parallel-"))
        self.assertEqual(len(self.rows()), 8)
        same = [
            subprocess.Popen(  # noqa: S603 - controlled test command
                self.command("--id", "race"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for _ in range(2)
        ]
        results = [child.communicate(timeout=20) for child in same]
        self.assertEqual(sorted(child.returncode for child in same), [0, 1])
        self.assertEqual(sum(row["id"] == "race" for row in self.rows()), 1)
        self.assertTrue(any(b"duplicate id" in stderr for _, stderr in results))

    def test_synthetic_history_preserves_prefix(self):
        historical = b'{"v":1,"id":"old"}\n{"v":2,"id":"new"}\n'
        self.log.write_bytes(historical)
        row = self.run_cli("--id", "temporary-copy-new-event")
        result = self.log.read_bytes()
        self.assertTrue(result.startswith(historical))
        self.assertEqual(json.loads(result[len(historical) :])["id"], row["id"])

    def test_unsupported_lock(self):
        import importlib.util
        from unittest import mock

        spec = importlib.util.spec_from_file_location("journal", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with (
            mock.patch.object(module, "fcntl", None),
            mock.patch.object(sys, "argv", self.command("--id", "no-lock")[1:]),
            mock.patch("sys.stderr") as stderr,
        ):
            self.assertNotEqual(module.main(), 0)
        self.assertIn(
            "locking is unsupported",
            "".join(str(c) for c in stderr.write.call_args_list),
        )
        self.assertFalse(self.log.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
