# Merging a task branch — LEAD draft

Proposed procedure for the reviewed merge helper. It is not yet adopted by this
repository or its templates and grants no permission to merge the current draft.
Use it only after explicit adoption or authorization of the helper for the merge;
existing scoped HUMAN authorization does not need repeated confirmation.

## Before merging

LEAD confirms the source branch is ready: required checks passed, review findings
are closed, and later commits contain only permitted reports or other accepted
changes. Check that the evidence still applies to the intended source and current
main. Arrange any missing checks or review through the usual roles.

Record the source and main tips, take exclusive writer ownership, and prepare a
nonempty commit message describing the result. Use the reviewed helper revision
from an absolute path that will remain available with main checked out. For this
draft, keep the helper in a separate checkout; do not rely on a file that exists
only in the branch being merged.

Use a clean target worktree with main already checked out. If switching is needed,
use `git checkout --no-overwrite-ignore main`; do not force the switch, stash work
or discard local files to get past a refusal. The helper performs the mechanical
Git precondition checks. LEAD remains responsible for authorization, acceptance
and check evidence; invoking it does not grant authority to run product checks.

## Run and report

From the target repository, invoke the reviewed helper with the exact local
source branch and the prepared message:

```sh
python3 /absolute/path/to/merge.py SOURCE -m "MESSAGE"
```

On success, record the resulting commit and report completion. If integration or
hooks changed inputs covered by existing checks/review, arrange the affected
checks/review before claiming the result is validated. Keep the source branch;
push, deployment and branch deletion require separate authorization.

On failure, stop and inspect the reported Git state. Do not blindly rerun, reset,
abort or bypass hooks. A failure may leave staged content, unresolved conflicts
or an already-created commit. Hand any needed correction to the responsible role
and apply the normal check/review process before continuing. Release writer
ownership when handing off, and report the exact remaining state and next action.
