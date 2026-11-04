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

## Create a project

Requires Python 3.9 or newer and Git on PATH. No Python packages are required.
From this repository run:

```sh
python3 newproject.py my-project
```

From another directory, use the script's absolute path. The destination is always
beside this repository, not beside the current working directory. Quote names
containing spaces. Pass exactly one name argument; names beginning with a dash
are accepted directly.

The script copies only `template/`, including hidden files, and initializes an
uncommitted Git repository on `main`. An existing empty directory or a directory
containing only its own empty Git repository is accepted. Existing Git settings
are preserved. No initial commit is made.

Nonempty projects, repositories with history or staged entries, and symbolic-link
targets are refused. A repeated run after success refuses to overwrite the project.
Preflight failures leave the target unchanged. A later copy or Git failure may
leave partial files; the error identifies the destination for manual inspection.
The script does not delete that directory automatically.

See [the specification](docs/specs/newproject.md) for the complete contract.
Optional sibling `common` preferences are not copied into the project.

## Tests and repository workflow

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary directories and isolated Git settings, including real Git
checks and injected failures. They do not create projects beside this repository.

Root [AGENTS.md](AGENTS.md) applies the workflow to this repository.
Independent review and implementation evidence are kept in `docs/worklog/`.
