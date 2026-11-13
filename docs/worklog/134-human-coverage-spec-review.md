# Human coverage specification review

Verdict: `ACCEPTED_SUBJECT_TO_CHECKS`.

Reviewed specification: `docs/worklog/133-human-coverage.md`, README,
`docs/specs/make-checks.md`, and root/base PROCESS at frozen HEAD
`ea890c7392c4bfc5f743582fed543de6f96c8195`.
Baseline: `3fed10ba88da4fa29fd10a997b26e03fac600f35`.
Only allowed review report: `docs/worklog/134-human-coverage-spec-review.md`.

## Findings and assessment

F1: `docs/workflow/PROCESS.md:88` and
`template/base/docs/workflow/PROCESS.md:88` describe mechanical implementation
handoff independently of the standard route. Coverage is required only in
standard-route step 4, leaving the short route without the same obligation.
This does not fully implement HUMAN's final requirement that configured
coverage accompany implementation handoff. Close F1 through condition C1 below.

Otherwise the specification is sufficiently bounded: existing tests and normal
check targets stay unchanged, collection must include subprocesses and copied
scripts, HTML and terminal output must be usable, generated artifacts stay local,
and percentages establish no acceptance gate. The final HUMAN clarification
clearly supersedes earlier REVIEWER execution permission. Root/base process
changes preserve DEVELOPER runtime ownership and REVIEWER static inspection.

The pinned coverage.py documentation supports Python 3.9, subprocess collection,
path consolidation, and standard text/HTML reports. This establishes technical
plausibility, not successful collection in this repository; the specified
implementation checks must demonstrate that outcome and its runtime cost.
Sources: [configuration](https://coverage.readthedocs.io/en/7.10.7/config.html),
[coverage.py 7.10.7](https://coverage.readthedocs.io/en/7.10.7/).

## Exact conditions for closure without another review

Author: LEAD. Base for all allowed corrections:
`ea890c7392c4bfc5f743582fed543de6f96c8195`.

C1: In both `docs/workflow/PROCESS.md` and
`template/base/docs/workflow/PROCESS.md`, replace the unique text:

```text
  REVIEWER checks the exact commit and saved results.
```

with exactly:

```text
  REVIEWER checks the exact commit and saved results. The coverage handoff
  requirements in standard-route step 4 also apply to these mechanical changes.
```

Evidence locations are those two files' mechanical-code-change bullets under
`Short route for small tasks`. Expected value: the exact replacement above in
both files, with no other content changes in either file.

C2: After C1, LEAD runs `make check`; formatting, lint, and all 60 tests must
pass, with overall exit 0. Append exactly this closure evidence section to
`docs/worklog/133-human-coverage.md` only after observing those results:

```text
## Specification review closure evidence

- Reviewed base: `ea890c7392c4bfc5f743582fed543de6f96c8195`.
- Checked inputs: reviewed base plus the two exact PROCESS insertions in review 134 condition C1; executable inputs unchanged.
- Command: `make check`.
- Formatting: PASS.
- Lint: PASS.
- Tests: 60 passed.
- Overall exit: 0.
```

Evidence location: that section's exact fields and values. Save any unexpected
result separately and return to REVIEWER instead of claiming closure.

Commit the corrected documents after checks and provide the full corrected
commit ID to DISPATCHER. Relative to the reviewed base, the complete permitted
change list is C1 in the two PROCESS files, C2's appended evidence in report 133,
and this review report. DISPATCHER may close C1/C2 without another review only
when all literal comparisons match, the corrected commit contains exactly those
changes, and its identity is retained with this reviewed base and closure
evidence. Other changes or mismatches require REVIEWER. Do not claim that the
corrected version was independently reviewed.

## Evidence, limitations, and next owner

LEAD reported pre-review `make check` success: formatting and lint passed,
60 tests passed in 23.788 seconds. Only documentation changed from the baseline.
REVIEWER performed static inspection and did not execute project checks.
Implementation has not begun and is not accepted by this review.

Next owner: LEAD for C1/C2, then DISPATCHER for exact closure and implementation
routing. REVIEWER releases exclusive report-writer ownership after committing
this report. No merge or push is authorized.
