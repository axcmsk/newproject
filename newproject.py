#!/usr/bin/env python3
"""Create a sibling project from this repository's template."""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path


class RefusalError(Exception):
    pass


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="Create a sibling project from the template."
    )
    parser.add_argument(
        "--heavy", action="store_true", help="include the heavy workflow"
    )
    parser.add_argument("NAME", help="name of the project directory")
    parsed = parser.parse_args(args)
    name = parsed.NAME
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
    return name, parsed.heavy


def validate_input(root, heavy):  # noqa: C901 - preflight keeps all collision decisions together
    template = root / "template"
    if template.is_symlink() or not template.is_dir():
        raise RefusalError("template must be a real directory")

    def scan(source):
        if source.is_symlink() or not source.is_dir():
            raise RefusalError(f"template layer must be a real directory: {source}")
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
            raise RefusalError(f"template is empty: {source}")
        return entries

    base = template / "base"
    entries = [(base, path) for path in scan(base)]
    composed = None
    if heavy:
        layer = template / "heavy"
        additions = scan(layer)
        base_paths = {path: (base / path).is_dir() for _, path in entries}
        if Path("AGENTS.add.md") in base_paths:
            raise RefusalError("reserved base entry: AGENTS.add.md")
        for path in additions:
            if path in base_paths and (
                not base_paths[path] or not (layer / path).is_dir()
            ):
                raise RefusalError(f"template collision: {path}")
        try:
            base_agent = base / "AGENTS.md"
            fragment = layer / "AGENTS.add.md"
            if not base_agent.is_file() or not fragment.is_file():
                raise RefusalError("AGENTS.md and AGENTS.add.md must be regular files")
            base_text = base_agent.read_bytes().decode("utf-8")
            fragment_text = fragment.read_bytes().decode("utf-8")
            if not base_text or not fragment_text:
                raise RefusalError("AGENTS.md and AGENTS.add.md must be nonempty")
            composed = (
                base_text.rstrip("\n") + "\n\n" + fragment_text.rstrip("\n") + "\n"
            ).encode("utf-8")
        except UnicodeError as exc:
            raise RefusalError(f"invalid UTF-8 in AGENTS metadata: {exc}") from exc
        entries.extend(
            (layer, path)
            for path in additions
            if path != Path("AGENTS.add.md") and path not in base_paths
        )
    return entries, composed


def add_merge_helper(root, entries):
    tools = root / "tools"
    helper = tools / "merge.py"
    if tools.is_symlink() or not tools.is_dir():
        raise RefusalError("helper tools must be a real directory")
    if helper.is_symlink() or not helper.is_file():
        raise RefusalError("merge helper must be a regular file")
    with helper.open("rb") as stream:
        stream.read(1)
    paths = {path: source / path for source, path in entries}
    tools_path = Path("tools")
    helper_path = tools_path / "merge.py"
    if helper_path in paths or (tools_path in paths and not paths[tools_path].is_dir()):
        raise RefusalError("template collision: tools/merge.py")
    if tools_path not in paths:
        entries.append((root, tools_path))
    entries.append((root, helper_path))


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


def copy_template(entries, target, composed):
    for source, relative in entries:
        src, dst = source / relative, target / relative
        if src.is_dir():
            dst.mkdir()
        else:
            with dst.open("xb") as out:
                if composed is not None and relative == Path("AGENTS.md"):
                    out.write(composed)
                else:
                    with src.open("rb") as inp:
                        shutil.copyfileobj(inp, out)
            shutil.copystat(src, dst)


def main():
    root = Path(__file__).resolve().parent
    target = root.parent / "<NAME>"
    mutated = False
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env["GIT_CONFIG_NOSYSTEM"] = "1"

    try:
        name, heavy = parse_args(sys.argv[1:])
        target = root.parent / name
        entries, composed = validate_input(root, heavy)
        add_merge_helper(root, entries)
        git = git_runner(env)
        existing_repo = validate_target(target, git)
        if not target.exists():
            target.mkdir()
            mutated = True
        mutated = True
        initialize_git(target, existing_repo, git)
        copy_template(entries, target, composed)
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
