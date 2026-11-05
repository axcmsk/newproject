# Merge helper implementation evidence

Initial contract: `docs/specs/merge.md` and `docs/worklog/039-merge-task.md` at `29c1cdd`; accepted in `docs/worklog/040-merge-spec-review.md` at `ce541dd`. HUMAN changed the interface to a fixed `main` target during implementation. The uncommitted draft was preserved and restored byte-for-byte while LEAD amended the contract at `1c52fb2`; `docs/worklog/043-merge-main-spec-review.md` accepted it at `703ca8e`. Implementation resumed from that source with the preserved draft. Checked executable inputs are committed with this report.

The helper uses a top-level target constant, pins local tips, checks repository state and chooses squash or two-parent merge from source-exclusive subjects. It leaves failed operations for inspection and verifies the resulting branch, parents and cleanliness. Tests use isolated temporary Git repositories and cover both modes, merge-commit subjects, messages, source preservation, status refusal, ignored file collision, operation markers and linked worktrees, conflict, hook failure, no-net-change, routing environment isolation, Git configuration, help and unavailable Git.

Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed: 35 tests in 11.993s (`OK`).
- `.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).

An early focused run found an outdated test invocation after the fixed-target amendment; it was corrected. A later fixture mistakenly treated an untracked file as ignored before the ignore rule existed on the target; the fixture was corrected and all checks rerun. Submodule dirtiness and reuse of a populated rerere cache were not independently exercised; the command explicitly requests submodule status and disables rerere. Checks ran on this host only. No development branch was merged or pushed.
