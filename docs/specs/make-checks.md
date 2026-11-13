# Repository checks with Make

The root Makefile runs this repository's configured checks. Development requires
Make, Python 3.9+, Git for existing tests, and Ruff installed in `.venv` as
specified in README. No target installs dependencies. Generated projects do not
receive this Makefile; they document their own configured commands.

## Targets

All targets are phony. `check` is the default target, depending on `format`,
`lint`, and `test` in that order. Ordinary invocation runs them sequentially;
explicit parallel Make execution may run independent prerequisites concurrently.

- `format`: `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`
- `lint`: `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`
- `test`: `python3 -m unittest discover -s tests -v`
- `reformat`: `.venv/bin/python -m ruff format tools newproject.py tests template/heavy/scripts`

Ruff uses the local virtual environment without fallback. Both formatting modes
and lint use the same target paths. `format` does not modify sources; `reformat`
applies formatting only, preserving partial edits on failure. No target applies
lint fixes or commits changes. An individual check does not replace the full
suite. Use `make reformat && make check` to format before full verification.

## Invocation and failures

Run from the repository root, or use `make -C /path/to/newproject check` from
another directory. Commands run with the repository root as their working directory.
Make displays commands and tool output, without a custom result summary.
Ordinary Make execution stops on failure and exits nonzero; missing tools are
failures. `make -k check` continues independent checks while retaining a failing
overall status. Interrupts use ordinary Make handling; no custom status mapping,
retry mechanism or orchestration layer is provided.

## Verification

Verify full and individual targets, matching tool arguments and target paths,
non-mutating formatting, reformat on a temporary fixture, failure propagation,
and invocation from another directory. Do not recursively invoke the real suite
from tests. Preserve existing generator and helper coverage. Record executed
checks and their results in task evidence before independent static review.
