#!/usr/bin/env python3
"""Run this repository's format, lint and test checks sequentially."""

import argparse
import shlex
import signal
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = ["tools", "newproject.py", "tests", "template/heavy/scripts"]


def run_checks(reformat=False, only=None):
    venv_python = str(ROOT / ".venv/bin/python")
    lint = ("lint", [venv_python, "-m", "ruff", "check", *TARGETS])
    format_args = [] if reformat else ["--check"]
    formatting = (
        "format",
        [venv_python, "-m", "ruff", "format", *format_args, *TARGETS],
    )
    checks = [formatting, lint]
    checks.append(
        ("tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
    )
    if only is not None:
        checks = [item for item in checks if item[0] == only]
    results = []
    try:
        for name, command in checks:
            print(f"\n{name}: {shlex.join(command)}", flush=True)
            try:
                result = subprocess.run(command, cwd=ROOT, check=False)  # noqa: S603
            except OSError as exc:
                outcome = f"launch error: {exc}"
                success = False
            else:
                if result.returncode == -signal.SIGINT:
                    raise KeyboardInterrupt
                outcome = f"exit {result.returncode}"
                success = result.returncode == 0
            print(f"{name}: {outcome}", flush=True)
            results.append((name, outcome, success))
    except KeyboardInterrupt:
        print("\nChecks interrupted.", file=sys.stderr, flush=True)
        return 130
    print("\nSummary: " + "; ".join(f"{name}: {result}" for name, result, _ in results))
    return 0 if all(success for _, _, success in results) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reformat",
        action="store_true",
        help="apply formatting changes instead of checking formatting",
    )
    parser.add_argument(
        "--only",
        choices=("format", "lint", "tests"),
        help="run only the selected check",
    )
    args = parser.parse_args()
    if args.reformat and args.only in ("lint", "tests"):
        parser.error("--reformat requires all checks or --only format")
    return run_checks(args.reformat, args.only)


if __name__ == "__main__":
    sys.exit(main())
