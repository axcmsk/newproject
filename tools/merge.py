#!/usr/bin/env python3
"""Merge local branches using the project's draft mechanical mode rule."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

TARGET = "main"


class MergeError(Exception):
    pass


def git(*args, check=True):
    env = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    try:
        result = subprocess.run(  # noqa: S603 - arguments are never evaluated by a shell.
            ["git", *args],  # noqa: S607 - intentionally resolve Git on PATH.
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
    except OSError as exc:
        raise MergeError(f"git {' '.join(args)} failed: {exc}") from exc
    if check and result.returncode:
        raise MergeError(
            f"git {' '.join(args)} failed: {result.stderr.strip() or result.stdout.strip()}"
        )
    return result


def tip(branch):
    ref = f"refs/heads/{branch}"
    git("check-ref-format", ref)
    result = git("show-ref", "--verify", "--hash", ref)
    return git(
        "rev-parse", "--verify", f"{result.stdout.strip()}^{{commit}}"
    ).stdout.strip()


def clean():
    status = git(
        "status", "--porcelain=v1", "--untracked-files=all", "--ignore-submodules=none"
    ).stdout
    if status:
        raise MergeError(f"working tree or index is not clean:\n{status.rstrip()}")


def ready(target, source, source_tip, target_tip):
    git("rev-parse", "--show-toplevel")
    head = git("symbolic-ref", "--quiet", "--short", "HEAD").stdout.strip()
    if head != target:
        raise MergeError(f"HEAD must be attached to target {target}")
    if tip(source) != source_tip or tip(target) != target_tip:
        raise MergeError("branch tips changed")
    for state in (
        "MERGE_HEAD",
        "rebase-merge",
        "rebase-apply",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD",
        "sequencer",
    ):
        path = git("rev-parse", "--git-path", state).stdout.strip()
        if Path(path).exists():
            raise MergeError(f"unfinished operation: {state}")
    clean()


def choose_mode(source_tip, target_tip):
    subjects = git(
        "log", "--format=%s", f"{target_tip}..{source_tip}"
    ).stdout.splitlines()
    if not subjects:
        raise MergeError("source-exclusive range is empty")
    prefixes = ("step:", "fixup:", "docs:", "review:", "log:")
    return (
        "squash"
        if all(s.startswith(prefixes) for s in subjects)
        and sum(s.startswith("step:") for s in subjects) <= 1
        else "merge"
    )


def perform(source, target, message):
    if source == target:
        raise MergeError("source and target must be distinct")
    if not message.strip():
        raise MergeError("message must not be empty")
    source_tip, target_tip = tip(source), tip(target)
    mode = choose_mode(source_tip, target_tip)
    ready(target, source, source_tip, target_tip)
    options = ["--squash"] if mode == "squash" else ["--no-ff", "--no-commit"]
    try:
        git(
            "-c",
            "merge.ff=true",
            "merge",
            "--no-autostash",
            "--no-overwrite-ignore",
            *options,
            source_tip,
        )
        if mode == "squash":
            diff = git("diff", "--cached", "--quiet", check=False)
            if diff.returncode == 0:
                raise MergeError("squash has no net change; no commit created")
            if diff.returncode != 1:
                raise MergeError(
                    f"git diff --cached --quiet failed: {diff.stderr.strip() or diff.stdout.strip()}"
                )
        git("commit", "--cleanup=verbatim", "-m", message)
        head = git("rev-parse", "HEAD").stdout.strip()
        parents = git("rev-list", "--parents", "-n", "1", head).stdout.split()[1:]
        expected = [target_tip] if mode == "squash" else [target_tip, source_tip]
        if (
            tip(source) != source_tip
            or tip(target) != head
            or git("symbolic-ref", "--quiet", "--short", "HEAD").stdout.strip()
            != target
            or parents != expected
        ):
            raise MergeError("unexpected branch or commit topology after commit")
        clean()
    except MergeError as exc:
        raise MergeError(
            f"{exc}\nState may be partial; inspect the repository. A failed commit may leave staged content."
        ) from exc
    print(f"Created {mode} commit {head}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", metavar="SOURCE")
    parser.add_argument("-m", "--message", required=True, metavar="MESSAGE")
    args = parser.parse_args()
    try:
        perform(args.source, TARGET, args.message)
    except MergeError as exc:
        print(f"Cannot merge: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
