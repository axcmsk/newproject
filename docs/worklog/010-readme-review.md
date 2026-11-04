# README review

## Assignment and identity

- Role: REVIEWER; independent static documentation review requested by LEAD.
- Goal: check README correctness and usability, with optional simplification;
  no new requirements or changes to implementation, rules or process.
- Frozen commit: `c01c5bf131c845c248d6560abb0c5e9fc55f16ca`.
- Reviewed artifact: `README.md`, Git blob
  `5e0b534705d4f4c3195163955ad906dcb62f4bff`.
- Behavioral specification: `docs/specs/newproject.md`, Git blob
  `6cdbbb0dd383efc2d0f300e55d2d2469e053ec0d` at that commit.
- Implementation: `newproject.py`, Git blob
  `f6985d1707d072baf3e985b781ff09cb626e1739` at that commit.
- Supporting sources at the same commit: `tests/test_newproject.py`, the
  `template/` file inventory, `template/README.md`, `template/AGENTS.md`,
  `template/docs/workflow/PROJECT-RULES.md`,
  `template/docs/workflow/PROCESS.md` and
  `template/docs/workflow/roles/LEAD.md`.

## Findings

No blocking findings. The normal command, sibling destination independent of
working directory, template copying, initial unborn `main` branch without a
commit, accepted existing directories, refusal behavior and partial-state
warning agree with the implementation and specification. The template inventory
and agent defaults agree with their sources. The test command names the existing
suite, whose fixtures support the stated temporary-directory isolation.

The README is usable as written. Its principal excess is repetition of agent
policy already maintained in linked source documents.

## Optional reductions

These are editorial suggestions, not acceptance conditions or new requirements.

1. `README.md`, **Agent defaults**: replace the whole section with this paragraph
   at the end of **What new projects include**:

   ```markdown
   Agent instructions start at [template/AGENTS.md](template/AGENTS.md).
   Model defaults and optional personal preferences are documented in the
   [LEAD guide](template/docs/workflow/roles/LEAD.md).
   ```

   This removes duplicated model, process, communication and Git policy while
   retaining access to every detail. Closure, if adopted: those source links
   resolve and the duplicated section is absent.

2. `README.md`, **What new projects include**: the five-file inventory may be
   shortened to one sentence:

   > The template includes a starter README, AGENTS.md and the project rules,
   > process and role guides under docs/workflow/.

   Keep the existing statements that `template/` controls future defaults and
   existing projects are not updated. Closure, if adopted: the sentence matches
   the frozen template inventory and those two statements remain.

Keep the quick-start command and prerequisites, destination/name constraints,
no-initial-commit note, existing-directory limits, partial-state warning,
specification link and test command. They support normal use and recovery rather
than duplicating the internal workflow.

## Verdict and handoff

- Verdict: `ACCEPTED` for `README.md` at the frozen commit above.
- Limitations: static inspection only; no project code, tests, validators or CI
  were run. This is documentation acceptance, not a fresh runtime certification.
- Next owner: LEAD. Keep the accepted README or prepare a smaller revision and
  submit its frozen identity for review of the affected wording. This verdict
  does not automatically accept an edited version.

## Reduced revision review

- Base: `c01c5bf131c845c248d6560abb0c5e9fc55f16ca`.
- Frozen revised artifact: `/private/tmp/newproject-readme-v2.md`, Git blob
  `78b1d3d2e0ec428a40b847e63ea7d0db81291353`; working `README.md` has the same
  blob identity at review. All behavioral and supporting sources remain the
  versions identified above.
- Scope: static review of the reduced README and its diff from the accepted
  baseline. The duplicated agent-policy explanations are replaced with valid
  links to `template/AGENTS.md` and the template LEAD guide. The workflow-folder
  aside and testing administration footer are removed; the personal-preference
  note is shortened without changing its meaning.
- Findings: none. Usage, destination and name constraints, refusal and recovery
  information, template customization, optional preferences and test instructions
  remain intact. The retained file inventory is useful and need not be reduced.
- Verdict: `ACCEPTED` for README Git blob
  `78b1d3d2e0ec428a40b847e63ea7d0db81291353`.
- Limitations: static documentation review only; no executable checks run or
  requested for these wording changes.
- Next owner/action: LEAD may commit the accepted README and this review together
  and report the simplification. No further review is needed for unchanged
  accepted content.
