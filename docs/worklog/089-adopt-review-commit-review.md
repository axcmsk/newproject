# Review helper adoption implementation review

Verdict: `ACCEPTED`.

Reviewed implementation and initial HEAD:
`69c7f1eb793373d0588de6e0b17e9ffc320a2183`, on `codex/adopt-review-commit`.
The index and working tree were clean at review start. REVIEWER's only allowed
write is `docs/worklog/089-adopt-review-commit-review.md`.

Approved specification: `docs/specs/newproject.md` and assignment
`docs/worklog/086-adopt-review-commit-task.md` at
`27177ed212635cd19fa5bd0ecb704b0caffc9af9`, accepted in report 087 at
`e24d9878352e9af027cdaef07f2d34f71a5d2470`.

## Scope and conclusions

Static review covered `newproject.py`, `tests/test_newproject.py`, evidence 088,
the correction-free implementation diff from the accepted specification report,
and the relevant source/helper and workflow contracts. No blocking findings.

The generator preflights a real root tools directory and both named readable
regular helpers. It rejects selected-layer collisions before target mutation,
permits a shared tools directory, and appends exactly the two helper paths to
the existing payload. Root/cwd resolution, exclusive file creation, byte/mode
preservation and partial-failure handling remain in the established copy path.
Argument parsing still precedes all helper checks, so help and syntax errors
remain independent of source availability. No helper runs during generation.

The expanded source tests cover each helper missing, symlinked, a directory or
a FIFO, plus a symlinked tools directory. Injected read failures assert the
target is unchanged. File/directory collisions are exercised in both selected
layers; injected copy-time collisions preserve the appearing file and report
partial state. Shared tools directories retain layer files and both helpers,
while unrelated root tools are excluded.

Real-template tests inspect helper bytes/modes and shared guides in both normal
and heavy output. They retain the installed merge exercise and invoke the
installed report helper after bootstrap. Report success checks its returned
commit ID, sole parent, report-only diff, contents and clean state. Foreign-dirt
refusal checks the intended diagnostic, preserved HEAD, clean index and preserved
report/foreign contents. Report-helper test environments remove inherited Git
overrides. Existing generator, merge, report-helper and journal coverage remains
in the configured suite; the test count is unchanged because cases were expanded
within existing test methods.

## Evidence and limitations

All four SHA-256 identities in evidence 088 match the reviewed generator, test
file and unchanged helper sources. The record reports 53 passing unittest cases
(18.581s), passing configured Ruff lint and format checks (eight files), and
passing working/staged whitespace checks including the final evidence record,
using Python 3.9.6 and Git 2.54.0. These are DEVELOPER results, inspected statically;
REVIEWER did not rerun tests, validators or other project checks.

The scope remains new generated projects only. Existing projects are not updated,
helper behavior and template instructions are unchanged from their accepted
versions, and concurrent hostile filesystem replacement remains outside the
generator contract. Adding this report does not alter checked inputs.

## Handoff

Save only this report using the accepted REVIEW-COMMIT procedure with the initial
HEAD above; this administrative helper execution does not constitute a test or
general runtime action. After successful report commit and report-only handoff
verification, REVIEWER releases writer ownership to DISPATCHER. DISPATCHER may
return accepted source, report and check identities to LEAD for integration under
the existing workflow. Return the report commit separately from the reviewed
implementation identity.
