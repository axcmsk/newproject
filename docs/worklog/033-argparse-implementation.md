# Standard CLI parsing implementation evidence

Approved contract: `docs/worklog/031-argparse-task.md` at `1cef241f0a9893a63c35f906449508acfdb17e47`, with `docs/specs/newproject.md`; specification acceptance: `docs/worklog/032-argparse-spec-review.md` at `dbc3e81`. Implementation started from `dbc3e81`. The checked source is committed together with this report; no executable inputs changed after checks. Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

The parser now uses standard `argparse` for the positional name, boolean flag and help; domain validation and creation safeguards remain in place. CLI tests exercise help and syntax errors with both templates and Git unavailable, both flag positions, repeated flags, and terminator-based literal flag names alongside the existing creation and journal regressions.

- `python3 -m unittest discover -s tests -v` — passed: 26 tests in 5.494s (`OK`).
- `.venv/bin/python -m ruff check newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts` — passed (`4 files already formatted`).
- `git diff --check` — passed.

Checks ran on this host with temporary fixtures; no other platforms were exercised.
