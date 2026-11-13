# Go coverage target

Baseline: `4ab7fe19f5f0ba1102750a57699d18a599d8df23`.
Sources at baseline: examples/go/Makefile, examples/go/.golangci.yml,
tests/test_go_makefile.py, README Go check template section, root Makefile.
HUMAN requests `test-coverage` for the Go Makefile already on main. Preserve the
separate pending Python coverage branch; do not merge unrelated work here.

## Required outcome

Add a phony standalone `test-coverage` target to examples/go/Makefile. Use only
installed Go tools and simple shell commands: run the existing package scope
`./...` with a coverage profile, show per-function/total statement coverage,
and generate local HTML for HUMAN. Keep the native Go profile as the
machine-readable artifact for inspection. No JSON converter, dependencies,
custom collector, coverage percentage gate, or change to check/test/linter setup.

Place outputs in `coverage/`: `coverage.out`, `functions.txt`, `index.html`.
Start each attempt without stale versions of these three generated files;
remove only those named artifacts, preserve unrelated files in the directory.
A failing test or report command must fail Make and stop dependent report steps.
Do not install golangci-lint for coverage. Do not automatically open a browser.
Document normal Go package coverage scope, outputs, invocation from another cwd,
and that percentages measure executed statements rather than correctness.
Document adding `/coverage/` to the consuming project's .gitignore; do not
replace its existing ignore configuration or add generator payloads.

## Ownership and routing

LEAD owns this assignment and README usage text. Standard PROCESS route:
REVIEWER Astra/high reviews specification (report 144); DISPATCHER Luna/low
then delegates to DEVELOPER Terra/medium. Developer owns examples/go/Makefile,
tests/test_go_makefile.py and docs/worklog/145-go-coverage-results.md. Developer
may commit exact released README without editing it. Final static review report
146. Work only in /private/tmp/newproject-go-test-coverage, branch
codex/go-test-coverage. No merge/push. Do not edit historical Go specifications.

## Validation

Run repository `make check`. Extend existing bounded template tests to cover
coverage execution without tool installation and failure propagation/stale
artifact cleanup (including a later report failure). Exercise the real copied
Makefile in a temporary small Go module with covered and uncovered statements,
without external dependencies, and validate profile, text totals and usable HTML.
Run from another cwd with `make -C`; ensure existing targets keep their behavior.
Capture Go version, commands, outcomes, runtime and sample coverage in evidence.
No test framework or permanent Go module in this repository. Use temporary caches
if needed; do not weaken coverage or skip the real-Go verification silently.
Commit checked inputs and evidence before independent static review.

Official reference: https://pkg.go.dev/cmd/cover
