# Broaden useful lint coverage

LEAD assignment. Baseline: 6b5fd6d7fbb40acf0f89d245bdd8f7cfd2d6968e.
Short route for behavior-preserving mechanical improvements and local tooling.
User asks to add remaining useful checks while the script is small, and asks
which are excessive. Preserve simplicity, readable autoformat and CLI behavior.

LEAD selects stable Ruff groups E, W, F, I, N, B, UP, S and C90, targeting
Python 3.9. Keep Ruff 0.17.3 and default formatter. Do not enable ALL/preview,
mandatory docstrings (D), mandatory annotations (ANN), TODO policies or print bans.
Use complexity limit 10. Do not refactor for style beyond what improves clarity
or is necessary for accepted checks. No features/runtime dependencies/templates.

DEVELOPER owns newproject.py, tests/test_newproject.py, ruff.toml configuration
and explanatory comments, and docs/worklog/018-lint-implementation.md. Required
sources: baseline code/tests/config, docs/specs/newproject.md and current rules.
Fix findings without changing behavior or weakening assertions. Narrow inline
suppressions with rationale are permitted for legitimate subprocess use (argument
lists, no shell; Git on PATH is intended) and controlled test fixtures. Report any
other proposed exclusions to LEAD before adopting them. Avoid broad security
suppression. Formatter-incompatible style rules may be excluded with explanation;
line length E501 may be excluded because formatter owns wrapping and deliberately
leaves some lines long. Do not claim comprehensive PEP 8 or security coverage.

First report findings and proposed changes/exclusions to LEAD, then implement
routine authorized fixes. Freeze final source/config and any LEAD README update
before decisive checks. Run full unittest suite, Ruff check, Ruff format --check,
and diff whitespace check. Record exact commands, versions, hashes, outcomes and
raw output. Compare baseline behavior/callers/error paths; add tests only for real
uncovered risks, not to mirror helper extraction. Report any behavioral change to
LEAD before proceeding; it requires standard requirements review.

DISPATCHER gpt-6-luna / low forwards exact frozen assignment from
/private/tmp/newproject-lint-assignment/017-lint-task.md to DEVELOPER
(gpt-6.1-terra / medium), then REVIEWER (gpt-6-astra / high).
Reviewer independently reviews exact config scope, comments/suppressions, code,
tests, preservation evidence and LEAD docs; no executable checks. Write
019-lint-review.md. Route ordinary fixes, preserve snapshots/review rounds and
return accepted result to LEAD. No worker commits, push or real sibling projects.
LEAD handles substantive documentation and authorized final local commit.
