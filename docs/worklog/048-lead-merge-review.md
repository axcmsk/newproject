# LEAD merge procedure review

- Verdict: `ACCEPTED` as an unadopted draft procedure.
- Reviewed source and review-start HEAD:
  `f579eba2501f75f71400611fb19cb5fd3a332f89`.
- Baseline: `215af5b07b79290d6ff895a089f0fbc136d72802`.
- Assignment: `docs/worklog/047-lead-merge-instruction.md` at source.
- Scope: new `docs/workflow/MERGE.md` against the accepted helper and current
  authority/check ownership; no active-policy adoption or merge authorization.
- Findings and conditions: none.
- Next owner/action: LEAD returns the draft for HUMAN inspection; keep the
  current branch unmerged and do not push.

The command matches the fixed-main helper interface. The procedure keeps caller
authorization, source readiness, current-main evidence and exclusive ownership
explicit, without duplicating mode-selection logic or requiring Conventional
Commits. The separate-checkout absolute path remains usable when the target
worktree checks out main, even while merge.py exists only in the feature branch.

The guarded checkout option preserves ignored collisions as documented in the
[Git checkout manual](https://git-scm.com/docs/git-checkout). Refusals do not grant
permission to force, stash or discard work. Error handling correctly allows for
staged content, conflicts or an already-created commit, prohibits blind recovery,
and routes corrections/checks to the responsible roles. Integration/hook changes
require affected validation before claiming the result is validated. The explicit
hold on merging this draft remains in force.

Executable inputs and templates are unchanged; the supplied prior 40-test and
Ruff results remain applicable. This review was static only, with no checks or
source edits. Review began at the exact source with a clean tree. Only this report
may be committed after HEAD/index/path verification; return its actual commit hash
separately and release ownership. Acceptance of the document does not adopt it.
