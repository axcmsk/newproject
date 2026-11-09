# Adopt the review commit helper

Baseline: cad01efe53ed47950a54ea101e0195dd228756cd.
HUMAN asked to integrate the helper first into this repository's instructions,
then into generated projects, and to keep tools and usage instructions in one
task branch. Branch: codex/adopt-review-commit. No push or existing-project update.

## Outcome and scope

LEAD first prepares root workflow instructions and then their common template
counterparts. REVIEWER's report saving uses tools/review_commit.py under the
new REVIEW-COMMIT guide. Permit this specific administrative execution while
preserving static review, DEVELOPER's executable-check ownership and report-only
write authority. Keep root/base policy aligned. LEAD guidance explicitly includes
tools and usage instructions in the same outcome branch.

Preserve heavy's existing permission for operational writes during review:
only when those explicitly permitted changes are present, HEAVY retains direct
report-only commits, checking pinned parent, exact diff, clean index and remaining
unstaged operational changes. No generic fallback after helper refusal. Otherwise
heavy uses the common helper. No helper behavior change or new dirty-path option.

The revised docs/specs/newproject.md defines installation of exactly merge.py
and review_commit.py from root tools into both variants. Preserve bytes/modes,
preflight and exclusive-copy safeguards; reject invalid sources and selected-layer
collisions for either helper before target mutation. Do not copy the whole tools
directory. Help/argument errors remain independent of helper availability.
No new dependencies, initial commits or runtime execution during generation.

Required checks: README unittest suite, Ruff lint and format check, diff checks.
Add integration tests for both installed report helpers (successful report-only
commit plus unrelated dirt refusal with preservation), bytes/modes, helper source
failures/collisions/copy-time protection and no copying of unrelated root tools.
Use isolated temporary repositories; retain all existing merge and generator tests.
Review document links, root/base alignment and heavy exception statically.

## Ownership and routing

LEAD owns README.md, template/base/README.md, docs/specs/newproject.md,
docs/specs/review-commit.md, root/base docs/workflow/{REVIEW-COMMIT.md,PROCESS.md,
roles/REVIEWER.md,roles/LEAD.md}, template/heavy/docs/workflow/HEAVY.md and this brief.
First checkpoint contains only these documentation/specification edits. Its exact
commit pins this assignment and sources for all workers.

REVIEWER Astra/high reviews that checkpoint directly with LEAD. Only permitted
write: docs/worklog/087-adopt-review-commit-spec-review.md. This first review uses
baseline report-commit authority and direct Git, not the unapproved new exception.
After acceptance, DISPATCHER Luna/low releases the exact specification to
DEVELOPER Terra/medium. DEVELOPER owns only newproject.py,
tests/test_newproject.py and docs/worklog/088-adopt-review-commit-implementation.md,
runs configured checks, records identities/results, commits and releases ownership.
REVIEWER statically reviews implementation and evidence, writing only
docs/worklog/089-adopt-review-commit-review.md, then commits using the accepted
report procedure. Changes to requirements return to LEAD; code corrections return
to DEVELOPER. One writer at a time; HEAD/inputs fixed during each review.
LEAD verifies report-only handoffs and integrates accepted changes using merge.py,
preserving source branch and checked tree. No further helpers or process redesign.

## Specification checkpoint checks

LEAD ran documentation-stage checks with baseline executable code and the updated
templates: `python3 -m unittest discover -s tests -v` passed 53 tests (17.882s);
`.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`
passed; `.venv/bin/python -m ruff format --check tools newproject.py tests
template/heavy/scripts` passed (8 files). Subsequent root README/spec wording
adjustments do not change these executable or template inputs. Final staged
diff check is required before commit. New generator behavior remains pending.
