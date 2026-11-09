# Remove duplicated workflow rules

HUMAN approves the three proposed simplifications: state optional branches once,
consolidate unchanged-input check reuse, and keep heavy branch requirements plus
a common merge reference instead of repeating inherited rules. Baseline:
bfc4fbfa6e9fec8af83ef6117925ef827c391d8e. Branch: codex/simplify-workflow-rules.

Documentation short route: LEAD edits root/base PROJECT-RULES together and heavy
HEAVY, preserving requirements through the inherited PROCESS and MERGE rules.
Keep bootstrap and accepted-main boundaries. No edits to message guides, helper,
generator, role authorities or other heavy features. LEAD runs README checks
because templates change, records results here and commits. REVIEWER Astra/high
independently checks preservation and commits only 079-simplify-workflow-review.md
under docs/worklog. After acceptance LEAD merges through the helper, retains the
branch and does not push.

## Checks

On baseline plus the documented edits, LEAD ran:

- `python3 -m unittest discover -s tests -v`: 43 tests passed in 14.463s.
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`: passed, 6 files already formatted.
- `git diff --check`: passed; shared root/base Git sections match.

Tests ran in temporary repositories; code and test files are unchanged.
