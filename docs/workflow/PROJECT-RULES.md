# Project rules

## Repository purpose

This repository maintains common defaults in `template/base/` and an additive
heavy variant in `template/heavy/`. Its own workflow remains normal. Root
`AGENTS.md` and `docs/workflow/` govern work on this repository. Template rules
are deliverables for future projects; keep root and base shared policy aligned
and document intentional project-specific differences. Heavy adds explicitly
selected rules without replacing the common files.

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
repository workflow. Feature branches are optional but useful for multi-step
work, unless project policy requires them. Pull requests are not required.

Under the user's standing instruction, make local checkpoint commits before
review and after corrections, then commit the review report at closeout. This
authorizes neither pushing, publication nor deployment. A checkpoint is not
acceptance.
Preserve unrelated work and reviewed commits; do not amend, rebase or otherwise
rewrite reviewed history. When a merge into `main` is needed, LEAD uses
`tools/merge.py` following [MERGE](MERGE.md). The helper may squash the result
on `main`; preserve the source branch and its reviewed commits.

### Commit messages and ownership

Work and report commits in task branches follow [BRANCH-MESSAGE](BRANCH-MESSAGE.md).
Merge results and standalone commits made directly on `main` follow
[MAIN-MESSAGE](MAIN-MESSAGE.md).

Supporting files need no separate commit. Check the message before committing;
a wrong existing prefix neither blocks review nor warrants rewriting history.

The assigned writer may commit their own files and exact files released by other
roles, but may not edit another role's files. Stage explicit permitted paths and
check the staged changes. Role-specific write limits still apply.

### Checks, review and commit

Use this order: finish changes, pass configured checks, commit the reviewable
inputs, obtain independent review, then commit the review report. Apply this to
specifications and process documents as well as code. Corrections require a new
checked commit and review of the affected part. Routine content exempt from
review under AGENTS needs only the applicable checks and a local commit.

Before submission to REVIEWER and before every commit, the configured tests,
linter and formatting check must have passed using documented commands. This
also applies to documentation-only commits. Give REVIEWER the exact commit,
paths and saved check results. Use the formatter's check mode; apply needed
fixes before the final checks.

Record HEAD and allowed report paths at review start; keep HEAD and reviewed
inputs fixed until review completes. REVIEWER then follows its
[report commit rules](roles/REVIEWER.md#report-commits). At handoff, verify that
only the allowed reports were committed on top of the recorded HEAD. This report
commit does not change source acceptance.
Investigate unexpected changes; source corrections return to review unless
covered by explicit conditional acceptance.

Run only checks that are configured for the project; do not add tools just to
satisfy this rule. A configured check that cannot run is a blocker, not an absent
check. Resolve failures or report the blocker before committing.

Check results must cover the inputs being committed. Reuse results while their
inputs are unchanged; rerun affected checks when inputs change. Adding only a
review or check report does not require another run. Record the commands,
outcomes and checked version in the task evidence, or in the final response for
routine work without a worklog. Preserve PROCESS's check ownership: DEVELOPER
runs executable checks for logic work; LEAD may run them for documentation-only
work. REVIEWER remains static-only.
