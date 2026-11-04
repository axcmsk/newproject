# Script implementation assignment

Baseline: ae40b4c2641e0c8ed4ed9b55872f81ab19166303.
Requirements: docs/specs/newproject.md (frozen together with this assignment
in /private/tmp/newproject-script-spec-v1). User approved the proposed CLI,
sibling placement, template-only copy, empty/existing-Git handling, refusals,
main branch, no initial commit, and requested extensive tests.

LEAD owns specifications and substantive documentation. REVIEWER first reviews
this specification directly to LEAD; implementation starts only on acceptance.
DISPATCHER then delegates to DEVELOPER (gpt-6.1-terra / medium), followed by
REVIEWER (gpt-6-astra / high). Dispatcher uses gpt-6-luna / low.

DEVELOPER may write newproject.py, tests/, .gitignore and implementation evidence
in docs/worklog/008-script-implementation.md. No template modifications. Propose
README/setup instructions to LEAD rather than changing substantive requirements.
Developer owns all executable tests and ordinary fixes. Freeze reviewed code
and tests in a saved snapshot with hashes before decisive checks. Preserve every
reviewed revision and evidence. Reviewer writes docs/worklog/009-script-review.md;
append rounds or use subsequent uniquely reserved numbers if needed. Specification
review goes in docs/worklog/007-script-spec-review.md.

Acceptance: implement the specification, complete meaningful full-suite checks,
resolve independent review findings, and supply exact source identity and evidence.
No external effects beyond temporary test fixtures. LEAD updates README and root
project configuration for the approved implementation, obtains static review,
and commits accepted changes locally. No push or actual new sibling project.
