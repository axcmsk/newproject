# Go Makefile template

## Goal and sources

HUMAN requested a Go Makefile with everything in the Python Makefile and
automatic installation of missing tools into `~/go/bin`. The preceding
conversation approved golangci-lint standard plus bodyclose, durationcheck,
errorlint, nilnesserr, noctx, nolintlint and revive; preserve all revive defaults
and add early-return and identical-branches. nolintlint requires a specific
linter and explanation.

Baseline: `3fed10ba88da4fa29fd10a997b26e03fac600f35`, root `Makefile`,
`docs/specs/make-checks.md`, `README.md`, and governing workflow documents.
Deliver a separately copyable template at `examples/go/`; do not change the
generator or common templates. Root Python checks remain unchanged.
HUMAN confirmed: keep it separate for now; change the generator later.

## Contract

- Supply `examples/go/Makefile` and `.golangci.yml`, usable when copied into an
  existing Go module. GNU Make 3.81 and POSIX shell on macOS/Linux are supported.
- Preserve default/check, format, lint, test, reformat targets and ordinary
  Make failure/output semantics. `check` depends on format, lint, test in that
  order; explicit parallel Make may run independent checks concurrently.
- `format` checks without writing sources, reports formatting differences and
  fails for them or tool errors. `reformat` applies only formatting. Configure
  gofmt and goimports. Both use the same scope, excluding dependency/vendor
  trees according to documented golangci-lint behavior.
- `lint` runs the approved configuration without fixes. `test` runs
  `go test ./...`. Do not add race, coverage, build, tidy or automatic lint fixes.
- Add `tools` for explicit installation. format/lint/reformat also ensure the
  external executable exists. test alone does not download the linter.
- Default executable location is exactly `$(HOME)/go/bin/golangci-lint`, not
  GOPATH or PATH discovery. An optional directory override supports isolated
  tests. Use a quoted path when invoking tools. Existing executable is reused;
  do not auto-upgrade or overwrite it. An incompatible executable may fail
  clearly when invoked; document removal/replacement as explicit user action.
- When missing, install a pinned official binary release (initially v2.15.0)
  with the upstream installer, checking download and installation failures.
  Do not hide curl failure in a pipeline. No successful target after failed
  installation. One make -j invocation must not race its own installation.
  Separate concurrent Make invocations need not be coordinated.
- Go, Make and curl are prerequisites, not automatically installed. Download
  requires network access. Go dependency/cache downloads remain normal Go
  behavior. No changes to shell startup files or global Go configuration.
- Support normal invocation from module root and `make -C` from elsewhere.
  Template copying is manual; no generator CLI or generated project changes.

## Ownership and routing

LEAD owns this task specification and root README documentation. DEVELOPER owns
`examples/go/Makefile`, `examples/go/.golangci.yml`, focused tests in
`tests/test_go_makefile.py`, and `docs/worklog/135-go-makefile-results.md`.
REVIEWER owns `docs/worklog/134-go-makefile-spec-review.md` and
`docs/worklog/136-go-makefile-review.md`. DISPATCHER routes approved work and
evidence. Use role models from LEAD. No other writes; preserve untracked `.idea/`.

LEAD sends the checked specification commit to REVIEWER, then releases its exact
approved version to DISPATCHER. Developer implements, checks, checkpoints;
reviewer performs independent static acceptance. No push or merge requested.

## Verification and acceptance

DEVELOPER runs configured `make check`, with focused regression tests integrated
in unittest discovery. Cover targets/commands, default/check order, explicit
parallel installation sharing, existing executable reuse, absent-tool install,
download/install failures, test not installing lint tools, formatting differences
and formatter errors returning failure without mutation, reformat mutation on a
fixture, lint/test failures, and invocation through make -C. Mock downloads in
automated tests, with isolated directory overrides; never replace real HOME.
Use real golangci-lint to validate configuration and run the template against a
temporary Go module, checking bad formatting then reformat/check. Record any
network/environment limitation honestly. Retain exact commands, checked source,
results and meaningful failure evidence. Do not install tools in the user's
home merely for tests; use a temporary tools directory. Report source diffs and
independent verdict before closeout.

## Documentation sources

- https://golangci-lint.run/docs/welcome/install/local/
- https://golangci-lint.run/docs/configuration/cli/
- https://golangci-lint.run/docs/linters/configuration/

Read on 2026-11-13. Upstream recommends binary installation. Its fmt --diff
prints differences; implementation must ensure a dirty format check fails.

## Specification checkpoint evidence

DEVELOPER ran `make check` with README and this specification present: exit 0,
60 tests; raw output `/tmp/newproject-133-spec-make-check.log`. The subsequent
user-scope confirmation and this evidence paragraph change no check inputs.
