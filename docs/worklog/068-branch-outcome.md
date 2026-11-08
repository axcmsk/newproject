# One primary outcome per branch

HUMAN approves one primary outcome per task branch, allowing supporting docs
and tests, and test: for test changes without product behavior changes. Baseline:
4c5b1ce6f64c9448e84f4484d88cec2b8bbe270a. LEAD edits only root roles/LEAD.md,
MERGE-MESSAGE.md and this brief. Do not mandate branches, preselect their types,
or change internal commit prefixes, helper behavior, templates or generator.

Documentation short route: REVIEWER Astra/high statically reviews and commits
only docs/worklog/069-branch-outcome-review.md, then releases ownership.
Existing 40-test and README Ruff results in 055 remain valid: code, tests,
configuration and template inputs are unchanged. LEAD inspected the diff and
ran git diff --check successfully. No merge or push is part of this task.
