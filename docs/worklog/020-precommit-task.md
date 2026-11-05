# Required checks before commits

LEAD documentation-route assignment. Baseline:
028beb003d1dc3f4958a7db8b4bd0c7244cf13d0.
User requests tests, lint and formatting checks before committing, in repository
rules and template wherever configured. User clarified the order explicitly:
changes, configured tests/lint/format checks, independent review, then commit. Preserve small, understandable process.

LEAD changed only root/template PROJECT-RULES and PROCESS to require configured
checks before every commit, including documentation, with passing results on
committed inputs, blockers for unavailable configured checks, no obligation to
install absent checks and no automatic addition of tooling. Preserve executable
check ownership and static-only independent review; LEAD may check docs-only work.
No runtime changes or new tests. Authoritative commands remain in README.

Frozen documents and assignment: /private/tmp/newproject-precommit-rules-v3.
REVIEWER gpt-6-astra/high: independently review the four documents against user
intent, consistency with role/scope rules and proportionality. Write only
021-precommit-review.md with exact identities, findings, verdict and next action.
No project execution. Return findings directly to LEAD. LEAD runs documented
checks for this docs-only task and commits only after acceptance and passing
checks. Commands/results are recorded below in this existing task file. No push or actual sibling project.

## Check evidence before revised review submission

LEAD executed the existing configured checks for this documentation-only task.
No Python or Ruff configuration inputs changed from baseline. Checked Git blobs:
- newproject.py: 293876835b8e6f4839572fa4f241d9dc32cac083
- tests/test_newproject.py: 2fbc1d7db75dfad615a84ba6838ed83f7f3e07d5
- ruff.toml: afdf11150e40e3acadd76f5859ecf8cb96ea41c5

Commands and outcomes (all exit 0):
- `python3 -m unittest discover -s tests -v`: 11 tests, 2.786s, OK.
- `/private/tmp/newproject-ruff-venv/bin/python -m ruff check newproject.py tests/test_newproject.py`: All checks passed!
- `/private/tmp/newproject-ruff-venv/bin/python -m ruff format --check newproject.py tests/test_newproject.py`: 2 files already formatted.

The first policy snapshot was sent for review in parallel with these checks.
The revised policy explicitly requires checks before review; this revised
submission occurs after the passing outcomes above. Only policy/task prose changed
subsequently, so checked executable inputs and results remain unchanged.
