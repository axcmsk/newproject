# Merging a task branch

LEAD follows this procedure only when HUMAN instructs it to merge the branch.
Completing work or reading this instruction does not authorize a merge.

Confirm that required checks and review cover the source branch and its
integration with current `main`; arrange missing checks through the usual roles.
Take exclusive writer ownership, record both branch tips and prepare the commit
message describing the result.

Work in a clean target worktree on `main`. Preserve local files when preparing
it, including ignored files. Use the reviewed helper from an absolute path that
remains available there, such as a separate checkout:

```sh
python3 /absolute/path/to/merge.py SOURCE -m "MESSAGE"
```

`SOURCE` is the exact local branch name. The helper checks Git preconditions;
LEAD remains responsible for authorization and acceptance.

On success, record the resulting commit. Arrange affected checks or review if
integration or hooks changed their inputs, then report the result. Keep the
source branch; pushing, deployment and branch deletion need separate authority.

On failure, inspect and report the remaining Git state before continuing: a
commit may already exist. Do not blindly retry, reset, abort or bypass hooks.
Hand corrections to the responsible role and release writer ownership;
corrections follow the normal check and review process.
