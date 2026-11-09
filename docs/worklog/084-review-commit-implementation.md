# Review report commit helper implementation

Implemented the contract in `docs/specs/review-commit.md` at
`f214677c7bac64ade6621767cc6712e1ccaaa8b9`, accepted by
`docs/worklog/083-review-commit-spec-review.md` at
`f4e42bacecc2ac2897a3ee64982165b65885c438`. The starting HEAD was the latter
commit, on `codex/review-commit-helper`, with a clean working tree.

The helper validates repository state and exact report paths, stages complete
report contents, and checks the resulting commit and final state. Failures leave
state for inspection. Tests use temporary repositories and cover successful
staged, modified and new reports, literal names, refusals, hooks and preservation.
The helper relies on the specified exclusive writer ownership assumption.

## Checks

Checked implementation inputs, SHA-256:

- `tools/review_commit.py`: `7a885a59f1df0bc4194eb64002b374419207318d5f087b58d961fb68611d7904`
- `tests/test_review_commit.py`: `e6130354c8c12a665fb00a26eb415599c6d449a819aa402553b67bd928fdf2e3`

On Python 3.9.6 and Git 2.54.0:

- `python3 -m unittest discover -s tests -v`: 49 tests passed.
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`:
  passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
  passed; eight files already formatted.
- `git diff --check`: passed before this report was added.

An initial test run failed because `git check-ignore` does not accept the
literal pathspec environment setting; the helper now passes its already literal
filename directly. The subsequent full run passed. Initial lint findings were
corrected before final checks. No independent implementation review is claimed.

## Corrections after review 085

Starting from report commit `783c95ea57b4127d9932a5d5cfc667bef6c55ba0`,
the helper now refuses index entries marked assume-unchanged or skip-worktree
before staging and during final verification, without clearing flags. Regression
tests preserve and compare the index, HEAD and affected files for hidden foreign
changes, tracked foreign modifications, rename source deletion, conflicts and
index/worktree type changes. A post-commit hook test verifies that a hidden
tracked change cannot yield success and that the flag and file remain intact.

Corrected checked implementation inputs, SHA-256:

- `tools/review_commit.py`: `05183f07eb02750ceed8015eae5bac6da808966a790e84fd666171b3088e9465`
- `tests/test_review_commit.py`: `802e9803ea78d2a4082b5cf8b73faedf330171f3cd0a9d3eb61ae1285f5aa2e6`

On Python 3.9.6 and Git 2.54.0:

- `python3 -m unittest discover -s tests -v`: 53 tests passed.
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
  passed; eight files already formatted.
- `git diff --check`: passed on corrected source before this evidence update;
  the staged diff check below covers this report as well.

These are developer results; the correction awaits independent review.
