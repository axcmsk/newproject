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

## Optional human coverage report

`test-coverage` is a separate phony target, excluded from `check`. It runs the
existing unittest suite using optional pinned coverage.py 7.10.7 in `.venv`,
prints per-file statement coverage with missing lines, writes JSON to
`coverage.json`, and writes HTML to `htmlcov/index.html` from the same measured
data without rerunning tests. It includes the four production scripts, Python
subprocess execution and temporary copies, mapped back to canonical repository paths;
tests and measurement internals are excluded from the report.

Use declarative coverage configuration and standard coverage commands. Start
with fresh measurement data and store it outside temporary test repositories.
Ignore generated measurement data, JSON and HTML output. Missing tooling or failing tests must
fail the target; no automatic installation or success-only masking. There is no
coverage threshold and no change to the `check` target or its dependencies.
When handing an implementation to review, DEVELOPER supplies the report under
PROCESS, identifying the measured source version and accessible artifact paths.
REVIEWER reads the JSON per-file totals and missing lines statically; HTML is
supplementary for browsing source.
The report helps HUMAN inspect test coverage and does not establish correctness.
