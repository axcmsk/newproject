# Individual check selection: specification review

Verdict: `ACCEPTED_SUBJECT_TO_CHECKS` with the literal corrections below.

Reviewed checkpoint and initial HEAD:
`b59676c6a9a39f3d59cc93c3e64d0274688c7a2b`, on `codex/check-helper`.
Baseline: `65f6f857f5b3edf385a442f0dd36b3cae5e14d15`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/114-python-check-selection-spec-review.md`.

## Scope and findings

Static review covers task 113, the revised selection contract, README and the
existing helper-test dependencies. Selection, compatible flag combinations,
argparse errors, selected-result summaries and the full-verification boundary
are otherwise coherent. Two wording conflicts require correction before dispatch.

R1: `docs/specs/check.md:33-34` says tests-only needs no Ruff, but the retained
`tests/test_python_check.py:115-141` integration test invokes the local Ruff
interpreter unconditionally. The selected suite still has that dependency.
LEAD clarified that selection limits wrapper steps, not dependencies internal
to a selected check; no integration-test skip or dependency exemption is intended.

R2: `docs/specs/check.md:38-39` unconditionally requires lint/tests after a
formatter failure, conflicting with the exactly-one-step promise for format-only
selection. LEAD confirmed that continuation applies only to a full run.

## Literal closure conditions

LEAD may close these conditions without another review only by making the exact
changes below to `docs/specs/check.md` from the reviewed base. README and executable
inputs must remain unchanged. Other substantive changes require review.

C1. Replace these two lines:

```text
argparse option repetition/order rules apply. Selected checks do not require
tools for omitted steps: `--only tests` needs no Ruff/virtual environment.
```

with:

```text
argparse option repetition/order rules apply. The wrapper starts no omitted step
and performs no separate availability check for its tools; dependencies used
internally by the selected check still apply, including Ruff used by this
repository's tests.
```

C2. Replace:

```text
start, still run lint and tests and return overall failure. Preserve partial
```

with:

```text
start, return overall failure. In a full run, still run lint and tests; a
format-only run must not launch other steps. Preserve partial
```

C3. Replace:

```text
choices/missing values and incompatible flags start nothing; tests-only without
Ruff; selected failure, launch error and interruption outcomes. Preserve all
```

with:

```text
choices/missing values and incompatible flags start nothing; tests-only launches
only unittest (suite dependencies still apply); selected failure, launch error
and interruption outcomes. Preserve all
```

C4. Append closure evidence to task 113 under `Conditional review 114 closure`:
record the reviewed base above, this report's commit, the corrected specification's
full Git blob ID, `applied: C1, C2, C3 exactly`, `other_source_changes: none`, and
the successful staged whitespace-check command/result. The corrected spec must
equal the reviewed spec with exactly C1-C3 substituted; the recorded blob must
match the corrected specification in the new committed checkpoint. Only these
spec edits and the closure-evidence appendix are permitted for this closure.
Return that new checkpoint identity with the acceptance record before dispatch.
Any mismatch, additional source edit or failed check returns to REVIEWER.

## Evidence, limits and handoff

Task 113 reuses accepted unchanged executable/template inputs from
`485b423c68c9a62ab452968c6a14b29ed24c0dcf`: full renamed helper overall 0,
format/lint/tests all 0, 66 tests passed. LEAD reported staged whitespace-check
success for this checkpoint, exit 0, chunk `9960df`. REVIEWER ran no project
checks. The literal corrections and evidence appendix do not change those
executable inputs, so no duplicate full run is required.

Commit only this review report using the accepted strict helper, verify the
report-only direct child and clean state, then release writer ownership to LEAD
for C1-C4. This verdict does not yet authorize implementation dispatch. After
exact closure, the corrected specification is covered by conditional acceptance,
not claimed as separately reviewed. Keep work on `codex/check-helper`; no merge
or push.
