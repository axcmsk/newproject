# Optional reformat mode: specification review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`939b29f415fe7a4eee7b95504c6992cb0df20778`, on `codex/check-helper`.
Baseline: `a79e2a079e78f708b92b9eee13e5725845dbf0de`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/106-check-reformat-spec-review.md`.

## Scope and conclusions

Static review covers task 105, `docs/specs/check.md`, README and the
repository-specific PROJECT-RULES exception, against HUMAN's approval of an
optional formatting mode without a redundant subsequent formatting check.
No blocking findings.

No-flag behavior retains lint, format-check and tests in the established order.
The flag explicitly substitutes formatting with writes, then lint, then tests,
using the same targets and interpreters and exactly three sequential steps.
Successful formatting supplies the formatting result. Formatter failure or launch
failure still allows lint/tests to run while preserving overall failure. Partial
edits remain for inspection; no rollback, lint fixes or Git mutations are added.
Existing help/interruption and streamed-result requirements remain applicable;
help must disclose the writing behavior.

README accurately distinguishes the two modes. PROJECT-RULES makes the successful
formatter a narrow repository-specific substitute for formatting verification in
this run, with lint/tests following on formatted files and evidence reusable only
while its inputs are unchanged. This implements the explicit HUMAN decision;
it does not weaken role/check ownership or change template policy.

Verification requirements cover both exact sequences, CLI propagation, shared
targets, default non-writing behavior, no fourth check, formatter errors and
preserved help/interruption behavior. A real formatting exercise uses an isolated
unformatted Python fixture with content assertions, without recursively running
the repository suite. Final validation uses the actual flag and retains all
three results and source identities. Unrelated formatting changes return to
LEAD for disposition rather than being silently staged or discarded.

Task ownership and later independent implementation review are explicit. Work
must remain on `codex/check-helper` without merge or push. This specification
verdict does not claim the new option is already implemented.

## Evidence and limitations

Task 105 records the existing helper completing with overall exit 0: lint exit 0,
format-check exit 0 for ten files, and unittest exit 0 with 63 passing tests
(27.526s), on unchanged executable baseline inputs. The working-tree whitespace
check passed. LEAD additionally reported successful staged whitespace validation
immediately before this checkpoint in a sequential command, exit code 0,
chunk `695ba3`. These results verify current behavior, not the proposed option.

REVIEWER ran no executable project checks. Adding this report does not alter
checked inputs. Implementation correctness and final reformat-mode results remain
for the next source checkpoint and independent review.

## Handoff

Commit only this report using the accepted strict report-helper invocation with
the initial HEAD, verify the report-only direct child and clean repository state,
then release writer ownership to LEAD. Return the report commit separately from
the approved checkpoint. LEAD may dispatch this exact contract for implementation;
no merge or push is authorized.
