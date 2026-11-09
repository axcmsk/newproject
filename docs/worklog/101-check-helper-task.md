# One sequential check command

Baseline 1be232c2bfd84912688c9f9491168873e73d87b1, branch codex/check-helper.
HUMAN requests one command for tests, lint and formatting checks and then asks
to omit parallelism. LEAD chooses sequential lint, format check, tests with all
three attempted and an overall failing exit status if any fail.

Contract: docs/specs/check.md in this checkpoint. LEAD owns this record, contract,
README.md and docs/workflow/PROJECT-RULES.md. The first documentation checkpoint
contains the contract and routing only; README/check reference adoption follows
implementation, in this same branch. No template or generator changes.

LEAD runs configured documentation-stage checks, commits and sends the exact
contract directly to REVIEWER Astra/high. Reviewer owns only
docs/worklog/102-check-helper-spec-review.md; static review and report commit
using accepted review_commit.py. After acceptance, DISPATCHER Luna/low releases
the pinned specification to DEVELOPER Terra/medium. Developer owns
tools/check.py, tests/test_check.py and docs/worklog/103-check-helper-implementation.md.
Implement and test the accepted contract; retain command/version/source identities
and all check results. Before final checks, return writer ownership to LEAD for
README/project-specific check references. LEAD releases exact documents back to
DEVELOPER for testing and committing unchanged with the implementation.

REVIEWER then statically reviews the exact committed source and evidence; only
writes docs/worklog/104-check-helper-review.md. Corrections return to their
author; requirement questions go directly to LEAD. Keep pinned inputs fixed and
one writer at a time. Verify report-only commits and release ownership. Per
HUMAN's latest instruction, leave completed work in codex/check-helper: no merge
into main and no push.

Documentation checkpoint evidence on unchanged baseline code/templates:
`python3 -m unittest discover -s tests -v`: 59 passed (28.701s);
`.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`:
passed; `.venv/bin/python -m ruff format --check tools newproject.py tests
template/heavy/scripts`: passed (8 files); `git diff --check`: passed.
Final staged diff check runs in the sequential checkpoint commit command and
its outcome is supplied to REVIEWER with the exact commit ID.
