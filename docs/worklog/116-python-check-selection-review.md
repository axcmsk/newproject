# Individual check selection: implementation review

Verdict: `ACCEPTED`.

Reviewed implementation and initial HEAD:
`b8597f5f6e64ad8bd1543fa633baff6f6d19cbec`, on `codex/check-helper`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/116-python-check-selection-review.md`.

Approved corrected contract: `docs/specs/check.md` at
`11cf4cc60d9f353946c86d10b77c98dff31dae30`, Git blob
`799c623f228cae0188e933f62ad2a6dcb911e1c6`. Report 114 at
`36d0beb9a44d05d71c5f5a6d1718eb1c5b389385` provided conditional acceptance;
task 113 records exact closure and assignment. This review checks implementation
against that corrected contract, not the earlier contradictory wording.

## Scope and conclusions

Static review covers `tools/python_check.py`, `tests/test_python_check.py`,
evidence 115 and the conditional-closure record. No blocking findings.

The corrected specification contains exactly the three literal substitutions
from report 114, its Git blob matches the recorded identity, and the closure
checkpoint changes only the specification and task appendix. The appendix records
the reviewed base/report, exact application, no other source changes and passing
staged whitespace validation. The approved dependency and continuation meanings
are therefore preserved in the implementation reference.

Argparse limits `--only` to format, lint or tests and rejects incompatible
reformat combinations before calling `run_checks`. Missing/invalid values use
parser errors; normal argument order/repetition semantics are retained. The
runner filters its existing ordered command list before execution, so one
selection runs exactly one unchanged command with the same targets, cwd and
interpreter. With no selection, the full format/lint/tests sequence remains.

Results, summary and overall status are based only on executed steps. Omitted
steps are neither launched nor checked for availability. Tests-only still invokes
the unchanged unittest suite, including its real Ruff formatting test; no skip
or false dependency exemption is introduced. A selected formatter failure cannot
launch lint/tests. Existing streaming, failure handling and interruption behavior
remain in force, and the output does not claim all checks ran for a selection.

Focused tests assert CLI propagation, each selection's exact single subprocess
call and result-only summary, both formatting modes, both valid argument orders,
invalid/missing choices and incompatible flags with no launch, and selected
failure/launch-error/interruption outcomes. Existing full-run, real-formatting,
help and interruption coverage remains. The source checkpoint contains only the
assigned helper, tests and evidence; no unrelated changes are included.

## Evidence and limitations

Both SHA-256 identities in evidence 115 match the reviewed source files. The
final actual full `python3 tools/python_check.py --reformat` run is recorded with
overall exit 0, format exit 0 (ten files unchanged), lint exit 0 and unittest exit
0 with 69 tests passing in 23.875s. Versions are Python 3.9.6, Git 2.54.0 and
Ruff 0.17.3. Working/staged whitespace checks passed. Earlier successful full
runs were repeated after changed check inputs; no final executable failure is
reported.

These are DEVELOPER results, inspected statically. REVIEWER ran no project checks.
Adding this report does not change checked inputs; only the accepted strict
review helper is used for administrative report saving.

## Handoff

Commit only this report directly atop the pinned source, verify the report-only
child and clean state, then release writer ownership to DISPATCHER. Return the
report commit separately from the accepted source identity. DISPATCHER may report
completion to LEAD. Keep all work on `codex/check-helper`, without merge or push.
