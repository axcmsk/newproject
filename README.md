# New project defaults

Reusable agent rules and workflow guides for new projects.
The starter files live in `template/`; copy its contents to a new project root.
The rules in that directory govern projects created from the template.

## Included

- `template/AGENTS.md`: entry point, communication and process scope.
- `template/docs/workflow/PROJECT-RULES.md`: project configuration and general rules.
- `template/docs/workflow/PROCESS.md`: short and standard task routes, reviews and acceptance.
- `template/docs/workflow/roles/`: LEAD, DISPATCHER, DEVELOPER and REVIEWER.
- `template/README.md`: minimal project entry point.

Create `docs/specs/` and `docs/worklog/` when their first documents are needed.
Keep the source convention `docs/` consistently throughout the template.

## Inherited defaults

LEAD uses the user's current chat settings. Worker defaults are DISPATCHER:
Luna / low; DEVELOPER: Terra / medium; REVIEWER: Astra / high. The exact IDs and
unavailable-setting policy are in the LEAD guide. These are preferred settings,
not a claim that every environment supports those models.

The workflow retains bounded worker contexts, frozen review inputs, independent
static review, developer-owned executable checks and explicit review verdicts.
Optional personal preferences are read from sibling `common/DIALOGUE.md` and
`common/EDITING.md` when present; the template does not require that directory.
Communication uses the user's language and the environment-based mode label.

## Git authorization

Local commits after required checks and independent review are authorized.
Pushing, publication and deployment require their own authorization. No branch
strategy is imposed by the template.

## Status and next step

Root [AGENTS.md](AGENTS.md) applies these rules to this repository.
Independent review records are kept in `docs/worklog/`.
No project-creation script is included yet. A later script should run from this
repository and create a sibling project directory from `template/`, refusing to
overwrite an existing target. Its behavior and checks should be specified before
implementation.
