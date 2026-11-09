# Committing a review report

After completing a review, REVIEWER commits only its assigned reports, for any
verdict. Keep the reviewed source commit in the report. Required checks must
already cover the reviewed inputs; this procedure does not run them.

Take exclusive writer ownership. Use the full HEAD recorded at review start and
the exact assigned report paths below `docs/worklog/`. All changes in the index
and working tree must belong to those reports.

From the repository root, run:

```sh
python3 tools/review_commit.py --head FULL_HASH -m "review: description" docs/worklog/NNN-review.md
```

Pass additional assigned report paths as separate arguments. The helper stages
their complete contents and commits with normal Git hooks. It checks the pinned
HEAD, change scope and resulting commit; it does not judge review acceptance.

On success, return the report commit separately from the reviewed source commit
and release writer ownership. On failure, inspect and report the Git state before
continuing: staging or a commit may already have occurred. Do not blindly retry,
discard changes or bypass a refusal with a manual commit.
