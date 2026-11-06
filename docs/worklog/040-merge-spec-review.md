# Draft merge helper specification review

- Verdict: `ACCEPTED` for the specification.
- Reviewed source and review-start HEAD:
  `29c1cdd125e11ccdfdf3a205a8ed349015ed10fa`.
- Baseline: `99c70534b3344c94e1d012f0a0f8ea02c1a32bd0`.
- Contract: `docs/worklog/039-merge-task.md` and `docs/specs/merge.md` at source.
- Scope: requirements, mechanical safety boundaries, implementation scope and
  verification plan. No implementation or real merge is accepted by this review.
- Findings and conditions: none.
- Next owner/action: LEAD may release this exact specification to DISPATCHER;
  implementation must pass its expanded checks and independent review.

The mode rule is deterministic over the pinned source-exclusive range, including
merge commits: known prefixes and at most one step select squash; all other
nonempty ranges select a real two-parent merge. It introduces no inferred commit
relationships or caller-approval machinery. The explicit interface, checked-out
target requirement and existing local branches keep operation and ownership clear.

The contract covers tracked/index/untracked cleanliness, submodule dirtiness,
unfinished-operation state in linked worktrees, ignored-file collisions, routing
environment isolation, pin rechecks and post-operation topology/status checks.
It preserves ordinary hooks/configuration within the stated non-hostile boundary,
while requiring explicit merge controls. Conflicts and failed commits remain for
caller inspection, with no automatic retry, abort, cleanup or mode fallback.
Empty ranges and no-net-change squash behavior are explicit.

The requested sequencing is consistent with the
[Git merge manual](https://git-scm.com/docs/git-merge): no-commit alone cannot
prevent fast-forward updates, no-ff prevents that advance, squash prepares a
single-parent result, and no-overwrite-ignore guards ignored collisions.
The [Git commit manual](https://git-scm.com/docs/git-commit) documents verbatim
cleanup for preserving the supplied message. These are documentation checks,
not evidence that the future implementation satisfies the contract.

The real-Git temporary-fixture plan covers both modes, topology/content/message,
clean and refused cases, ignored data, conflicts, hook failure, linked-worktree
state, config/environment interactions and preservation of existing regressions.
No template installation, active merge-policy change or framework is required.
Caller-owned authorization/tests/review and the later LEAD evaluation boundary
remain explicit.

Prior passing 26-test and Ruff results apply only to unchanged existing code;
expanded checks remain required after implementation. REVIEWER ran no executable
project checks or test merges. Review began at the exact source with a clean tree.
Only this report is authorized for the review commit; verify HEAD/index/report
boundaries before committing and return its actual hash separately. Writer
ownership is released after that handoff; no branch merge or push is authorized.
