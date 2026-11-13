# Integrate Python and Go coverage with Python JSON

Baseline main: `4ab7fe19f5f0ba1102750a57699d18a599d8df23`.
HUMAN requests both completed coverage tasks merged into main, plus JSON for both
if simple. Python coverage.py supports JSON directly. Installed Go cover help
supports native profiles/text/HTML, not coverage JSON; go test JSON describes
test events. Preserve Go's machine-readable profile without a converter or new
dependency, consistent with HUMAN's inexpensive-only condition.

## Inputs and requirements

Integrate accepted Python branch tip `f98fe2aef3784361d547f717ff0c85ea70b401ad`
(spec133, implementation8ed990b, acceptance136) and accepted Go branch tip
`67e5239cd9ad3a75f8fcb46b6024b0b3dd5acea0` (spec143, implementationac1fcbf,
acceptance146). Read their specs, evidence and review reports at those exact tips.
Preserve current main's Go template/tooling and all independently accepted task
behavior, including developer-supplied coverage handoff and static reviewer role.
Retain existing reports and their source identities; do not rewrite old branches.

Add Python coverage JSON using the same measured data, written to coverage.json
and ignored by Git. Its content must identify the same four canonical production
scripts with line totals/missing lines, without temporary duplicates or tests.
Document JSON for agents/tooling and HTML for human inspection. No second test
execution for JSON generation and no new dependencies or thresholds. Go retains
coverage/coverage.out, functions.txt and index.html with no false JSON claim.

Integrate on codex/coverage-integration in /private/tmp/newproject-coverage-integration.
Do not touch main until implementation checks and independent review succeed.
After acceptance LEAD uses tools/agents/merge.py to merge this branch to main;
HUMAN explicitly authorized this merge. Preserve .idea and source branches.
No push.

## Roles and files

Standard route. LEAD owns this assignment, README and docs/specs/make-checks.md;
merge/reconcile those documents and update JSON wording after spec approval.
REVIEWER Astra/high report148 for spec, report150 for implementation.
DISPATCHER Luna/low coordinates DEVELOPER Terra/medium. Developer integrates
accepted source/tests/config/process docs and historical reports unchanged,
changes Makefile and .gitignore for JSON, and writes report149. Any document
conflict or substantive new requirement returns to LEAD; README/make-checks are
LEAD-owned. Developer may commit exact released LEAD files with implementation.
No new test framework or source behavior changes.

## Checks and acceptance

Run combined make check and make test-coverage with installed coverage7.10.7.
Coverage data must include four canonical scripts only; confirm JSON matches
terminal/HTML totals and missing-line accounting. Verify JSON failure propagates
by normal Make semantics. Root checks include Go template tests; retain their
real-Go evidence and additionally verify the integrated Go target with a bounded
real temporary module if executable inputs changed. Inspect active docs/links.
Save commands, outcomes, source identities and report locations for static review.
Commit all checked inputs before final review; freeze until review completes.
After merging, compare main tree with accepted integration tip; changed inputs
from hooks/integration require renewed checks/review as appropriate.
