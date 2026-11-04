# Project rules

## Project configuration

Record confirmed project-specific decisions here as they become known:

- Purpose, intended users, scope and exclusions.
- Authoritative inputs, specifications and generated outputs.
- Runtime, dependencies and supported environments, when applicable.
- Setup and check commands, with references to README where maintained.
- Data formats, compatibility requirements and external integrations.
- Branch, commit, publication and deployment policy, if explicitly established.

An unspecified setting is unknown, not permission to invent a requirement.
Resolve routine implementation details within the authorized task; ask only
when a missing decision materially affects scope, correctness or authority.

## Documentation structure

- `README.md`: purpose, entry points, setup and normal usage.
- `docs/workflow/`: process, roles and this project's rules.
- `docs/specs/`: current behavioral and format specifications, as needed.
- `docs/worklog/`: task briefs, reviews and implementation evidence, as needed.

Keep format details in their specifications rather than duplicating them here.
Create specifications and worklogs only when required or useful; avoid empty
placeholder records. Name each worklog with the next unique three-digit number
and a descriptive suffix, such as `001-parser-task.md`. Do not renumber existing
files. LEAD reserves filenames before parallel work to avoid collisions. The
short route permits combined records without separate handoff documents.

## Working rules

- Preserve supplied facts and useful existing content. Separate verified facts,
  assumptions and examples. Do not invent missing information or outcomes.
- Edit authoritative sources; regenerate derived artifacts using their documented
  process. Identify the source before editing an apparent generated output.
- Update specifications, implementation and affected data together when changing
  a format or behavior. Preserve stable identifiers and compatibility unless
  the task authorizes a migration.
- Preserve unrelated changes. Avoid destructive cleanup or unsolicited rewrites.
- Do not store secrets or unnecessary personal data in source or worklogs.
- Choose meaningful checks proportionate to the change. DEVELOPER owns executable
  checks for logic tasks under PROCESS. Report only checks actually performed.
- Inspect the final diff and record material limitations honestly.

## Git workflow

When the project uses Git, inspect the current branch, working-tree status and
remotes before changing files. Preserve unrelated work and follow the established
repository workflow. A local feature branch may be useful for multi-step changes;
this template mandates neither a branch strategy nor pull requests.

Under the user's standing instruction, commit completed changes after the
checks and independent review required for their scope. This authorizes local
commits only, not pushing, publication or deployment. Preserve unrelated work;
avoid force operations and rewriting shared history.

Freeze review inputs with a commit and path or a saved snapshot with content
hashes. Review and check requirements apply whether or not a commit is made.
