# Review commit helper task

Baseline: e9c6ec2b41a07884891bea4f4aca6e1dd9fdbe7b.
HUMAN approved implementing the report commit helper discussed in chat.
Contract: docs/specs/review-commit.md in the specification commit containing this
record. Scope ends with independently accepted local integration; no push.

LEAD owns specification and README. REVIEWER (Astra/high) first reviews the
committed specification directly with LEAD and commits only
docs/worklog/083-review-commit-spec-review.md. DISPATCHER (Luna/low) then forwards
that exact approved specification to DEVELOPER (Terra/medium), who owns
tools/review_commit.py, tests/test_review_commit.py and
docs/worklog/084-review-commit-implementation.md. DEVELOPER runs all configured
README checks, records source identity/results, and commits implementation.
REVIEWER statically reviews that commit and evidence, committing only
docs/worklog/085-review-commit-review.md. Corrections return to their author.
Each report records initial HEAD and released ownership. Only one writer at a
time; no other files may change. LEAD integrates through tools/merge.py after
acceptance and verifies the resulting tree. Follow PROCESS and role guides.

Specification checkpoint checks on baseline code with this specification and
README usage addition: `python3 -m unittest discover -s tests -v` passed all
43 tests (14.643s); `.venv/bin/python -m ruff check tools newproject.py tests
template/heavy/scripts` passed; `.venv/bin/python -m ruff format --check tools
newproject.py tests template/heavy/scripts` passed (6 files); `git diff --check`
passed. LEAD ran these for the documentation checkpoint only.
