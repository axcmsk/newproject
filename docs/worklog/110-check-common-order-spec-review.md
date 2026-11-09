# Common check order: specification review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`efae4c464ad25a03bfb0f1a73b12ac390275a3cf`, on `codex/check-helper`.
Baseline: `ccc486f2b548598c35bc2a84b9c1efe8b452ca4a`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/110-check-common-order-spec-review.md`.

## Scope and conclusions

Static specification review covers task 109, `docs/specs/check.md` and README
against HUMAN's request for a common order in both modes. No blocking findings.

The contract now specifies formatting, lint and tests for both invocations.
Default formatting retains `--check`; `--reformat` omits only that argument.
Targets, interpreters, sequential execution, result handling, interruption,
formatting-write scope and the absence of a redundant fourth check remain
unchanged. README describes the same order and presents individual diagnostic
commands consistently.

The assignment confines implementation to removal of mode-dependent ordering
and corresponding test/assertion changes, with separate developer evidence and
independent review. Requirements cover the common order in both modes while
preserving default non-writing behavior, flag propagation, failure continuation,
real temporary-file formatting and interruption/help behavior. The existing
project-specific formatting exception remains applicable to the final successful
reformat run; no new authority or unrelated behavior is introduced.

This accepts the new default-order requirement, not an implementation already
matching it. Work must remain on `codex/check-helper`, without merge or push.

## Evidence and limitations

Task 109 reuses unchanged executable/template inputs from accepted source
`608b2e9076c6042e3465708a576b68dbc2b5e1d8`, reviewed in report 108 at the
baseline. Saved evidence 107 records final `python3 tools/check.py --reformat`
overall exit 0, format/lint/tests exit 0 and 66 passing tests. The checkpoint
changes only README, specification and routing text, so reuse follows the
unchanged-input rule. LEAD additionally reported successful
`git diff --cached --check` before the checkpoint commit in a sequential command,
exit code 0, chunk `6520b6`.

REVIEWER ran no executable project checks. Reused results establish prior
behavior, not the proposed default-order change. The later implementation must
supply its own final-input results; adding this report does not alter existing
checked inputs.

## Handoff

Commit only this report with the accepted strict report helper and pinned initial
HEAD, verify the report-only direct child and clean repository state, and release
writer ownership to LEAD. Return the report commit separately from the approved
checkpoint. LEAD may dispatch this exact specification for implementation;
the no-merge/no-push boundary remains in force.
