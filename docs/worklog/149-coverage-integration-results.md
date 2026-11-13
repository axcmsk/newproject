# Coverage integration results

Specification: `docs/worklog/147-coverage-integration.md` at `f753825b22e09594091f2461935b950d9a9cecb3`, with review 148 at `341d590c6d50db11b1c5183815d4947ddca5dda2` and dispatcher-closed conditions. Baseline `4ab7fe19f5f0ba1102750a57699d18a599d8df23`; accepted Python tip `f98fe2aef3784361d547f717ff0c85ea70b401ad` (merge base `3fed10ba88da4fa29fd10a997b26e03fac600f35`); Go tip `67e5239cd9ad3a75f8fcb46b6024b0b3dd5acea0` (merge base baseline). Historical reports 133–136 and 143–146 are copied unchanged. The final commit identifies the checked integration and released LEAD documents. Existing production scripts are unchanged; measured Git blob identities are:

- `newproject.py`: `e924a99a4c0feead25accb316d44d95228a663f4`
- `template/heavy/scripts/workflow/work_log.py`: `c9c8d78f47c535f9c756d739d867eb562b7b2c2b`
- `tools/agents/merge.py`: `f61bc0538dba4a8223cfec6c91958e86234793d1`
- `tools/agents/review_commit.py`: `e11769dfdb2e7ce3aac988ea51853b732e9f2856`

Checks used coverage.py 7.10.7 from a temporary `.venv` symlink, removed after checks. `make check` passed formatting, lint and 70 tests (37.47 s wall). `make test-coverage` passed 70 tests (57.49 s wall) and produced all reports. Raw logs: `/private/tmp/coverage-integration-check.log` and `/private/tmp/coverage-integration-run.log`.

Python report for static review: `/private/tmp/newproject-coverage-integration/coverage.json`; supplementary HTML: `/private/tmp/newproject-coverage-integration/htmlcov/index.html`. The JSON and HTML per-file statement counts, missing counts and every missing line were compared programmatically; terminal totals and lines were also inspected. All agree:

| Source | Statements | Missing | Missing lines |
| --- | ---: | ---: | --- |
| newproject.py | 172 | 7 | 44, 88, 147, 148, 178, 183, 187 |
| template/heavy/scripts/workflow/work_log.py | 208 | 15 | 16, 17, 75, 76, 78, 100, 130, 167, 168, 180, 224, 258, 259, 271, 274 |
| tools/agents/merge.py | 87 | 3 | 59, 61, 101 |
| tools/agents/review_commit.py | 168 | 8 | 38, 40, 84, 92, 119, 207, 209, 247 |
| Total | 635 | 33 | 602 covered, 95% rounded |

`coverage debug data` listed exactly the four canonical paths, without tests or temporary duplicates. Coverage is evidence of execution, not a correctness threshold. A bounded copy of the Makefile with a stub coverage executable failed JSON with exit 23; Make returned 2 after calling erase, run, combine, report, html and json in order. Log: `/private/tmp/coverage-integration-failure.log`.

Real Go verification used `go version go1.26.2 darwin/arm64`, a temporary no-dependency module, and `PATH="/opt/homebrew/bin:$PATH" GOTOOLCHAIN=local GOPROXY=off GOCACHE="$fixture/cache" make -C "$fixture" test-coverage` from `/private/tmp`. It passed; Covered was 100%, Uncovered 0%, total 50%. Stale named outputs were replaced, unrelated `coverage/keep.txt` retained, and HTML contained the source. Source fixture and reports for static review: `/private/tmp/coverage-integration-go.3HzzNV/sample.go`, `/private/tmp/coverage-integration-go.3HzzNV/sample_test.go`, `/private/tmp/coverage-integration-go.3HzzNV/coverage/functions.txt`, `/private/tmp/coverage-integration-go.3HzzNV/coverage/coverage.out`, and supplementary `/private/tmp/coverage-integration-go.3HzzNV/coverage/index.html`. Log: `/private/tmp/coverage-integration-go.log`. Integrated Go Makefile blob `ba30792204f052015db9b54cc5281b7fbe487e3b`; test blob `9e85c131f80174a435faa679470565ace101bb39`. Root tests exercise Go failure propagation and tool preservation.

Inspected active documentation and coverage references, including root/base PROCESS and REVIEWER alignment; `git diff --check` passed. Reports are local generated artifacts, not committed or published. Independent implementation review remains pending.
