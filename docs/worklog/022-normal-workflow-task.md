# Normal workflow update

## Assignment and authority

HUMAN requested two project variants, normal and later heavy, and authorized
updating normal now. Normal adds shared writer/runtime ownership, compact pinned
assignments, reviewer write boundaries, uncertain-session recovery, proportionate
check evidence and affected-check reruns. Preserve existing role routing and
conditional acceptance. Exclude STATE, shared journals, budgets, heavy fixture
lifecycle and DiBBS-specific policy. HUMAN explicitly selected Git commits before
review and after corrections, with review reports committed separately; feature
branches remain optional. This supersedes the former commit-after-review order
for this task; other authority changes require review before reliance.

Baseline:  see the parent of the source commit containing this assignment.
Allowed changes: README.md and root/template copies of PROCESS.md and
PROJECT-RULES.md; this assignment and separate review reports.
LEAD authors documentation and runs configured documentation checks. REVIEWER
(gpt-6-astra/high) independently reviews exact source, consistency and scope;
may write only docs/worklog/023-normal-workflow-review.md and must not commit.
Return findings and verdict to LEAD. No developer or dispatcher is needed for
this documentation-only short route. Stop after accepted local commits; no push.

## Acceptance

Both workflow copies agree, Git recovery points and review identities are
explicit, reviewer edits cannot silently enter acceptance, no heavy extension
is introduced, and configured checks pass. No generator behavior changes.

## Check evidence

On the prepared source, before its checkpoint commit:
- python3 -m unittest discover -s tests -v: PASS, 11 tests.
- .venv/bin/python -m ruff check newproject.py tests/test_newproject.py: PASS.
- .venv/bin/python -m ruff format --check newproject.py tests/test_newproject.py:
  PASS, 2 files unchanged.
- git diff --check: PASS.

Ruff 0.17.3 was installed in the repository's ignored .venv, as documented.
Adding this assignment/report does not change configured check inputs.
