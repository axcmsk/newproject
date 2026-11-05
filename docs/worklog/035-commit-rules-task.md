# Commit messages and reviewer-owned reports

## Assignment

Baseline: 2243ed6d3424cd3a22d2ea76daa3be0c450059b1 on main, initially clean.
HUMAN approved applying the English commit rules to this repository and both
template variants. Types are step, fixup, docs, review and log; classification
is by content, with standalone documentation using step and accompanying docs
using docs. Choose/check the message before committing; do not rewrite existing
commits or block review for a wrong type. Preserve the current merge policy.

HUMAN explicitly authorizes REVIEWER to commit its own report after completing
review. This authorization applies to this task directly, independently of the
policy revision being reviewed. Keep exact source identity, exclusive writer
ownership, unchanged review-start HEAD and report-only staged contents. Preserve
static review: Git inspection/report commit is allowed, executable project checks
remain prohibited for REVIEWER. Existing valid checks need not be repeated merely
because the report was added.

Use the documentation short route. LEAD authors all changes and runs configured
checks. REVIEWER gpt-6-astra/high independently reviews the checked source and
records its verdict in docs/worklog/036-commit-rules-review.md. The reviewer owns
only that report and may commit it with review: after verifying the boundary,
then returns the source and report commit identities to LEAD. No other agent or
additional implementation is needed. Stop after local accepted commits; no push.

Allowed source changes: root and template/base copies of PROJECT-RULES.md,
PROCESS.md and roles/REVIEWER.md; template/heavy/docs/workflow/HEAVY.md and
work-log-format.md; this assignment/check record and separate review report.
No executable, generator, validation, dependency or historical-report changes.

## Acceptance

Common message/ownership rules have one home in PROJECT-RULES for each variant;
reviewer-specific commit boundaries live in its role guide. PROCESS routes both
specification and implementation report commits without treating the expected
HEAD advance as source drift or a failed verdict as acceptance. Heavy explicitly
reconciles preauthorized operational writes with report-only staging/commit and
keeps operational data outside the reviewer verdict. Base/root shared policy
matches. No new automation or merge-selection policy is introduced.

## Checks

LEAD ran these commands on the prepared source before its checkpoint commit:
- python3 -m unittest discover -s tests -v: PASS, 26 tests, 5.326s.
- .venv/bin/python -m ruff check newproject.py tests template/heavy/scripts:
  PASS, All checks passed.
- .venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts:
  PASS, 4 files already formatted.
- git diff --check: PASS.

The checked source is the commit containing this record. No tested inputs changed
between checks and that commit; adding this record does not change them. Tests
include generated normal/heavy projects in temporary fixtures. No new tests were
added for this documentation-only change. LEAD inspected the diff and current
commit-related instructions; independent consistency review remains required.
