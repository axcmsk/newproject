# Draft LEAD merge procedure

HUMAN requests an instruction for LEAD after the branch-local merge prototype.
Baseline 215af5b07b79290d6ff895a089f0fbc136d72802; branch codex/merge-script.
Keep the prior explicit hold on merging to main. Deliver only the short English
procedure docs/workflow/MERGE.md; do not install code in templates, change active
role/merge rules, add mode-selection logic to agent instructions, or require
Conventional Commits. The helper's current CLI and behavior are authoritative.
Sources: merge.py, docs/specs/merge.md, current root role/process/project rules,
and the accepted source/evidence/review chain through report046 at baseline.

Documentation short route: LEAD authors this procedure; REVIEWER gpt-6-astra/high
independently checks scope, usability, authorization, current-HEAD/check validity,
helper availability across checkout, and safe error handling. Sole review path:
docs/worklog/048-lead-merge-review.md. Reviewer self-commits review: after verifying
HEAD/report boundary and returns the commit to LEAD. No executable checks by
reviewer. No merge, push or active-policy adoption is authorized by this task.

Prior developer checks on unchanged executable inputs passed 40 tests, expanded
Ruff lint and formatting, recorded in 041 and independently assessed through 046.
This task changes only new draft/brief text outside generated templates and check
inputs; those results remain valid. LEAD checks links/CLI consistency and diff
whitespace before committing. No additional test suite is needed for this draft.
