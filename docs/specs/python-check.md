# Python checks

`python3 tools/python_check.py` runs this repository's configured checks sequentially.
Requires Python 3.9+, Git for the existing tests, and Ruff installed in the
repository's `.venv` as documented in README. The helper uses standard-library
Python and does not install dependencies. Source formatting is opt-in.

## Invocation and sequence

Support boolean `--reformat`, optional `--only {format,lint,tests}` and standard
argparse `-h`/`--help`, with no parallel execution or configuration file. Unexpected arguments fail with
status 2; help exits 0 without starting checks or requiring Ruff. Resolve the
repository from the helper's location, independent of the caller's cwd. Run all
checks with the repository root as cwd, with argument lists and no shell.
Both modes use the same sequence: formatting, lint, tests. Without the flag:

1. `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`
2. `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`
3. The invoking Python interpreter (`sys.executable`) with
   `-m unittest discover -s tests -v`.

Use the local virtual environment's Python for both Ruff checks; no fallback to
a global Ruff or automatic installation. Tests use the invoking interpreter,
equivalent to the documented python3 command when invoked as above.
With `--reformat`, omit only `--check` from the first command; all other
arguments and the order remain the same.

`--only` selects exactly one of these steps, retaining its arguments, targets,
working directory and output behavior. With no selection run all three.
`--only format --reformat` applies formatting only. Reject `--reformat` combined
with `--only lint` or `--only tests` as an argparse error (exit 2) before starting
any checks. Invalid choices and missing values also fail before checks; standard
argparse option repetition/order rules apply. The wrapper starts no omitted step
and performs no separate availability check for its tools; dependencies used
internally by the selected check still apply, including Ruff used by this
repository's tests.

Use the same target list for both formatting modes and lint. The formatting step
may modify files; do not run a subsequent `format --check` in this mode. A
successful formatter run supplies the formatting result. If it fails or cannot
start, return overall failure. In a full run, still run lint and tests; a
format-only run must not launch other steps. Preserve partial
formatting edits; do not roll back. Do not run lint fixes, Git mutations, commits
or review operations. Help must explain that --reformat writes formatting changes.

## Output and failures

Print a clear label and command before each check, flushing before the child
starts. Stream child stdout/stderr to the caller; do not capture and replay long
logs. Report each check's exit status or launch error, then a compact final
summary naming only the selected results (all three by default). Use human-readable output, with no persistent
log/state service or JSON schema.

Run every selected check even when an earlier check fails or cannot start. Wait for each
child to finish before starting the next. Return 0 only when all selected checks succeeded;
otherwise return 1. Distinguish launch errors from nonzero child exit codes and
never print success for an unavailable tool. On user interruption, stop the
sequence and do not claim a completed result or start remaining checks. No retry,
parallel scheduling, timeout policy or process orchestration framework.

## Integration and verification

README uses this command as the normal full-check entry point and retains the
installation command. Expose individual checks and formatting through helper
options, with no direct tool invocation in README except installing Ruff.
An individual selection does not satisfy a requirement to run the full suite.
Document the optional writing mode and its order. The repository's check policy
permits this mode to satisfy formatting verification in the same run without
another formatting check; default usage stays read-only with respect to sources.
Update the repository-specific setup/check reference in PROJECT-RULES if needed;
role/check ownership stays unchanged. This helper is specific to this repository's
commands and is not installed into generated projects. The common template
defines a check-command convention; each project configures its own commands
and targets. Existing tools and generator behavior remain unchanged.

Use focused tests covering:

- Command order, arguments, exact targets and cwd in both formatting modes;
  CLI flag propagation, default non-writing behavior and no redundant formatting
  check.
- Each `--only` choice, including formatting write/check variants and both flag
  orders: launch exactly the selected command and report only its result.
  Tests-only launches unittest; its internal dependencies still apply.
- Continuation after failures or launch errors, overall status, streamed output
  and summaries, for full and selected runs; interruption stops the sequence.
- Help, invalid arguments, invalid choices, missing values and incompatible
  flags: no checks start.
- Real formatting of intentionally unformatted Python in a temporary fixture,
  asserting the resulting contents.

Use temporary fixtures, small fake checks or bounded subprocess substitution;
never recursively run the real suite from helper tests. Preserve short,
coherent functions and a readable entry point.

Before the source checkpoint, run the full helper with `--reformat` and diff
checks. Retain all three check outcomes and the overall result. Successful
results remain valid while their inputs are unchanged; do not repeat
`format --check` or the suite solely to reconfirm them.
