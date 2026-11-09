# Simplify check guidance

HUMAN asks to shorten the template rule to using the Python helper and not
inventing missing checks. Baseline 7de37f5b41172ec2f6aeeb5109908e89e3ed84cd on
codex/check-helper. No merge/push.

Documentation short route: LEAD owns root/base PROJECT-RULES and this record.
Replace detailed interface/ordering guidance with a short Python-helper rule,
conditional on its availability because generator installation remains unchanged.
Keep configured-check-only and README usage guidance. Preserve the accepted
no-redundant-format-check allowance in the existing check-before-commit paragraph.
Required full checks, unavailable configured checks as blockers, and role
boundaries remain below. Helper/spec/README behavior and generator are unchanged.

LEAD runs configured checks, commits; REVIEWER Astra/high statically reviews the
exact checkpoint and evidence, writing only
docs/worklog/120-simplify-check-guidance-review.md. Use accepted helper for the
report, verify report-only child and release ownership. No delegated developer
needed. Preserve historical reports and leave work in the current branch.

LEAD ran `python3 tools/python_check.py` on baseline executable sources with
updated templates: overall 0, format check 0 (10 files), lint 0, tests 0
(69 passed, 28.426s). `git diff --check` passed. Shared edits are identical in
root/base. Final staged diff check is run before commit and reported with hash.

Latest HUMAN refinements: keep a brief --reformat mention and remove README
documentation guidance from this language-specific rule. LEAD applies both;
general documentation instructions remain elsewhere. REVIEWER released ownership
without committing draft120; it remains excluded from the source checkpoint and
will be updated for the corrected source. No code or authority changes.

Corrected-template verification: `python3 tools/python_check.py` overall 0;
format check 0 (10 files), lint 0, tests 0 (69 passed, 26.654s).
`git diff --check` passed. The final staged diff check excludes reviewer draft120.
