# Allowed operational changes: implementation

Baseline `609d0c7c0076b21405a34574cd5d9f1e6ed31b2d` on
`codex/review-commit-allowed-dirty`. Behavioral contract:
`docs/specs/review-commit.md` at `280fcca540825e1a21798086d728088944e6ecad`,
accepted in 091 at `a5682ab79ff227e8b3fbcfbbd6839cf120ead804`; assignment 096.
LEAD released the five activation documents for unchanged staging and commit.

The repeatable option validates literal tracked operational paths against HEAD
and the index. The helper snapshots file bytes, permission bits and index entries,
checks them before staging, before commit and after commit, and permits only
unstaged modifications on listed paths. Reports alone are staged. Existing global
index-flag and strict-mode checks remain in place. No automatic repair occurs.

Temporary-repository tests cover multiple, duplicate and literal paths, ignored
tracked files, clean and modified files including mode changes, commit parent and
report-only diff, snapshots and dirty status. Refusal tests cover overlap, invalid,
untracked and unsafe paths, staged and partly staged content, modes and types,
deletions, renames, conflicts, hidden flags, unlisted dirt and operational-only
changes. Hooks changing content, mode or staging and a clean filter changing an
operational file are detected without repair. Both generated variants exercise
strict refusal and successful installed-helper operation with allowed dirt. Tests
remain bounded by exclusive ownership; they do not establish concurrent-writer
or hostile-hook protection.

## Checked identities and results

SHA-256 of checked implementation inputs:

- `tools/review_commit.py`: `f14b689df332e8813e621ae3d774af523d472c6fab77858a2c8ca62153b2accc`
- `tests/test_review_commit.py`: `8e775380afce21c343d624772984c6faca13d8a519f9e49fa85d62632015a4e5`
- `tests/test_newproject.py`: `80753453f570534467464e8a296f622d31ec420aa9c3650cc4d6d96c268afdd5`

Released document SHA-256 values in order: spec `84ae737615f343fffe2ba5b98124faf1a178e9a39c56d56be1fcd0dc31bc671c`;
root and base REVIEW-COMMIT both `008e315bba3c60adeeb5b66b17967a4f8b40dc00ad0a9558aea968fe5aaa878c`;
HEAVY `f416444ee54af6fad6caa90eaff0f2ef628ac8a53d1ce884954d246c1c8079cf`;
assignment 096 `fbbb0f97ffb60c149e8fcd627ec8eef3a7684a48eeb47742c5a9ebe071043fc9`.

Python 3.9.6; Git 2.54.0:

- `python3 -m unittest discover -s tests -v`: 59 tests passed (25.181s).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
  passed; eight files already formatted.
- `git diff --check` and final `git diff --cached --check`: passed.

Initial focused lint identified complexity and an annotation placement; these
were corrected before the final checks. No executable check failure remained.
Independent review is pending; this record does not grant acceptance.
