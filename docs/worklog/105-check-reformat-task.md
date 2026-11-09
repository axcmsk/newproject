# Optional reformat mode

HUMAN approves --reformat and omitting a redundant format check after formatting.
Baseline a79e2a079e78f708b92b9eee13e5725845dbf0de on codex/check-helper. Keep all
work on this branch; the standing no-merge/no-push instruction still applies.

Contract: docs/specs/check.md in this checkpoint. No-flag behavior unchanged;
opt-in sequence format (writes), lint, tests, exactly once each. Shared targets,
continued checks after failures, overall failure retained, no rollback or lint
fixes. Document the writing option in README and the project-specific formatting
verification exception in PROJECT-RULES; template policies remain unchanged.

LEAD owns specification, README, PROJECT-RULES and this routing. Run existing
configured checks for the documentation checkpoint and commit before independent
static specification review. REVIEWER Astra/high writes only
docs/worklog/106-check-reformat-spec-review.md, commits report via accepted helper
and releases ownership. DISPATCHER Luna/low then forwards the approved exact
checkpoint to DEVELOPER Terra/medium, who owns tools/check.py, tests/test_check.py
and docs/worklog/107-check-reformat-implementation.md. Preserve short functions.

Developer tests approved scope (including real temporary-file formatting), runs
the final actual --reformat sequence, records source identities, versions and
all outcomes, and commits fixup: after diff checks. If the formatter changes
unrelated source files, report those changes to LEAD rather than staging or
discarding them. No additional configured check run is required for unchanged
inputs after that successful sequence under HUMAN's approved exception.
REVIEWER statically reviews source/evidence against contract, writes only
docs/worklog/108-check-reformat-review.md and commits report. Corrections return
to their author. Verify report-only handoffs; freeze reviewed inputs and retain
one writer at a time. No generator/templates, merge, push or unrelated edits.

Documentation checkpoint checks on unchanged executable baseline:
`python3 tools/check.py` overall exit 0; lint exit 0; format --check exit 0
(10 files); unittest exit 0, 63 tests passed (27.526s). `git diff --check` passed.
These results verify current behavior, not the proposed option. Final staged
diff check is part of the sequential commit command, reported to REVIEWER with
the source checkpoint hash. No rerun is required for this evidence-only addition.
