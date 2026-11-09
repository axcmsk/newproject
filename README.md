# New project

Create a project with agent rules, role guides and an empty Git repository.
Requires Python 3.9+ and Git; no Python packages are needed to run the generator.

## Usage

From this repository:

```sh
python3 newproject.py my-project
python3 newproject.py --heavy my-long-project
python3 newproject.py --help
```

Each project is created beside this repository, on `main`, without an initial
commit. Pass a single directory name; quote names containing spaces. Existing
nonempty projects are not overwritten. A failed creation may leave partial files;
follow the error message before retrying.

Fill in the generated README and record project decisions in
`docs/workflow/PROJECT-RULES.md`.

## Variants

- **Normal:** roles, independent review and Git checkpoints. Feature branches
  are optional.
- **Heavy:** adds required task branches, a live checkpoint, allowance limits,
  an event journal and its writer. Journal append requires macOS/Linux or another
  platform with POSIX file locking.

Both variants include the [merge procedure](template/base/docs/workflow/MERGE.md)
and commit-message guides. The generator copies `tools/merge.py` and
`tools/review_commit.py` into each project from their single sources in this
repository. Both variants include the
[report commit procedure](template/base/docs/workflow/REVIEW-COMMIT.md).

Shared files live in `template/base/`; heavy additions live in `template/heavy/`.
During heavy generation, `AGENTS.add.md` is appended to `AGENTS.md`.
Editing these templates affects only future projects.

Details: [normal rules](template/base/AGENTS.md),
[heavy workflow](template/heavy/docs/workflow/HEAVY.md),
[limits](template/heavy/docs/workflow/LIMITS.md),
[journal usage](template/heavy/docs/workflow/work-log-format.md),
[generator specification](docs/specs/newproject.md).

Optional personal preferences live beside this repository in
`common/DIALOGUE.md` and `common/EDITING.md`; they are not copied into projects.

## Development

To commit assigned review reports from the repository root:

```sh
python3 tools/review_commit.py --head FULL_HASH -m "review: description" docs/worklog/NNN-review.md
```

Use the full commit ID recorded at review start and exact report paths. Hold
exclusive writer ownership and complete required checks beforehand. The helper
checks HEAD and permitted changes, then commits the reports with normal Git
hooks. On failure, inspect the state before retrying: the index may be staged
or a commit may already exist. See the [contract](docs/specs/review-commit.md).
Reviewers follow the [report commit procedure](docs/workflow/REVIEW-COMMIT.md).

Install Ruff once:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install ruff==0.17.3
```

Run all checks with one command:

```sh
python3 tools/python_check.py
```

It runs the formatting check, lint and tests sequentially, shows every result,
and exits nonzero if any check fails or cannot start. Ordinary failures do not
skip later checks; interrupting the command stops the sequence. The helper finds
this repository from its own location, so it also works from another directory.
It is specific to this repository and is not installed in generated projects.
See the [check helper contract](docs/specs/python-check.md).

To apply formatting first, then run lint and tests:

```sh
python3 tools/python_check.py --reformat
```

This mode changes source formatting. It uses the same paths and applies
formatting instead of checking it; no second formatting check runs afterward.
Formatting errors still make the overall command fail, even if lint and tests
pass. Any formatting edits remain available for inspection.

For diagnosis, select one check:

```sh
python3 tools/python_check.py --only format
python3 tools/python_check.py --only lint
python3 tools/python_check.py --only tests
```

To apply formatting alone:

```sh
python3 tools/python_check.py --only format --reformat
```

`--reformat` can accompany `--only format`; it is incompatible with selecting
lint or tests alone. Individual checks do not replace the full checks required
before commit and review. Tests use temporary directories, not real sibling projects.
