# Simplify the LEAD merge instruction

HUMAN requests a final instruction, not a draft, activated only by a command to
merge. Baseline: 541aca46ce727bd6b06cf44739273b43939bea53, codex/merge-script.
LEAD edits only docs/workflow/MERGE.md and this combined brief/check record.
Keep the procedure concise, with no conditional checkout recipe or internal
mode-selection algorithm. Preserve acceptance, helper availability, local files,
check ownership and failure handling. No merge to main, push, script change or
template installation is authorized. The prior hold on main remains in force.

Inputs: baseline MERGE.md, merge.py, root PROJECT-RULES and PROCESS. This request
supersedes the draft/adoption wording of task047 only. Use the documentation
short route: LEAD writes and commits; REVIEWER (Astra/high) independently reviews
and commits only docs/worklog/050-lead-merge-review.md, then returns to LEAD.

The 40-test and expanded Ruff results in 041, accepted through 046, remain valid:
no executable, test, configuration or template inputs changed. LEAD checked CLI
consistency and git diff --check. Reviewer performs static review only.
