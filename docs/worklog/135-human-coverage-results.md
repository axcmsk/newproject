# Human coverage implementation results

Specification: `docs/worklog/133-human-coverage.md` at
`ea890c7392c4bfc5f743582fed543de6f96c8195`, with the corrections at
`0e2f8fd688d9da2497c9e1dd875a139f0f9d4061` covered by review 134 conditions.
Checked source: that corrected commit plus this implementation's Makefile,
.coveragerc and .gitignore changes; the final commit identifies these inputs.
Existing tests and production scripts were unchanged. Python environment used
ruff 0.17.3 and coverage.py 7.10.7.

- `make check`: PASS, formatting and lint passed, 60 tests passed in 26.122 s;
  total wall time 26.25 s.
- `make test-coverage`: PASS, 60 tests passed in 43.225 s; total wall time
  43.96 s. Compared with the ordinary test portion, measurement added 17.103 s
  (about 65%); the total comparison adds 17.71 s. This is a local single-run
  measurement, not a benchmark guarantee.
- Terminal line coverage: `newproject.py` 96% (7 missing statements),
  `tools/agents/merge.py` 97% (3), `tools/agents/review_commit.py` 95% (8),
  `template/heavy/scripts/workflow/work_log.py` 93% (15); total 95%.
  Percentages describe execution, not correctness or an acceptance threshold.
- HTML report: `/private/tmp/newproject-test-coverage/htmlcov/index.html`.
  Inspection of the index found exactly the four canonical source links;
  inspection of the source page found numbered source lines marked as executed
  or missing. `coverage debug data` showed exactly those four canonical paths;
  existing tests invoke the scripts via subprocess and temporary copies.
- Command inspection: `coverage erase` precedes each run and removes the data
  file and parallel data files; the absolute data path keeps data outside test
  repositories. Make executes each recipe line separately and stops on a
  nonzero result, so a missing tool or failed tests prevents report commands.
  The first attempted run demonstrated propagation: tests passed but report
  exited nonzero on unmapped temporary paths and Make stopped before HTML.
  Directory path aliases corrected that issue in the successful run above.
- `git diff --check`: PASS. Generated `.coverage` and `htmlcov/` are ignored.

Raw output is retained locally at `/private/tmp/coverage-check.log` and
`/private/tmp/coverage-run.log`. Reports are local generated artifacts and are
not committed or published. Independent review remains pending.
