# Go target simplification

Baseline: `dc0b49fcf0cff42b0e9674598e4b085f023ac6ef`. HUMAN directed that
space-containing tool directories need not be supported; this supersedes that
requirement in tasks 133 and 137. LEAD assigned the mechanical removal of the
Make escaping variables, retaining the directory override, quoted shell paths,
installer, version and formatting behavior. README now states the constraint.

`make check` passed all 69 tests, exit 0; raw output and status are retained at
`/tmp/newproject-141-make-check.log`. The nine existing focused Go Makefile
regressions use a tool directory without spaces and retain their other checks.
The previous real installer evidence in task 139 remains applicable to the
unchanged installation recipe; no network download was performed for this
mechanical change.
