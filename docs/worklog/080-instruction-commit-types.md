# Instruction commit types

HUMAN approves replacing the longer instruction/Markdown explanation with
“Agent instructions are part of the implementation” and broadening refactor
from code to code or instructions without behavior changes. Baseline:
d1a6f5d8be559146bc67cb049060c8698515d6ac. LEAD edits root/base MAIN-MESSAGE
identically, without additional examples or repeating type-selection guidance.
No other rules, code or templates change.

Documentation short route: LEAD runs README checks and commits; REVIEWER
Astra/high statically reviews and commits only 081-instruction-commit-types-review.md
under docs/worklog, then releases ownership. LEAD integrates accepted changes
through the helper, retaining the branch; no push.

Checks on this source before commit:
- `python3 -m unittest discover -s tests -q`: 43 passed in 14.375s (same README suite, quiet output).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`: passed, 6 files already formatted.
- `git diff --check`: passed. Root/base guide content matches.
