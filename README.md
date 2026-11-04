# New project

Create a new project with shared agent rules, role guides and a Git repository.
The script copies the starter files from `template/` automatically.

## Quick start

Requires Python 3.9 or newer and Git on PATH. No Python packages are required.
From this repository run:

```sh
python3 newproject.py my-project
```

This creates `../my-project/`, copies the template and initializes Git on `main`.
No initial commit is made. Open the new project's README and describe its purpose;
record project-specific decisions in `docs/workflow/PROJECT-RULES.md`.

From another directory, run the script using its absolute path. The destination
is always beside this repository, regardless of the current working directory.
Pass exactly one directory name, without path separators. Quote names containing
spaces; names beginning with a dash are accepted directly.

## Existing directories and failures

An existing empty directory is accepted, as is one containing only its own empty
Git repository. Existing Git settings are preserved; the unborn branch becomes
`main`.

Nonempty projects, repositories with history or staged entries, and symbolic-link
targets are refused. Running the script again after successful creation refuses
to overwrite the project.

Preflight failures leave the target unchanged. A later copy or Git failure may
leave partial files. The error identifies the destination for manual inspection;
the script does not delete that directory automatically.

See [the specification](docs/specs/newproject.md) for the complete contract.

## What new projects include

`template/` is the source of the starter files. The script copies its contents,
including hidden files, into the new project root:

- `AGENTS.md`: agent entry point, communication rules and process scope.
- `docs/workflow/PROJECT-RULES.md`: project configuration and general rules.
- `docs/workflow/PROCESS.md`: task routes, reviews and acceptance.
- `docs/workflow/roles/`: LEAD, DISPATCHER, DEVELOPER and REVIEWER guides.
- `README.md`: a minimal project entry point to fill in.

The workflow uses `docs/specs/` for specifications and `docs/worklog/` for task
records. These directories are created when their first documents are needed.
To change the defaults for future projects, edit `template/`. Existing projects
are not updated by this script.

## Agent defaults

LEAD uses the user's current chat settings. Worker defaults are DISPATCHER:
Luna / low; DEVELOPER: Terra / medium; REVIEWER: Astra / high. Exact model IDs
and the unavailable-setting policy are in the LEAD guide. Availability depends
on the environment.

The workflow defines bounded worker contexts, frozen review inputs, independent
static review, developer-owned executable checks and explicit review verdicts.
Communication uses the user's language and an environment-based mode label.

Optional personal preferences are read from sibling `common/DIALOGUE.md` and
`common/EDITING.md` when present. That directory is not required and its files
are not copied into the project.

The rules authorize local commits after the checks and independent review
required for the change. Pushing, publication and deployment require their own
authorization. The template imposes no branch strategy.

## Testing

Run the test suite from this repository:

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary directories and isolated Git settings, including real Git
checks and injected failures. They do not create projects beside this repository.

Root [AGENTS.md](AGENTS.md) governs work on this repository. Independent review
and implementation evidence are kept in `docs/worklog/`.
