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
and commit-message guides. The generator copies `tools/agents/merge.py` and
`tools/agents/review_commit.py` into each project from their single sources in this
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

## Go check template

For an existing Go module, copy `examples/go/Makefile` and
`examples/go/.golangci.yml` into its root. These optional files are not installed
by the project generator. They require Go, GNU Make and, for the first tool
download, curl and network access on macOS/Linux.

Run `make` or `make check` for formatting verification, lint and `go test ./...`.
Individual targets are `format`, `lint`, `test`, and `reformat`; formatting is
checked without editing files, while `reformat` applies gofmt and goimports.
Use `make reformat && make check` to apply formatting and then verify everything.
From elsewhere, use `make -C /path/to/go-project check`.

`make tools` installs the missing golangci-lint version into `~/go/bin`, named
`golangci-lint-v2.15.0` for the current pin. Formatting and lint targets also
install it automatically when absent; `test` does not. Changing
`GOLANGCI_LINT_VERSION` in the Makefile selects and installs the new version.
Existing versions and an unversioned binary are preserved; old versions can be
removed manually when no longer needed.
The tool directory path must not contain spaces.

The template downloads a pinned official binary release into a temporary
directory, verifies installation, and moves the executable to its versioned
path. Adding `~/go/bin` to PATH is unnecessary. An existing destination file
without execute permission is not reinstalled and fails when invoked. Go itself
must already be installed; normal Go commands may download module dependencies
and write caches.

The configuration preserves standard golangci-lint and revive checks, adds
the selected error/resource checks, and requires explanations for lint
suppressions. See the [template contract](docs/worklog/133-go-makefile-task.md).

## Repository development

To commit assigned review reports from the repository root:

```sh
python3 tools/agents/review_commit.py --head FULL_HASH -m "review: description" docs/worklog/NNN-review.md
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

Development requires Make in addition to Python, Git, and Ruff.
Run all checks from the repository root:

```sh
make check
```

The default target (`make`) also runs the formatting check, lint, and tests.
Ordinary Make execution stops on failure and shows the tools' output without a
custom summary. With explicit `-j`, independent checks may run concurrently;
`make -k check` continues independent checks after an error and still fails overall.
From another directory, use `make -C /path/to/newproject check`.
This Makefile is specific to this repository and is not installed in generated
projects. See the [check contract](docs/specs/make-checks.md).

For diagnosis, select one check:

```sh
make format
make lint
make test
```

`format` checks formatting without changing sources. To apply formatting, then
run all checks:

```sh
make reformat && make check
```

`reformat` changes source formatting and runs no other checks. Inspect any edits;
partial edits remain if formatting fails. Individual targets do not replace the
full checks required before commit and review. Tests use temporary directories,
not real sibling projects.
