# Single readiness check

## Assignment

HUMAN authorized a bounded mechanical refinement on `codex/merge-script`, baseline `9536d599b983a5cb6b56de068d56b64e330a9d25`: remove the first `ready(target, source, source_tip, target_tip)` call in `merge.py`, keeping the call immediately after `choose_mode`. Preserve the branch-tip pinning and remaining logic. Allowed writes are `merge.py` and this combined assignment/evidence report. Run the full configured tests, expanded Ruff lint and formatting checks, commit checked inputs with `fixup:`, and hand off for independent review. Do not merge or push.

Sources: `merge.py`, `tests/test_merge.py`, and `docs/specs/merge.md` at the baseline. The sole code diff deletes the first readiness call. The retained call still checks the pinned tips, attached target, operation markers and cleanliness after read-only mode selection and before the merge; the existing real-Git tests exercise successful modes and precondition refusals. If more than one precondition is invalid, selecting the mode first may change which refusal is reported. No new call-count test was added.

## Checks

Checked source: baseline plus the single deletion committed with this report. Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed, 40 tests in 14.045s (`OK`).
- `.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).

Checks ran on this host using temporary repositories; independent review remains pending. No merge or push was performed.
