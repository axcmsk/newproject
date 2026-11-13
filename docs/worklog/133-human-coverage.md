# Optional coverage report for HUMAN

## Specification

Baseline: `3fed10ba88da4fa29fd10a997b26e03fac600f35`.
Sources at baseline: Makefile, README development section,
docs/specs/make-checks.md, .gitignore, tests/*.py and the four production scripts.
HUMAN asked to add `test-coverage` if inexpensive and clarified that this is for
HUMAN, not an agent/reviewer acceptance mechanism.

Add a separate phony `make test-coverage` target. Run the existing unittest suite
under coverage.py, print per-file coverage with missing lines, and generate an
HTML report at `htmlcov/index.html`. Measure the production scripts (newproject,
merge, review_commit, work_log), including Python subprocesses and temporary
copies executed by existing tests. Consolidate copied paths into their canonical
repository files. Exclude test/framework code from the human report.

Use standard coverage.py commands and declarative configuration; no custom
collector, shell program, test framework migration, product instrumentation or
test rewrites for measurement. Use pinned coverage 7.10.7 (supports Python 3.9)
as an optional development dependency. Existing dependency setup remains valid.
If correct collection needs substantially more machinery, report that limitation
instead of expanding the task. No coverage percentage threshold. The final handoff requirement below applies. `make check` and `make test` remain unchanged and need no coverage package.

Start each report run with fresh measurement data; store data outside temporary
test repositories so Git state assertions remain meaningful. Ignore measurement
data and HTML output. Do not silently accept test failures or missing tools.
Document installation, invocation, report location, subprocess collection, and
the distinction between measured execution and correctness. Generated projects receive no coverage tooling. Shared PROCESS guidance receives the coverage handoff requirement below. No network service or publication of reports.

HUMAN's final clarification: coverage belongs in the implementation handoff to
review. Where coverage is configured, DEVELOPER runs it and supplies the report
for the reviewed source; REVIEWER inspects it statically. Update root/base PROCESS
handoff requirements without granting REVIEWER runtime authority. Coverage values
are evidence, not a percentage gate. Projects without configured coverage acquire
no new tooling obligation. This supersedes the earlier discussion of optional
REVIEWER execution. Role/process changes receive independent static review.

## Ownership and routing

LEAD owns this specification, README, docs/specs/make-checks.md and root/base
PROCESS. Review the concrete handoff changes with this spec.
Standard route: REVIEWER Astra/high reviews this spec first (report 134);
DISPATCHER Luna/low then delegates implementation to DEVELOPER Terra/medium.
DEVELOPER owns Makefile, .coveragerc, .gitignore, and report
docs/worklog/135-human-coverage-results.md. Developer may commit exact released
LEAD docs without editing them. Final REVIEWER report is 136. Work only in
/private/tmp/newproject-test-coverage, branch codex/test-coverage. No merge/push.

## Acceptance and checks

Run configured `make check`, then `make test-coverage`. Record timings to show
incremental runtime cost and report line coverage for each production script.
Confirm all four canonical scripts appear with meaningful executed lines from
subprocesses, no duplicated temporary copies and no test files in the report.
Inspect HTML output for source/missing-line usability. Verify fresh-data handling
and failure propagation with bounded fixtures or command inspection as appropriate.
Existing tests must remain unchanged and pass; no tests mirroring Make recipes.
Save results and source identity; commit checked inputs before independent review.

Sources for coverage behavior:
https://coverage.readthedocs.io/en/7.10.7/config.html
https://coverage.readthedocs.io/en/7.10.7/

## Specification review closure evidence

- Reviewed base: `ea890c7392c4bfc5f743582fed543de6f96c8195`.
- Checked inputs: reviewed base plus the two exact PROCESS insertions in review 134 condition C1; executable inputs unchanged.
- Command: `make check`.
- Formatting: PASS.
- Lint: PASS.
- Tests: 60 passed.
- Overall exit: 0.
