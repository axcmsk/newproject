# Engineering preferences review

## Reviewed inputs and scope

- Brief: LEAD's direct-route handoff records the user's approved split into
  COMMON (general work and reading entry), ENGINEERING (code and agent
  instructions), EDITING (ordinary text), and DIALOGUE (communication).
  Move the existing Agent Instructions section without semantic changes;
  require all roles to read ENGINEERING for relevant tasks. Add the approved
  calendar preference: a suitable direct connection first, otherwise an `.ics`
  import file; browser interaction when explicitly requested or alternatives
  cannot meet the task; distinguish a created event from a prepared file.
  Do not invent additional code rules.
- Reviewed repository: `/Users/andreikondratev/src/agent-personal`.
- Base: `bc10c05911c6f91f832a1d19290eab36500bcf27`.
- Reviewed source: `ab3d367ec084076b9cc824fd07f905bf071df2c0`.
- Changed paths: `COMMON.md`, `EDITING.md`, `ENGINEERING.md`.
- Frozen report repository HEAD:
  `51b3d18b0d3e95023424008d4d0f7f91fee03e35`.
- Only assigned write: `docs/worklog/172-engineering-preferences-review.md`.

## Findings

No blocking findings.

The diff moves the complete Agent Instructions section verbatim from EDITING
to ENGINEERING. The remainder of EDITING and all of DIALOGUE are unchanged.
ENGINEERING adds only its title and applicable task scope; it invents no
additional code requirements. COMMON explicitly applies ENGINEERING reading
to every role before writing, editing, or reviewing code or agent instructions.
Its exception for other roles now names only DIALOGUE and EDITING, so it does
not exempt those roles from the engineering rules. All referenced instruction
files exist in the reviewed commit.

The calendar rules match the supplied approved preference, including the
explicit browser-request override and the distinction between creating an
event and preparing an import file. No project implementation or template
changes are included in the reviewed scope.

## Evidence and limitations

This was an independent static review of the pinned diff and instruction files.
No project code or executable checks were run by REVIEWER.

LEAD reports successful read-only assertions for the verbatim section move,
unchanged EDITING remainder, and existing COMMON link targets; LEAD also reports
that the final staged `git diff --check` passed after removing an extra trailing
blank line from ENGINEERING. Static inspection supports those content claims.
The personal repository contains only the four Markdown instruction files and
has no configured check suite.

Read `/tmp/common-check.log`: the saved `make check` output shows formatting
success, lint success, and 75 passing tests. LEAD identifies this as reusable
evidence for unchanged newproject implementation at the frozen report HEAD.
Those checks do not exercise the personal instruction wording; acceptance of
that wording rests on the static review. The unrelated untracked `.idea/` in
agent-personal was left untouched.

## Verdict and next owner

`ACCEPTED` for the named brief and personal-repository source commit.

Return to LEAD for final closeout. This report does not authorize publication
or unrelated changes. REVIEWER releases report writer ownership after the
report helper commits this file.
