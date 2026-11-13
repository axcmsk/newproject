#!/usr/bin/env python3
"""Commit exactly the reports produced by a completed review."""

import argparse
import os
import stat
import subprocess
import sys
from pathlib import Path


class RefusalError(Exception):
    pass


def git(*args, check=True, literal=False):
    env = os.environ.copy()
    if literal:
        env["GIT_LITERAL_PATHSPECS"] = "1"
    result = subprocess.run(  # noqa: S603
        ["git", *args],  # noqa: S607
        capture_output=True,
        env=env,
    )
    if check and result.returncode:
        raise RefusalError(
            f"git {' '.join(args)} failed: {os.fsdecode(result.stderr).strip()}"
        )
    return result


def output(*args):
    return os.fsdecode(git(*args).stdout).strip()


def repository_state(head, branch):
    if output("rev-parse", "HEAD") != head:
        raise RefusalError("HEAD differs from the recorded review start")
    if output("symbolic-ref", "--quiet", "--short", "HEAD") != branch:
        raise RefusalError("branch changed or HEAD is detached")
    for name in (
        "MERGE_HEAD",
        "rebase-merge",
        "rebase-apply",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD",
        "sequencer",
        "BISECT_LOG",
        "BISECT_START",
    ):
        if Path(output("rev-parse", "--git-path", name)).exists():
            raise RefusalError(f"Git operation in progress: {name}")


def check_index_flags():
    entries = git("ls-files", "-v", "-z").stdout.split(b"\0")
    for entry in entries:
        if entry and (entry[:1] == b"S" or entry[:1].islower()):
            raise RefusalError(
                f"index flag hides worktree changes: {os.fsdecode(entry[2:])!r}"
            )


def changes(allowed, operational=()):
    check_index_flags()
    raw = git(
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
        "--no-renames",
        "--ignore-submodules=none",
    ).stdout
    changed = set()
    for item in raw.split(b"\0"):
        if not item:
            continue
        status, path = os.fsdecode(item[:2]), os.fsdecode(item[3:])
        if path in operational:
            if status != " M":
                raise RefusalError(
                    f"unsupported operational change {status!r}: {path!r}"
                )
            continue
        if path not in allowed:
            raise RefusalError(f"change outside supplied reports: {path!r}")
        if status != "??" and any(c not in " AM" for c in status):
            raise RefusalError(f"unsupported change {status!r}: {path!r}")
        entry = git("ls-files", "--stage", "-z", "--", path, literal=True).stdout
        for line in entry.split(b"\0"):
            if line and line.split(b" ", 1)[0] not in (b"100644", b"100755"):
                raise RefusalError(f"unsupported index file type: {path!r}")
        changed.add(path)
    return changed


def validate_path(path):
    if (
        not path.startswith("docs/worklog/")
        or not path.endswith(".md")
        or any(part in ("", ".", "..") for part in path.split("/"))
        or path.startswith(":")
        or "\\" in path
    ):
        raise RefusalError(f"noncanonical report path: {path!r}")
    current = Path(".")
    for part in path.split("/"):
        current = current / part
        if current.is_symlink():
            raise RefusalError(f"symlink in report path: {path!r}")
    if not current.is_file():
        raise RefusalError(f"report is not an existing regular file: {path!r}")
    # Ignored tracked files remain valid; untracked ignored files cannot be added.
    tracked = git("ls-files", "--error-unmatch", "--", path, check=False, literal=True)
    ignored = git("check-ignore", "-q", "--", path, check=False)
    if tracked.returncode and ignored.returncode == 0:
        raise RefusalError(f"untracked report is ignored: {path!r}")
    if ignored.returncode not in (0, 1):
        raise RefusalError(f"could not check ignore status: {path!r}")


def operational_snapshot(path):
    if (
        path.startswith(("/", ":"))
        or "\\" in path
        or any(part in ("", ".", "..", ".git") for part in path.split("/"))
    ):
        raise RefusalError(f"noncanonical operational path: {path!r}")
    current = Path(".")
    for part in path.split("/"):
        current = current / part
        if current.is_symlink():
            raise RefusalError(f"symlink in operational path: {path!r}")
    if not current.is_file():
        raise RefusalError(
            f"operational path is not an existing regular file: {path!r}"
        )
    index = git("ls-files", "--stage", "-z", "--", path, literal=True).stdout
    head = git("ls-tree", "-z", "HEAD", "--", path, literal=True).stdout
    index_parts = index.split(b"\t", 1)[0].split()
    head_parts = head.split(b"\t", 1)[0].split()
    if (
        len(index_parts) != 3
        or len(head_parts) != 3
        or index_parts[0] not in (b"100644", b"100755")
        or index_parts[2] != b"0"
        or head_parts != [index_parts[0], b"blob", index_parts[1]]
        or not index.endswith(b"\0")
        or index.count(b"\0") != 1
        or head.count(b"\0") != 1
    ):
        raise RefusalError(f"operational index must match regular HEAD file: {path!r}")
    return current.read_bytes(), stat.S_IMODE(current.stat().st_mode), index


def check_snapshots(snapshots):
    for path, expected in snapshots.items():
        if operational_snapshot(path) != expected:
            raise RefusalError(f"operational snapshot changed: {path!r}")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--head", required=True)
    parser.add_argument("-m", "--message", required=True)
    parser.add_argument("--allow-dirty", action="append", default=[])
    parser.add_argument("paths", nargs="+")
    return parser.parse_args()


def validate_environment():
    forbidden = {
        "GIT_DIR",
        "GIT_WORK_TREE",
        "GIT_COMMON_DIR",
        "GIT_INDEX_FILE",
        "GIT_OBJECT_DIRECTORY",
        "GIT_ALTERNATE_OBJECT_DIRECTORIES",
        "GIT_NAMESPACE",
        "GIT_CEILING_DIRECTORIES",
        "GIT_DISCOVERY_ACROSS_FILESYSTEM",
        "GIT_LITERAL_PATHSPECS",
        "GIT_GLOB_PATHSPECS",
        "GIT_NOGLOB_PATHSPECS",
        "GIT_ICASE_PATHSPECS",
        "GIT_CONFIG",
        "GIT_CONFIG_COUNT",
    }
    overrides = sorted(
        k for k in os.environ if k in forbidden or k.startswith("GIT_CONFIG_")
    )
    if overrides:
        raise RefusalError(f"unsafe Git environment overrides: {', '.join(overrides)}")


def preflight(args):
    if (
        "\n" in args.message
        or "\r" in args.message
        or not args.message.startswith("review: ")
        or not args.message[8:].strip()
    ):
        raise RefusalError(
            "message must be one line starting with 'review: ' and a nonblank subject"
        )
    if output("rev-parse", "--is-bare-repository") != "false":
        raise RefusalError("repository must be non-bare")
    if Path(output("rev-parse", "--show-toplevel")).resolve() != Path.cwd().resolve():
        raise RefusalError("invoke from the repository root")
    actual = output("rev-parse", "HEAD")
    if args.head != actual:
        raise RefusalError("--head must equal the full recorded HEAD object ID")
    branch = output("symbolic-ref", "--quiet", "--short", "HEAD")
    repository_state(actual, branch)
    return actual, branch


def commit_reports(args, actual, branch):
    allowed = set(args.paths)
    for path in allowed:
        validate_path(path)
    operational = set(args.allow_dirty)
    if allowed & operational:
        raise RefusalError("report and operational paths overlap")
    snapshots = {path: operational_snapshot(path) for path in operational}
    changed = changes(allowed, operational)
    check_snapshots(snapshots)
    if not changed:
        raise RefusalError("no permitted report changes")
    git("add", "--", *sorted(changed), literal=True)
    repository_state(actual, branch)
    for path in allowed:
        validate_path(path)
    changes(allowed, operational)
    check_snapshots(snapshots)
    tree = output("write-tree")
    git("commit", "-m", args.message)
    new_head = output("rev-parse", "HEAD")
    parents = output("rev-list", "--parents", "-n", "1", new_head).split()
    if (
        parents != [new_head, actual]
        or output("rev-parse", f"{new_head}^{{tree}}") != tree
    ):
        raise RefusalError("commit parent or tree differs from the expected result")
    repository_state(new_head, branch)
    if changes(set(), operational):
        raise RefusalError("repository is not clean after commit")
    check_snapshots(snapshots)
    return new_head


def report_failure(exc, safe_environment):
    print(f"review commit failed: {exc}", file=sys.stderr)
    try:
        if not safe_environment:
            raise RefusalError("unsafe environment")
        print(f"Observed HEAD: {output('rev-parse', 'HEAD')}", file=sys.stderr)
    except (RefusalError, OSError):
        print("Observed HEAD unavailable", file=sys.stderr)
    print(
        "Inspect repository state before retrying; the index may be staged or a commit may already exist.",
        file=sys.stderr,
    )


def main():
    args = parse_args()
    safe_environment = False
    try:
        validate_environment()
        safe_environment = True
        actual, branch = preflight(args)
        new_head = commit_reports(args, actual, branch)
        print(new_head)
        return 0
    except (RefusalError, OSError) as exc:
        report_failure(exc, safe_environment)
        return 1


if __name__ == "__main__":
    sys.exit(main())
