# Individual check selection

HUMAN requests individual check options so README needs direct Ruff commands
only for installation. Baseline 65f6f857f5b3edf385a442f0dd36b3cae5e14d15 on
codex/check-helper. No merge/push. Contract: docs/specs/check.md in this checkpoint.
Add --only {format,lint,tests}; default all, --reformat valid with all or format
only, incompatible selections rejected before launch. No other behavior changes.

LEAD owns specification, README and this assignment. Spec REVIEWER Astra/high
owns only docs/worklog/114-python-check-selection-spec-review.md. After its
independent acceptance, DISPATCHER Luna/low releases the exact specification to
DEVELOPER Terra/medium, who owns tools/python_check.py, tests/test_python_check.py
and docs/worklog/115-python-check-selection-implementation.md. Test the contract
selection cases without real-suite recursion, then run the complete configured
helper, record source identity/all outcomes and commit after diff checks.
REVIEWER statically checks implementation/evidence and writes only
docs/worklog/116-python-check-selection-review.md. Commit reports with accepted
helper and verify report-only child/clean handoff. Questions about requirements
return to LEAD; corrections to their author. One writer at a time; no unrelated
paths, generators, templates or workflow authority changes. Leave accepted branch.

For this documentation checkpoint reuse unchanged executable/template inputs
from 485b423c68c9a62ab452968c6a14b29ed24c0dcf, accepted by 112 at baseline:
python3 tools/python_check.py exited 0, formatting check 0, lint 0, tests 0
(66 passed). Only specification/README/routing text changes. The sequential
checkpoint command runs git diff --cached --check and its result is reported
with the commit hash to reviewer.

## Conditional review 114 closure

Reviewed base: b59676c6a9a39f3d59cc93c3e64d0274688c7a2b.
Review commit: 36d0beb9a44d05d71c5f5a6d1718eb1c5b389385.
Corrected specification Git blob: 799c623f228cae0188e933f62ad2a6dcb911e1c6.
applied: C1, C2, C3 exactly
other_source_changes: none
`git diff --cached --check`: passed (exit 0) on the corrected specification and
closure appendix; repeated in the final commit command including this result.
LEAD compared the resulting spec with the reviewed base plus the three literal
substitutions. Existing executable-input check results remain applicable.
