# Final LEAD merge instruction review

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `038a3fe16f6b9a625cea3e7117c1f51b641639df`.
- Baseline: `541aca46ce727bd6b06cf44739273b43939bea53`.
- Assignment: `docs/worklog/049-lead-merge-instruction.md` at source.
- Scope: revised `docs/workflow/MERGE.md`; no script change or actual merge.
- Findings and conditions: none.
- Next owner/action: LEAD reports the completed instruction and preserves the
  existing hold on merging to main until HUMAN commands the merge.

The final instruction clearly requires HUMAN's merge command; neither completion
nor reading it creates authorization. Its command matches the fixed-main helper.
The shorter procedure retains source/current-main acceptance, exclusive ownership,
recorded tips, local-file preservation including ignored files, and a reviewed
helper path available from the target worktree. It removes the checkout recipe
and mode-selection detail without introducing alternative merge behavior.

Checks and corrections remain with the usual responsible roles. Post-integration
or hook changes require affected validation, failure may already include a commit,
and blind retry/reset/abort or hook bypass remains forbidden. Source preservation
and separate authority for push, deployment and deletion are explicit.

Executable inputs, templates and governing role/check rules are unchanged; the
supplied prior 40-test/Ruff results remain applicable. This review was static only.
Review began at the exact source with a clean tree. Only this report may be
committed after HEAD/index/path verification; return its actual hash separately
and release writer ownership. No merge or push is authorized by this verdict.
