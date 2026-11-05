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

Under the user's standing instruction, make local checkpoint commits before
review and after corrections, then commit the review report at closeout. This
authorizes neither pushing, publication nor deployment. A checkpoint is not
acceptance. Feature branches are optional; follow any explicit project policy.
Preserve unrelated work and reviewed commits; do not amend, rebase, squash or
otherwise rewrite reviewed history.

### Commit messages and ownership

Use `<type>: <short description>`:

- `step:` — an independently meaningful stage of work.
- `fixup:` — a correction or refinement of the current stage, including review fixes.
- `docs:` — documentation supporting another stage.
- `review:` — an independent review report.
- `log:` — check results, work journal entries or status updates.

Choose the type by content, not by the committer's role. For mixed commits, use
the type of the main change. Supporting documents and records do not require
separate commits. Before committing, choose the appropriate type and check the
message format. An existing mistyped commit is not a review blocker; do not
rewrite history solely to correct its type or message.

An independent stage produces a distinct result worth preserving for a separate
revert or reuse. Specification, implementation and review fixes may belong to
one stage: `docs:`, followed by `step:`, then `fixup:`. Use `step:` for a standalone
documentation task, such as a separately scoped requirements change; use `docs:`
for documentation supporting another stage.

The assigned writer may commit their own files and exact files prepared and
released by other roles, within the role's write authority. Permission to commit
another role's files does not include permission to edit them. Stage explicit
released paths only and verify the staged changes before committing.

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
fixes before the final checks. Existing results remain valid when their inputs
have not changed; adding only a review report does not require another run.

At review start, record HEAD and the permitted review-report paths. Keep HEAD
and reviewed inputs unchanged until review is complete. Report commits follow
[REVIEWER's commit boundary](roles/REVIEWER.md#report-commits). At handoff, verify
that the report commit's parent is the recorded HEAD and that its changes are
limited to the permitted reports; the report still identifies the original
reviewed source. This expected HEAD advance does not require another source
review or invalidate checks on unchanged inputs. Investigate any other mismatch;
never include unexpected edits as accepted work. Authorized corrections establish
a new expected commit and return the affected part to review, except exact
corrections covered by conditional acceptance.

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
