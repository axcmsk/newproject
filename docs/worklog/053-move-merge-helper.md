# Move merge helper

## Assignment

HUMAN authorized moving the merge helper to `tools/merge.py` and, after checks and independent review, merging the feature branch into main. Baseline: `8896956473dfda3ecead57555bd4c415bc6d086d` on `codex/merge-script`. This bounded mechanical task moves `merge.py` unchanged, updates the test's script path and records evidence here. LEAD prepared and released the exact accompanying changes to `README.md`, `docs/specs/merge.md` and `docs/workflow/MERGE.md` for inclusion. No algorithm change or template/generator installation is authorized. LEAD owns any subsequent merge; DEVELOPER does not merge or push.

## Evidence

Compared `tools/merge.py` byte-for-byte with `merge.py` at baseline using `cmp` and `git show`; they match. `tests/test_merge.py` changes only its script path, and its real-Git CLI and in-process cases exercise the relocated helper. Checked source is the baseline plus these assigned changes and LEAD's released documentation, committed with this report. Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed, 40 tests in 12.810s (`OK`).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).
- `git diff --check` — passed.

Checks ran on this host with temporary repositories. Independent review remains pending; no merge or push was performed.
