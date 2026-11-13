# Language starter templates

## Goal and source requirements

HUMAN approved `--lang go` and `--lang python` as starter-file selection.
Both Makefiles are intended to be adapted to the eventual project. No language
argument keeps the current neutral project; `--heavy` remains independent.
Generation only copies files, with no tool installation or guessed code layout.

Baseline `de0423e34d7073e25fbbeafa40f05839d73c6665`: `newproject.py`,
`docs/specs/newproject.md`, `README.md`, `template/base/`, `template/heavy/`,
`examples/go/`, root `Makefile`, `ruff.toml`, `.coveragerc`,
`tests/test_newproject.py`, `tests/test_go_makefile.py`, and current workflow.
Coverage added by the other chat is part of this baseline and must be retained.

## Contract and scope

- Add argparse `--lang` with choices `go` and `python`, default absent. It may
  appear before/after NAME, independently of --heavy. Preserve normal argparse
  last-value behavior for repeated --lang. Invalid/missing values exit 2 before
  mutation. Help works without template/language sources or Git.
- Keep `examples/go/` as the sole Go payload source. Add `examples/python/`
  as the Python payload source. Copy selected payload contents to project root,
  preserving bytes/modes, including hidden files, with no examples wrapper.
  Do not duplicate Go files into another template directory.
- Validate only the selected language: missing or malformed unselected sources
  cannot affect neutral or another-language generation. For a selected language,
  examples and its selected language directory must be real directories; apply
  the existing nonempty layer, symlink/special/.git rejection rules to payloads.
- Compose base, optional heavy, then optional language as additive layers.
  Merge shared directories, reject file/file and file/directory collisions
  across every selected layer before target mutation. Preserve heavy AGENTS
  composition and workflow-helper reserved paths. Language payload must not
  override AGENTS or workflow helper paths. Existing target, Git and exclusive
  copy safeguards remain unchanged; no automatic rollback.
- Neutral generation retains byte-for-byte existing payload behavior and does
  not require examples/. No generated source code, go.mod, pyproject metadata,
  dependency installation, tool execution, commits or remote operations.
- Go payload retains current Makefile and .golangci.yml behavior, including
  versioned tools, plain file dependency and test-coverage. Add .gitignore for
  /coverage/ and a docs/LANGUAGE.md guide (no base README collision).
- Python payload supplies Makefile, ruff.toml, .coveragerc, .gitignore and
  docs/LANGUAGE.md. Use current root check/format/lint/test/reformat and
  test-coverage conventions, replacing repository-specific target paths with
  `PYTHON_PATHS ?= .` and `TEST_DIR ?= tests`. Keep python3 unittest test command
  and .venv Ruff/coverage tooling. Do not auto-install Python dependencies.
  Guide gives setup with pinned Ruff 0.17.3 and coverage 7.10.7, clearly marking
  paths and rules as defaults to adapt before using the targets.
- Python coverage measures source `.` and omits tests and .venv. Retain
  subprocess collection and fresh erase/run/combine/report/html/json workflow,
  absolute COVERAGE_FILE/RCFILE. Do not copy root aliases or file-specific
  include patterns. Coverage remains optional and not in check; ignore caches,
  .venv, coverage data, coverage.json and htmlcov. No percentage gate.
- Python Ruff defaults follow root rules and Python 3.9 baseline; adapt prose
  that refers specifically to this repository. Do not change root checks or
  root coverage behavior for this feature. Existing Go tests must keep passing.
- Root README and generated common README explain language selection and
  adapting a starter; docs/LANGUAGE.md provides setup details when selected.
  Neutral README must not have a broken link to an absent language guide.

## Ownership and routing

LEAD owns this task, docs/specs/newproject.md, README.md, template/base/README.md,
and both examples/{go,python}/docs/LANGUAGE.md guides. DEVELOPER owns
newproject.py, examples/python/{Makefile,ruff.toml,.coveragerc,.gitignore},
examples/go/.gitignore, tests/test_newproject.py, any focused new tests under
tests/, and docs/worklog/153-language-templates-results.md. README/spec/guide
files are released for exact checkpoint commits when LEAD says so.
REVIEWER owns 152-language-templates-spec-review.md and
154-language-templates-review.md under docs/worklog. DISPATCHER routes approved
specification to existing DEVELOPER and exact checked source to REVIEWER.
Use role models specified by LEAD guide. Work only in
/private/tmp/newproject-language-templates. Preserve original .idea and other
chats' worktrees. No push, main merge or changes to coverage development scope.

## Verification

DEVELOPER runs configured make check and make test-coverage, retaining exact
source identity, commands, outcomes and coverage.json for static review.
Use temporary fixtures only, never actual sibling projects. Cover both
languages with/without heavy; CLI ordering, invalid/missing/repeated lang,
help independent of sources; neutral unchanged; selected source refusals and
unselected source independence; all-layer collisions including helper paths;
exact payload content/modes, main/unborn/unstaged output, cwd independence.
Retain existing generator safety and real-template/helper tests.

Exercise Python starter targets against a temporary minimal module/tests with
available real Ruff/coverage, overriding paths where needed; confirm read-only
format failure, reformat, lint/test, coverage JSON+HTML, no root-specific path
requirements. Do not recursively invoke repository tests from unit fixtures.
Inspect generated Go payload against its canonical source; unchanged Go recipes
need no repeated network installation. Document source limitations honestly.
Checkpoint tested source, obtain independent static acceptance, commit review.
