# Project rules

## Repository purpose

This repository maintains reusable project defaults in `template/`. Root
`AGENTS.md` and `docs/workflow/` govern work on this repository. Template rules
are deliverables for future projects; keep shared policy aligned between the
two copies and document intentional project-specific differences.

The repository includes project defaults and `newproject.py`, a standard-library
Python 3.9+ command-line script requiring Git on PATH. Its contract is in
[Project creation](../specs/newproject.md). Setup, usage and the unittest command
are maintained in [README](../../README.md). DEVELOPER owns executable checks;
review documentation links and policy consistency alongside code changes.

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

### Checks, review and commit

Use this order: finish changes, pass configured checks, obtain any required
independent review, then commit. Before submitting work to REVIEWER and before
every commit, the project's configured tests, linter and formatting check must
have passed using its documented commands. This also applies to documentation-only
commits. Give REVIEWER the checked version and saved check results. Use the formatter's check mode; if fixes
are needed, apply them before the final checks and review the resulting diff.

Run only checks that are configured for the project; do not add tools just to
satisfy this rule. A configured check that cannot run is a blocker, not an absent
check. Resolve failures or report the blocker before committing.

Check results must cover the code, tests and configuration being committed.
Rerun affected checks after changing their inputs. Adding only a review or check
report does not invalidate results for unchanged inputs. Record the commands,
outcomes and checked version in the task evidence, or in the final response for
routine work without a worklog. Preserve PROCESS's check ownership: DEVELOPER
runs executable checks for logic work; LEAD may run them for documentation-only
work. REVIEWER remains static-only.
