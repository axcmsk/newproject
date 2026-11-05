# Simplify commit instructions

HUMAN requested simpler wording after the accepted commit-rule update.
Baseline: aa97f25b29950c03966a01d6fd4dca59cd2d6458 on main.
Use the documentation short route: LEAD edits; REVIEWER gpt-6-astra/high checks
and commits only docs/worklog/038-commit-rules-review.md using review:.

Scope: root/base PROJECT-RULES, PROCESS, REVIEWER; heavy HEAVY. Remove repeated
explanations while retaining the five types, content-based choice, standalone
documentation distinction, no retrospective prefix rewrite/blocker, writer
boundaries, reviewer-owned report-only commits, source identity, valid-check reuse
and the heavy operational allowance. No executable or merge-policy changes.
Review the exact commit containing this record against the baseline. Verify
root/base alignment and preservation of authority and safety conditions.
Stop after accepted local commits; no push.

LEAD checks on the prepared source: python3 -m unittest discover -s tests -v
passed (26 tests); .venv/bin/python -m ruff check newproject.py tests
template/heavy/scripts passed; .venv/bin/python -m ruff format --check
newproject.py tests template/heavy/scripts passed (4 files unchanged).
Git diff --check passed. This record adds no tested-input changes.
