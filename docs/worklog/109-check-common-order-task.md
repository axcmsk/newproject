# Common check order

HUMAN requests format, lint, tests in both modes. Baseline
ccc486f2b548598c35bc2a84b9c1efe8b452ca4a; remain on codex/check-helper,
no merge or push. LEAD owns docs/specs/check.md, README.md and this assignment.
Only the default order changes; --reformat differs solely by omission of --check
from the format command. Keep targets, outcomes, failure continuation, interruption
and all other behavior. Remove the mode-dependent ordering branch.

Specification checkpoint: independent REVIEWER Astra/high reviews these edits,
writing only docs/worklog/110-check-common-order-spec-review.md, commits report
using the accepted helper and releases ownership. DISPATCHER Luna/low then sends
the exact accepted specification to DEVELOPER Terra/medium. Developer owns only
tools/check.py, tests/test_check.py and docs/worklog/111-check-common-order-implementation.md.
Update command-order assertions in both modes and affected error/output tests;
run the configured helper once on final inputs, record exact outcomes/identities
and commit fixup: after staged diff checks. REVIEWER statically reviews source
and evidence, writing only docs/worklog/112-check-common-order-review.md.
Verify report-only commits and clean handoffs; return the accepted branch to LEAD.

Documentation-stage checks reuse unchanged executable/template inputs from
608b2e9076c6042e3465708a576b68dbc2b5e1d8, accepted by report108 at baseline:
python3 tools/check.py --reformat returned 0, format 0, lint 0, tests 0 (66 passed).
Only README/spec/routing text changes here. The sequential commit command runs
git diff --cached --check; pass its actual result and checkpoint hash to reviewer.

## Naming follow-up

After order checkpoint ae9039bf5998ca6020c5c857b6387ee4b1bcb9b4, HUMAN chose
python_check and asked whether README needs the command. Keep the README entry
point and --reformat example. Mechanical rename, with no further behavior change:
tools/check.py -> tools/python_check.py; tests/test_check.py ->
tests/test_python_check.py, including the fixture's SCRIPT path. No old-name alias.
LEAD updates README.md, docs/specs/check.md and PROJECT-RULES references and releases
these documents plus this routing amendment for unchanged developer commit.
Developer's source ownership expands to the old/new paths and existing 111
evidence; run the configured renamed helper, record identities/outcomes and commit.
REVIEWER's same 112 report covers combined ordering, rename, updated references
and evidence. Renaming follows the mechanical short route; the previously
approved ordering contract is otherwise unchanged. Keep prior checkpoints and
historical worklog commands intact. No merge/push.
