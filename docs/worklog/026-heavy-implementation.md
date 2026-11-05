# Heavy implementation evidence

## Initial baseline checks

Checked source: `236ea1a1d0336c1d53c7f6a07ca6a705217e7757` on `codex/heavy-template`. The working tree contained LEAD's uncommitted specification, documentation and heavy payload drafts; the existing code and tests were unchanged. These checks precede the specification checkpoint and use the baseline commands, before the planned expanded check targets exist.

Environment: Python 3.9.6; Git 2.54.0; Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed, 11 tests in 2.509s (`OK`).
- `.venv/bin/python -m ruff check newproject.py tests/test_newproject.py` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check newproject.py tests/test_newproject.py` — passed (`2 files already formatted`).

No implementation was performed at this checkpoint. Expanded checks remain required after implementation.

## Implementation checks

Approved contract: `docs/worklog/025-heavy-task.md` at `71bf1e3`; specification verdict `docs/worklog/029-heavy-spec-review.md` at `610a238`. Implementation started from `610a238`. The checked source is the implementation committed with this report; no code, test or configuration changes occurred after these checks. Runtime: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed, 25 tests in 4.868s (`OK`). An earlier run exposed a faulty unsupported-lock test assertion; the test was corrected to reach and assert the actual refusal, then the suite was rerun successfully.
- `.venv/bin/python -m ruff check newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts` — passed (`4 files already formatted`).

The journal writer is sourced from DiBBS commit `767ced76e8f08810c11cf499cbcbc80a11f5238b`, `scripts/workflow/work_log.py`: branding removed, imports/format and one unnecessary mode argument adjusted for Ruff, and complexity suppression added. Tests adapt `tests/tooling/test_work_log.py` from that commit to temporary synthetic v1/v2 history, add unsupported-lock coverage, and preserve concurrent and duplicate-ID race checks. Generated-project integration checks use real templates and a temporary destination, including the default journal path from a different working directory. The configured test fixture uses real Git; no real sibling project or journal was modified.

The generated Markdown link audit found no missing internal targets in the combined layers. The two links from the base LEAD guide to sibling `common/DIALOGUE.md` and `common/EDITING.md` are intentional optional external preferences, as confirmed by LEAD. The normal/heavy onboarding chain and layer separation were inspected. POSIX locking is required for append; unsupported locking was simulated and refused without creating the log. Checks were run on this host only; other supported platforms were not exercised.
