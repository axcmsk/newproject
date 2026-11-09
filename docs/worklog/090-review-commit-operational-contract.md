# Explicit operational paths: contract extension

Baseline: 941708481d179ddb2e7fdb2653023e5ff7ced673.
HUMAN requested extending the report helper contract to support explicitly
authorized operational files left unstaged. This stage changes the contract
only; implementation and workflow adoption remain a subsequent stage in the same
codex/review-commit-allowed-dirty branch. Do not merge this pending contract into
main or publish it during this stage.

LEAD owns docs/specs/review-commit.md and this record. Define repeatable exact
--allow-dirty paths, tracked regular files, no overlap/staged operational changes,
report-only commits and operational snapshot preservation. Keep semantic authority
and STATE block/journal validation with the caller. Existing helper code and
workflow remain unchanged, with planned status explicit in the specification.

Use baseline docs/specs/review-commit.md, tools/review_commit.py,
docs/workflow/REVIEW-COMMIT.md and template/heavy/docs/workflow/HEAVY.md as sources.
LEAD runs configured README checks for this documentation checkpoint and commits
before independent static review. REVIEWER Astra/high owns only
docs/worklog/091-review-commit-operational-spec-review.md, checks the pinned
contract directly with LEAD, and commits its report using the existing strict
helper (no --allow-dirty), then releases ownership. Review all constraints for
internal consistency, authority scope and verifiable acceptance conditions.
No DEVELOPER/DISPATCHER needed until implementation is released. Preserve reviewed
history; no self-review presented as acceptance.

## Check evidence

Executable code and templates remain exactly at baseline 9417084. LEAD ran
`python3 -m unittest discover -s tests -v`: 53 tests passed (19.491s);
`.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`:
passed; `.venv/bin/python -m ruff format --check tools newproject.py tests
template/heavy/scripts`: passed, 8 files formatted; `git diff --check`: passed.
These checks cover the existing implementation, not the planned extension.
The final staged diff is checked in the sequential commit command; report its
actual result to REVIEWER with the checkpoint hash.
