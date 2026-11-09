# Adopt review commit helper: implementation

Approved specification: `docs/specs/newproject.md` at
`27177ed212635cd19fa5bd0ecb704b0caffc9af9`, accepted by report 087 at
`e24d9878352e9af027cdaef07f2d34f71a5d2470`. Starting HEAD was that report
commit on `codex/adopt-review-commit`, with a clean working tree.

The generator preflights both named root helpers and selected-layer collisions,
then copies only those helper paths with the existing exclusive creation and mode
preservation. Tests cover invalid and unreadable sources, collisions in each
selected layer and at copy time, shared tools directories, and non-installation
of unrelated root tools. Both real generated variants verify helper bytes and
modes, exercise the installed merge helper, and run the installed review helper
in isolated temporary repositories. Each review-helper success asserts the
returned hash, sole parent, exact report-only diff and clean status; each refusal
asserts foreign dirt and report contents remain unchanged, the index is clean and
HEAD is unchanged. Review-helper invocations have all inherited `GIT_*` variables
removed. No helper source or template documents were changed.

## Checked inputs and results

SHA-256 identities:

- `newproject.py`: `6c141a6c2b8c47c5a667d912d62bfc575337d3f74345e99931b6a403271a55f6`
- `tests/test_newproject.py`: `d9f847e7fd2e2f7c8f3df1070caf2a36052a3c3777de4d95847bef3c5162f98d`
- `tools/merge.py`: `8e20c9c326379d651769c5d752617f6ea0d47125858af49201d1db02f82b9100`
- `tools/review_commit.py`: `05183f07eb02750ceed8015eae5bac6da808966a790e84fd666171b3088e9465`

Python 3.9.6, Git 2.54.0:

- `python3 -m unittest discover -s tests -v`: 53 tests passed (18.581s).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
  passed; eight files already formatted.
- `git diff --check` and `git diff --cached --check`: passed, including final
  staged implementation and this evidence record.

Initial focused lint identified loop-variable and subprocess annotations; these
were corrected before final checks. Independent implementation review is pending.
