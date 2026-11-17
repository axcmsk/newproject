# Instructions as code review

## Scope and source

LEAD's direct-route brief records the user's explicit approval to add, as the
first Agent Instructions paragraph in ENGINEERING, the principle that agent
instructions are code regardless of file format because they define system
behavior, and therefore receive the same checks and independent review
requirements as program code. English wording matches the existing file.

- Repository: `/Users/andreikondratev/src/agent-personal`.
- Base: `ab3d367ec084076b9cc824fd07f905bf071df2c0`.
- Reviewed source: `aea6e526867e6f349012df90af8d03bf37022e23`.
- Scope: the added first paragraph under `ENGINEERING.md`'s Agent Instructions.
- Frozen report HEAD: `60b12c309204b1122a2e31809ea46d380225812c`.
- Only allowed write: `docs/worklog/173-instructions-as-code-review.md`.

## Findings and evidence

No findings. The paragraph preserves all parts of the approved principle:
file format does not change the classification, instructions define system
behavior, and checks and independent review apply equally to program code and
agent instructions. Its placement matches the brief. The pinned commit changes
only this paragraph and its separating blank line. Existing requirements remain
unchanged and consistent with the project's scope rules.

Independent static review inspected the pinned diff, commit scope, and repository
state. LEAD reports that removing the new paragraph reproduces the previous
file exactly and that staged `git diff --check` passed. No configured test suite
exists in the personal repository. Newproject implementation remains unchanged;
the previously inspected `/tmp/common-check.log` contains passing formatting,
lint, and 75 tests. Those results cover the unchanged project code, not the new
instruction's meaning, which was reviewed statically. REVIEWER ran no executable
checks. The unrelated untracked personal `.idea/` was preserved.

## Verdict and handoff

`ACCEPTED` for the named brief and reviewed source commit.

Return to LEAD for closeout. Release report writer ownership once the report
helper commits this file. No additional changes or publication are authorized
by this verdict.
