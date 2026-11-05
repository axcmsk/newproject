# New project

Create a new project with shared agent rules, role guides and a Git repository.
The script composes starter files from `template/base/` and, when requested,
`template/heavy/`.

## Quick start

Requires Python 3.9 or newer and Git on PATH. No Python packages are required.
From this repository run:

```sh
python3 newproject.py my-project
python3 newproject.py --heavy my-long-project
```

This creates `../my-project/`, copies the template and initializes Git on `main`.
No initial commit is made. Open the new project's README and describe its purpose;
record project-specific decisions in `docs/workflow/PROJECT-RULES.md`.

From another directory, run the script using its absolute path. The destination
is always beside this repository, regardless of the current working directory.
Pass exactly one directory name, without path separators. Quote names containing
spaces; names beginning with a dash are accepted directly, except the reserved
`--heavy` flag. Use `-- --heavy` for that literal name. The flag may precede or
follow NAME; use `--heavy -- NAME` when the heavy project name resembles a flag.

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

`template/base/` supplies the shared files for both variants:

- `AGENTS.md`: agent entry point, communication rules and process scope.
- `docs/workflow/PROJECT-RULES.md`: project configuration and general rules.
- `docs/workflow/PROCESS.md`: task routes, reviews and acceptance.
- `docs/workflow/roles/`: LEAD, DISPATCHER, DEVELOPER and REVIEWER guides.
- `README.md`: a minimal project entry point to fill in.

Normal projects use bounded assignments, independent review, Git checkpoints
and proportionate evidence. Feature branches are optional.

With `--heavy`, `template/heavy/` adds STATE, LIMITS, task routing fields, fuller
execution/resource rules, an empty event journal and its Python writer. The
`AGENTS.add.md` fragment is appended to the generated AGENTS.md and is not copied
as a separate file. No common files are duplicated or overridden. Any other
file collision is rejected before creating the project. Generated projects are
standalone; their agents follow explicit instructions rather than probing for
optional workflow files.

Heavy projects require task branches and retain reviewed commits. After the
initial checked bootstrap commit on main, create `codex/<task>` for work. Merge
accepted changes with `--no-ff` only when authorized; no squash or history rewrite.
Default limits: park at 30% weekly allowance remaining, stop at 25%, and stop for
assessment after a 15-percentage-point decline within one stage. Unknown allowance
pauses substantive work until measured or explicitly overridden. Only HUMAN can
change standing limits; repeated failure on the same blocker escalates after
three rounds.

In a generated heavy project:

```sh
python3 scripts/workflow/work_log.py schema
python3 scripts/workflow/work_log.py append --help
```

DISPATCHER appends actual events under exclusive writer ownership. The writer
uses the installed project's `docs/workflow/work-log.jsonl` by default, regardless
of working directory. It preserves history and refuses duplicates/malformed tails.
Append requires POSIX `fcntl.flock` (macOS/Linux); unsupported platforms refuse
append, while schema/help remain available. No third-party packages are required.

Edit the appropriate source layer to change defaults for future projects.
Existing projects are not updated by the script. Heavy grants no inherited
permission over production data, host resources or unrelated fixtures.

## Agent rules

See [AGENTS.md](template/base/AGENTS.md) for the default workflow and
[the LEAD guide](template/base/docs/workflow/roles/LEAD.md) for roles and model settings.

Optional personal preferences are read from sibling `common/DIALOGUE.md` and
`common/EDITING.md` when present; these files are not copied into the project.

## Testing

Run the test suite from this repository:

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary directories and isolated Git settings, including real Git
checks and injected failures. They do not create projects beside this repository.

For lint and formatting checks, install Ruff in a local environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install ruff==0.17.3
.venv/bin/python -m ruff check newproject.py tests template/heavy/scripts
.venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts
```

To apply formatting:

```sh
.venv/bin/python -m ruff format newproject.py tests template/heavy/scripts
```

Ruff is only needed for development; the script uses the Python standard library.
