# Merging a task branch

When a merge into `main` is needed, LEAD follows this procedure.

Confirm that required checks and review cover the source branch and its
integration with current `main`; arrange missing checks through the usual roles.
Take exclusive writer ownership and record both branch tips.

Prepare the commit message describing the result using
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
`feat:`, `fix:`, `docs:`, `refactor:` or `chore:` as appropriate. Scope is optional,
for example `fix(merge): preserve ignored files`. Mark breaking changes with `!`
before the colon or a `BREAKING CHANGE:` footer, and describe the incompatibility.
This applies to the final commit in either merge mode. LEAD supplies the message;
the helper neither selects nor validates its type.

Work from the repository root in a clean worktree on `main`. Preserve local
files when preparing it, including ignored files. Run:

```sh
python3 tools/merge.py SOURCE -m "MESSAGE"
```

`SOURCE` is the exact local branch name. The helper checks Git preconditions;
LEAD remains responsible for authorization and acceptance. Use the helper's
chosen merge mode; do not reproduce its selection rules or bypass a refusal
with a manual merge.

On success, record the resulting commit. Arrange affected checks or review if
integration or hooks changed their inputs, then report the result. Keep the
source branch; pushing, deployment and branch deletion need separate authority.

On failure, inspect and report the remaining Git state before continuing: a
commit may already exist. Do not blindly retry, reset, abort or bypass hooks.
Hand corrections to the responsible role and release writer ownership;
corrections follow the normal check and review process.
