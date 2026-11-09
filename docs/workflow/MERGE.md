# Merging a task branch

When a merge into `main` is needed, LEAD follows this procedure.

Confirm that required checks and review cover the source branch and its
integration with current `main`. Take exclusive writer ownership and record
both branch tips.

Prepare the final commit message following [MAIN-MESSAGE](MAIN-MESSAGE.md).

From the repository root in a clean worktree on `main`, run:

```sh
python3 tools/merge.py SOURCE -m "MESSAGE"
```

`SOURCE` is the exact local branch name. Preserve local files, including ignored
files, when preparing the worktree. Do not bypass a helper refusal with a manual merge.

On success, record the resulting commit and report the result after any checks
or review needed for inputs changed by integration or hooks. Keep the source
branch; pushing, deployment and branch deletion need separate authority.

On failure, inspect and report the Git state before continuing: a commit may
already exist. Do not blindly retry, reset, abort or bypass hooks. Corrections
follow the normal check and review process.
