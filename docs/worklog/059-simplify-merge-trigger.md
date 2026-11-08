# Simplify the merge trigger

HUMAN asks to simplify the approved rule to “when a merge is needed”. Baseline:
560eab11bcdc46c378bcb5a7172968b177529b2c. LEAD edits root MERGE, LEAD, PROCESS
and PROJECT-RULES only, plus this brief. Retain the removal of separate merge
approval; express when to use the procedure without requiring every completed
branch to be merged. Explicit HUMAN holds remain in MERGE, along with existing
checks, review, helper use and recovery. No code, templates, push or actual merge.

Documentation short route: REVIEWER Astra/high statically reviews and commits
only docs/worklog/060-simplify-merge-review.md, then returns ownership to LEAD.
The passing 40 tests and README Ruff checks in 055 remain valid with all their
inputs unchanged. LEAD inspected the diff and ran git diff --check successfully.
