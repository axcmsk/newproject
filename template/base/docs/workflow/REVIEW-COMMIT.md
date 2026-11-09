# Committing a review report

After completing a review, REVIEWER commits only its assigned reports, for any
verdict. Keep the reviewed source commit in the report. Required checks must
already cover the reviewed inputs; this procedure does not run them.

Take exclusive writer ownership. Use the full HEAD recorded at review start and
the exact assigned report paths below `docs/worklog/`. All staged changes must
belong to those reports. Other working-tree changes require the explicit
operational-path permission below.

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

## Operational changes

LEAD lists the exact operational paths permitted to remain
dirty in the review assignment. They must be outside the pinned review inputs
and separate from report paths. REVIEWER checks the authorized scope, including
STATE block boundaries and journal rules where applicable, before committing.
The helper preserves files; it does not establish permission or interpret them.

Pass each authorized path with a separate `--allow-dirty PATH`, for example:

```sh
python3 tools/review_commit.py --head FULL_HASH -m "review: description" \
  --allow-dirty docs/workflow/STATE.md \
  --allow-dirty docs/workflow/work-log.jsonl \
  docs/worklog/NNN-review.md
```

Use actual assigned paths, not this example as an automatic allowlist. Only
existing regular tracked files are eligible; their index entries must equal
HEAD. Do not add unlisted files, untracked files, staged operational changes or
reviewed inputs to make a refusal disappear. The helper leaves allowed changes
unstaged and checks their contents and modes remain unchanged through the commit.
The index and reports must end clean; only the allowed operational changes remain.
Return ownership for separate operational closeout after the report commit.
