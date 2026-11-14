# Direct implementation by LEAD

## Assignment and sources

LEAD owns this documentation change under the existing short route. Baseline:
`fd3f7c814c12cc692e7fbc29730733576bc1715c`, root `AGENTS.md`,
`docs/workflow/{PROCESS,PROJECT-RULES}.md`, role guides and their base-template
counterparts. HUMAN requested direct implementation when materially easier
than explaining it to DEVELOPER, with a prior specification, optional later
handoff and mandatory independent result review. HUMAN agreed to clarify check
ownership and allow joint specification/result review after implementation.

## Requirements and acceptance

- Add an explicit direct route chosen by LEAD without artificial size limits.
- Before implementation, save a specification with requirements and acceptance
  criteria; a brief document is sufficient and implementation details are optional.
  Preserve source identity, scope, permissions and material decisions.
- Allow joint independent specification/result review after implementation,
  without requiring separate preliminary specification approval.
- LEAD owns implementation checks, evidence, corrections and review handoff on
  this route; REVIEWER remains independent and static-only.
- Allow transfer to DEVELOPER with specification, findings, current changes and
  evidence, explicit ownership transfer and return to the ordinary route.
- Preserve check, coverage, commit, frozen-input and permission requirements.
  Resolve unclear requirements before dependent work. Role/process authority
  changes still require review before reliance.
- Keep root and base policy aligned; reconcile affected role references.

Allowed changes: root/base AGENTS and workflow documents as needed, this record
and independent review `docs/worklog/156-direct-lead-review.md`. No generator,
test, heavy-variant behavior or unrelated changes. Required checks: `make check`,
static link/policy/diff inspection. LEAD runs checks for this documentation task.
Checkpoint before REVIEWER (Astra/high); REVIEWER owns only its report. Stop at
local checked and independently reviewed changes; no push or publication.

## Evidence

Checked version: baseline plus the eight workflow policy files in this task’s
checkpoint commit; no executable source changes. `make check` passed (exit 0):
Ruff format, Ruff lint and the full unittest suite. Raw output:
`/tmp/direct-lead-checks.log`. `git diff --check` passed. Root/base PROCESS and
modified role guides are identical; PROJECT-RULES retains project-specific
content and equivalent shared check ownership. Static inspection found no new
link targets or changes to generator/coverage configuration.

Review will run in a separate clean worktree so the pre-existing untracked
`.idea/` directory remains untouched. REVIEWER may commit only report 156;
LEAD will bring that report commit into the original checkout.

## Clarification and revision

HUMAN clarified that fast track is the existing direct documentation route
extended to implementation, with a mandatory prior task specification. Express
the route as that extension and its differences instead of restating the full
process. Preserve all accepted requirements. Review the affected revision in
`docs/worklog/157-direct-lead-simplification-review.md`.

Revision checks: `make check` passed (exit 0; Ruff format/lint and 75 tests),
covering the revised root/base PROCESS files in the revision commit. Raw output:
`/tmp/direct-lead-revision-checks.log`. `git diff --check` passed.
