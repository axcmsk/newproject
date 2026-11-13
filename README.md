# New project

Create a project with agent rules, role guides and an empty Git repository.
Requires Python 3.9+ and Git; no Python packages are needed to run the generator.

## Usage

From this repository:

```sh
python3 newproject.py my-project
python3 newproject.py --heavy my-long-project
python3 newproject.py --lang go my-service
python3 newproject.py --heavy --lang python my-script
python3 newproject.py --help
```

Each project is created beside this repository, on `main`, without an initial
commit. Pass a single directory name; quote names containing spaces. Existing
nonempty projects are not overwritten. A failed creation may leave partial files;
follow the error message before retrying.

Fill in the generated README and record project decisions in
`docs/workflow/PROJECT-RULES.md`.

`--lang go` or `--lang python` adds language-specific starter files from
`examples/go/` or `examples/python/`. Without it, the project stays neutral.
Language selection is independent of `--heavy`. The generator does not create
application code, choose a module name, install tools or run checks. Adapt the
Makefile and configuration to your layout; the generated `docs/LANGUAGE.md`
explains setup and defaults. Existing projects can also copy these starter files
manually, taking care to merge any existing configuration rather than overwrite it.

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

`--lang go` installs the starter files from `examples/go/`. For an existing Go
module, copy the files manually and merge its ignore rules. They require Go,
GNU Make and, for the first tool
download, curl and network access on macOS/Linux.

Run `make` or `make check` for formatting verification, lint and `go test ./...`.
Individual targets are `format`, `lint`, `test`, and `reformat`; formatting is
checked without editing files, while `reformat` applies gofmt and goimports.
Use `make reformat && make check` to apply formatting and then verify everything.
From elsewhere, use `make -C /path/to/go-project check`.

For a coverage report, run `make test-coverage` (or use `make -C` from another
location). It tests `./...` with Go's standard per-package coverage, prints
per-function and total statement coverage, and produces:

- `coverage/coverage.out`: the native Go coverage profile for tooling.
- `coverage/functions.txt`: the text summary for review.
- `coverage/index.html`: the source report to open in a browser.

Each attempt clears these three generated files before running; unrelated files
in that directory are preserved. Failed tests or report generation stop the
target with an error. Add `/coverage/` to your project's `.gitignore`.
The generated Go starter already includes this ignore rule.
This separate target uses only Go, does not install the linter, and is not part
of `make check`. No coverage percentage is required; coverage measures executed
statements, not correctness. For implementation review, DEVELOPER supplies the
measured source version and accessible paths to `coverage/functions.txt` and
`coverage/coverage.out`. REVIEWER reads the function summary and profile blocks
alongside code and tests; HTML is supplementary for browsing source.

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

## Optional Python coverage report

To inspect which production code the tests execute, install the optional tool:

```sh
.venv/bin/python -m pip install coverage==7.10.7
```

Then run:

```sh
make test-coverage
```

This runs the existing tests with coverage, prints coverage and missing lines,
and writes `coverage.json` for machine analysis plus a browsable report to
`htmlcov/index.html`. Open that file in a browser and select a source file to inspect uncovered lines. Each run starts with fresh
measurement data. Collection includes Python subprocesses and consolidates
copies of the scripts executed in temporary projects.

Coverage is an optional aid for inspection, not proof of correctness. There is
no percentage threshold; `make check` and `make test` do not require coverage.py.
For implementation review, DEVELOPER supplies the accessible report paths and
the measured source version. REVIEWER reads `coverage.json`, focusing on
per-file totals and missing lines alongside code and tests; HTML is supplementary
for browsing source. Report files stay local and are ignored by Git.
Neutral projects do not include a coverage target; the Python starter includes
an adaptable coverage target and documents its optional dependency.
