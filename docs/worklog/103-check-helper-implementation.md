# Sequential check helper implementation

Approved contract `docs/specs/check.md` at
`59da9b0c8fe096a5ca2587e6d68222563f083cf4`, accepted in report 102 at
`7b3607e7e1d58cf325b9110209b04d0ea7c177b0`, the clean starting HEAD on
`codex/check-helper`. Assignment and ownership are recorded in 101.

The helper runs Ruff lint, Ruff format check, and unittest in order from the
repository root. It streams child output, continues after ordinary failures and
launch errors, reports each outcome and a final summary, and stops on interruption.
Focused tests substitute bounded subprocess results to verify order, arguments,
cwd, continuation, summary, interruption, and help/invalid arguments without
recursively invoking the suite. LEAD released README and PROJECT-RULES adoption
edits unchanged for this checkpoint.

## Checked identities and results

SHA-256:

- `tools/check.py`: `fe8b5a9f24b6882919b1131318e5c8f97b8f76bab859f975b3b5739bd5f87751`
- `tests/test_check.py`: `b7643b3673d741f17174fe8b39f6dd853461c4263b4d731b0b409246aa51a166`
- `README.md`: `ae67d4666492e1dbe346902091dc015b0afd33705a64ddbbb23cc58e5a33fee1`
- `docs/workflow/PROJECT-RULES.md`: `438d89daebe9eae63dfea25be162f8e6341e5223f7e84e0cafa48acf03842d11`

Python 3.9.6, Git 2.54.0, Ruff 0.17.3. Final configured invocation
`python3 tools/check.py` completed with overall exit 0. Its sequential outcomes:

1. `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`:
   exit 0, all checks passed.
2. `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
   exit 0, ten files already formatted.
3. Invoking Python `-m unittest discover -s tests -v`: exit 0, 63 tests passed
   in 26.839s.

`git diff --check` and final `git diff --cached --check` passed. The isolated
focused tests and lint also passed before final checks. No failed executable
checks remain. Independent review is pending.
