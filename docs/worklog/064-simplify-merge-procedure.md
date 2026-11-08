# Simplify the merge procedure

HUMAN requests another simplification pass. Baseline:
56be75d4fd4ae027b9beedd707f73e9d40a679b9. Documentation short route: LEAD edits
only MERGE.md and this brief. Remove repetition of general responsibilities and
handoff rules, shorten message guidance, retain checks/review, writer ownership,
branch tips, concrete CLI, local-file preservation, no manual bypass, success
validation, separate publication authority and partial-state failure handling.
No change to the helper, templates, generation or other workflow rules.

REVIEWER Astra/high statically reviews and commits only
065-simplify-merge-procedure-review.md under docs/worklog, then releases ownership.
The 40 passing tests and README Ruff results in 055 remain valid with executable,
test, template and configuration inputs unchanged. LEAD inspected the diff and
ran git diff --check successfully. No merge or push is part of this task.
