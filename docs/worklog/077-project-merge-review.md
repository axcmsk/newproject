# Shared project merge workflow implementation review

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `6cc1827d91f4f196761eb0be13127e3011e97003`.
- Implementation baseline: `ad32e4e4b6d0b674ba5e9e05c7c4309db2402e0e`.
- Approved contract: `docs/specs/newproject.md` and task 074 at
  `9115bc08c994507f95edf851dee40c04ae576711`, accepted in report 075
  at the implementation baseline. Both contract files remain unchanged.
- Scope: generator helper installation, tests, released workflow/README changes
  and implementation evidence 076. Findings and conditions: none.
- Next owner/action: DISPATCHER returns acceptance to LEAD for the authorized
  final integration under MERGE. No merge or push was performed by REVIEWER.

The generator resolves the single helper source beside itself, validates the
real directory and readable regular file before target mutation, and refuses
reserved selected-layer paths. Shared tools directories remain valid. Installation
uses the existing exclusive copy and mode-preservation path; it neither copies
unrelated repository tools nor executes the helper. Help and argument errors still
exit before source inspection. Git blob identity confirms tools/merge.py is
unchanged from the approved source.

The three base guides, PROCESS and LEAD match their root counterparts exactly.
PROJECT-RULES retains project-specific content while aligning shared merge and
message policy. Heavy keeps mandatory task branches and checkpoints, delegates
integration to MERGE, and preserves source history without the superseded no-ff
or additional approval restriction. Operational writer and report boundaries
remain unchanged. LEAD confirmed the committed documents match its released
content; no separate release snapshot was retained. Their committed content was
independently reviewed against the approved contract.

Static test inspection covers helper source failures, selected-layer collisions,
shared directories, absent-source help, injected copy refusal and preservation,
and real generated normal/heavy merges with installed bytes/mode, guides,
message/content, clean state and preserved source tip assertions. Existing
creation and merge-helper tests remain in scope of the reported full suite.
Evidence 076 records 43 passing tests, README Ruff lint/format and diff checks,
with source identity and runtime versions. These are DEVELOPER's reported results;
REVIEWER did not execute code, tests or validators. Host-only execution and the
contract's exclusion of hostile concurrent filesystem replacement remain limits.

Review started with a clean tree at the exact source. Only this report is allowed
to change; verify the frozen HEAD and report-only index/tree before committing,
then return the report commit separately and release writer ownership.
