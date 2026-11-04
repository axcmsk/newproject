#!/usr/bin/env python3
"""Create a sibling project from this repository's template."""

import os
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path


class RefusalError(Exception):
    pass


def validate_input(root):
    if len(sys.argv) != 2:
        raise RefusalError("usage: python3 newproject.py NAME")
    name = sys.argv[1]
    if (
        not name
        or name in (".", "..")
        or "/" in name
        or "\\" in name
        or any(unicodedata.category(c) == "Cc" for c in name)
    ):
        raise RefusalError(
            "NAME must be a single directory name without control characters"
        )
    source = root / "template"
    if source.is_symlink() or not source.is_dir():
        raise RefusalError("template must be a real directory")
    entries = []

    def traversal_error(exc):
        raise RefusalError(f"template traversal failed: {exc}") from exc

    for directory, dirs, files in os.walk(
        source, followlinks=False, onerror=traversal_error
    ):
        for item in dirs + files:
            path = Path(directory) / item
            if (
                item == ".git"
                or path.is_symlink()
                or not (path.is_file() or path.is_dir())
            ):
                raise RefusalError(f"invalid template entry: {path}")
            entries.append(path.relative_to(source))
    if not entries:
        raise RefusalError("template is empty")
    return source, entries


def git_runner(env):
    git_path = shutil.which("git", path=env.get("PATH"))
    if not git_path:
        raise RefusalError("Git executable not found")

    def git(*args, cwd=None, check=True):
        try:
            result = subprocess.run(  # noqa: S603 - Git is resolved on PATH; no shell is used.
                [git_path, *args],
                cwd=cwd,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as exc:
            raise RefusalError(f"Git failed: {exc}") from exc
        if check and result.returncode:
            raise RefusalError(f"Git {args[0]} failed: {result.stderr.strip()}")
        return result

    git("--version")
    return git


def validate_target(target, git):
    if target.is_symlink():
        raise RefusalError("target is a symlink")
    if target.exists():
        if not target.is_dir():
            raise RefusalError("target is not a directory")
        contents = list(target.iterdir())
        if contents:
            dotgit = target / ".git"
            if len(contents) != 1 or not dotgit.is_dir() or dotgit.is_symlink():
                raise RefusalError(
                    "target must be empty or contain only its own real .git directory"
                )
            validate_existing_repo(target, dotgit, git)
            return True
    return False


def validate_existing_repo(target, dotgit, git):
    actual = git("rev-parse", "--absolute-git-dir", cwd=target)
    if Path(actual.stdout.strip()).resolve() != dotgit.resolve():
        raise RefusalError("target does not own its Git repository")
    if git("rev-parse", "--is-bare-repository", cwd=target).stdout.strip() != "false":
        raise RefusalError("target Git repository is bare")
    head = git("symbolic-ref", "-q", "HEAD", cwd=target)
    if not head.stdout.strip().startswith("refs/heads/"):
        raise RefusalError("Git HEAD is not an unborn branch")
    if git("for-each-ref", "--format=%(refname)", cwd=target).stdout.strip():
        raise RefusalError("Git repository contains refs")
    if git("rev-parse", "--verify", "HEAD", cwd=target, check=False).returncode == 0:
        raise RefusalError("Git repository contains commits")
    if git("ls-files", "--stage", cwd=target).stdout.strip():
        raise RefusalError("Git repository contains staged entries")


def initialize_git(target, existing_repo, git):
    if existing_repo:
        git("symbolic-ref", "HEAD", "refs/heads/main", cwd=target)
    else:
        with tempfile.TemporaryDirectory(
            prefix="newproject-git-template-"
        ) as empty_template:
            git(
                "init",
                "--initial-branch=main",
                "--template=" + empty_template,
                str(target),
            )


def copy_template(source, target, entries):
    for relative in entries:
        src, dst = source / relative, target / relative
        if src.is_dir():
            dst.mkdir()
        else:
            with src.open("rb") as inp, dst.open("xb") as out:
                shutil.copyfileobj(inp, out)
            shutil.copystat(src, dst)


def main():
    root = Path(__file__).resolve().parent
    target = root.parent / (sys.argv[1] if len(sys.argv) == 2 else "<NAME>")
    mutated = False
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env["GIT_CONFIG_NOSYSTEM"] = "1"

    try:
        source, entries = validate_input(root)
        git = git_runner(env)
        existing_repo = validate_target(target, git)
        if not target.exists():
            target.mkdir()
            mutated = True
        mutated = True
        initialize_git(target, existing_repo, git)
        copy_template(source, target, entries)
        print(f"Created project: {target}")
        return 0
    except (RefusalError, OSError, ValueError) as exc:
        state = (
            " Partial state may remain; inspect the target."
            if mutated
            else " Target unchanged."
        )
        print(f"Cannot create project at {target}: {exc}.{state}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
