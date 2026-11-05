# Merge helper implementation evidence

Initial contract: `docs/specs/merge.md` and `docs/worklog/039-merge-task.md` at `29c1cdd`; accepted in `docs/worklog/040-merge-spec-review.md` at `ce541dd`. HUMAN changed the interface to a fixed `main` target during implementation. The uncommitted draft was preserved and restored byte-for-byte while LEAD amended the contract at `1c52fb2`; `docs/worklog/043-merge-main-spec-review.md` accepted it at `703ca8e`. Implementation resumed from that source with the preserved draft. Checked executable inputs are committed with this report.

The helper uses a top-level target constant, pins local tips, checks repository state and chooses squash or two-parent merge from source-exclusive subjects. It leaves failed operations for inspection and verifies the resulting branch, parents and cleanliness. Tests use isolated temporary Git repositories and cover both modes, merge-commit subjects, messages, source preservation, status refusal, ignored file collision, operation markers and linked worktrees, conflict, hook failure, no-net-change, routing environment isolation, Git configuration, help and unavailable Git.

Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed: 35 tests in 11.993s (`OK`).
- `.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).

An early focused run found an outdated test invocation after the fixed-target amendment; it was corrected. A later fixture mistakenly treated an untracked file as ignored before the ignore rule existed on the target; the fixture was corrected and all checks rerun. Submodule dirtiness and reuse of a populated rerere cache were not independently exercised; the command explicitly requests submodule status and disables rerere. Checks ran on this host only. No development branch was merged or pushed.

## Review corrections and policy amendment

Implementation review `docs/worklog/042-merge-review.md` at `bc3327e27512c9b59fb3522b1092449e6f42e912` requested changes to `cdd81879e575a3026cd360c386935df332a4db96`. The amended contract at `07c6ec1` and acceptance `docs/worklog/044-merge-git-policy-review.md` at `836abe0` supersede the prior hook/rerere policy. Work in progress was preserved while the amendment was reviewed and restored before these corrections.

- R1: operation-scoped `merge.ff=true` prevents inherited ff-only from blocking a diverged squash. A real-Git regression checks the one-parent commit, message, content, source and unchanged persistent configuration. The preliminary `merge.ff=false` approach failed because Git forbids no-ff with squash; it was corrected before the final checks.
- R2: diff status 0, 1 and error are distinguished. Injected status 2 preserves staged content, reports the command/error and leaves HEAD unchanged without committing.
- R3: HUMAN's revised contract explicitly permits successful hooks to modify message and content. Real successful commit-msg and pre-commit hooks prove both modifications are committed and accepted; no pre-hook comparison remains.
- R4: a dirty local submodule is refused without changes. A populated rerere cache is honored, including an applied and staged resolution; Git's nonzero merge result stops the helper without a commit or retry, leaving state for inspection. This replaces the previous reported evidence limitation.

Final correction checks, on the code and tests committed with this report (Python 3.9.6, Git 2.54.0, Ruff 0.17.3):

- `python3 -m unittest discover -s tests -v` — passed, 40 tests in 17.019s (`OK`).
- `.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).

Tests ran locally using temporary repositories only. No branch was merged or pushed; independent affected review remains required.

## R5 test isolation correction

Review `docs/worklog/045-merge-review.md` at `452cf786728fafc195cf6b195a58dbc5fc316416` closed or superseded R1–R4 and requested a fixture-only correction. The diff-error test now saves the actual current directory before changing it, restores it in `finally`, and runs the in-process helper under the isolated fixture environment. Its injected error, no-commit and staged-content assertions remain intact. Product code is unchanged.

- `python3 -m unittest discover -s tests -p test_merge.py -k diff_error -v` — passed, 1 test in 0.312s.
- `python3 -m unittest discover -s tests -v` — passed, 40 tests in 15.855s.
- `.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts` — passed.
- `.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts` — passed, 6 files already formatted.

The checked test and this evidence are committed together; independent affected review remains required.
