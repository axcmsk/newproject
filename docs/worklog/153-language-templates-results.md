# Language starter implementation evidence

Specification: `docs/worklog/151-language-templates-task.md` at
`032d6174b504bef1463e4abc1abf826417225c56`. Specification review:
`docs/worklog/152-language-templates-spec-review.md` at
`4f64160f36cfeaf70f22b4f5be7f4e723c4db058`, accepted subject to C1. The
literal README correction closing C1 is at
`683d122000b9023065d591a685245851cbff0ef1`. Implementation inputs and this
report are in the same checkpoint commit.

- `make check`: passed 75 tests, exit 0; output and status retained at
  `/tmp/newproject-language-implementation-check.log`. The new tests cover both
  languages with and without heavy, argument order and repetition, syntax and
  help, source isolation and refusals, layer and helper collisions, Git state,
  and real payload bytes and modes. Existing tests cover neutral generation and
  helper behavior. `python3 -m unittest discover -s tests -p test_newproject.py -v`
  also passed the focused suite before its last two helper collision cases.
- `make test-coverage`: passed, exit 0; output and text report at
  `/tmp/newproject-language-coverage.log`, machine-readable report at
  `/private/tmp/newproject-language-templates/coverage.json`, and HTML at
  `/private/tmp/newproject-language-templates/htmlcov/index.html`. These are
  from the implementation inputs in this checkpoint. The report shows 96% for
  newproject.py and 95% total; percentages alone are not acceptance criteria.
- Real Python starter in `/tmp/newproject-language-smoke/starter`: generated
  with `python3 .../source/newproject.py --lang python starter`. With a minimal
  module and test, `make format PYTHON_PATHS='example.py tests'` failed on dirty
  formatting (status 2), and `cmp` confirmed source unchanged (status 0); see
  `/tmp/newproject-language-smoke/dirty.log` and `dirty-status.log`. `make
  reformat PYTHON_PATHS='example.py tests'`, `make check PYTHON_PATHS='example.py
  tests'`, and `make test-coverage` then passed; their logs are `reformat.log`,
  `check.log`, and `coverage.log` in that directory. Coverage JSON and HTML
  were produced in the temporary starter. No dependencies were installed.
- Real Go payload files were checked byte-for-byte and mode-for-mode against
  `examples/go/` by the tests. Its unchanged recipes were not network-tested
  again; the prior Go template evidence remains in task 139.

Environment: Python 3.9.6, Git 2.54.0, Coverage.py 7.10.7, GNU Make 3.81,
macOS arm64. Other platforms were not exercised. No actual sibling project was
created; all generated projects used temporary fixture roots.
