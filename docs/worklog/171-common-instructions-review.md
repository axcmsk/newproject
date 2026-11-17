# Common personal instructions review

## Scope and sources

Independent REVIEWER review of LEAD’s direct-route brief: create a common file
other than `AGENTS.md` in the confirmed sibling `agent-personal` directory;
centralize when to read `DIALOGUE.md` and `EDITING.md` and the Chat/Work/Local/Cloud
response labels; update the affected entry points while preserving other
personal preferences.

Reviewed frozen sources:

- `newproject` commit `db5086da0bdb329f9d38856e5503300a254d8665`, against its parent:
  root and base-template `AGENTS.md`, root and base-template LEAD guides, README.
- `agent-personal` commit `bc10c05911c6f91f832a1d19290eab36500bcf27`, against its
  parent: new `COMMON.md` and removal of the duplicate labels in `DIALOGUE.md`.
- Current `/Users/andreikondratev/.codex/AGENTS.md`, containing the absolute
  common-file entry point and missing-file fallback.
- Repository AGENTS, PROJECT-RULES, PROCESS, REVIEWER and REVIEW-COMMIT guides;
  current personal preference files; LEAD’s check evidence and clarification
  of the prior global entry point.

Recorded `newproject` HEAD at review start was
`db5086da0bdb329f9d38856e5503300a254d8665`. Only this report was authorized for
reviewer writes. Both repositories were clean at inspection.

## Findings

No blocking findings.

The common file preserves the four labels, their environment-based selection,
the prohibition on guessing execution location, bold separate-line formatting,
the following blank line, first-response applicability and artifact exclusion.
It retains LEAD’s personal-reading responsibilities and delegated-text handoff,
adds an explicit equivalent for projects without roles, and preserves silent
skipping of missing preference files and instruction precedence.

Root and template entry points match. The generated-project instruction resolves
the optional sibling path from the generated root. LEAD guides now route through
those entry points. README names the actual sibling directory. The personal
repository diff removes only the duplicate label section from DIALOGUE;
EDITING and other personal content are unchanged.

## Evidence and limitations

LEAD supplied `make check` results for the unchanged reviewed inputs in
`/tmp/common-check.log`. Static inspection confirms Ruff formatting and lint
passed and all 75 tests passed. LEAD also reported successful `git diff --check`
for both repositories and no configured personal-repository checks. No executable
checks were run by REVIEWER. No production code or test assertions changed.

The global entry point is outside the two reviewed repositories. Its prior
contents were not independently available as a versioned diff. LEAD attested
that it contained only the response-label instructions now represented in
COMMON; the current entry point was inspected directly. This review does not
claim an observed new-chat runtime test of instruction loading.

## Verdict and next owner

`ACCEPTED` for the named scope and source versions.

LEAD owns final closeout and verification that the report commit contains only
the assigned report above the pinned source HEAD. No publication is authorized
by this verdict.
