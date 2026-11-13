# Go tool file dependency evidence

Specification: `docs/worklog/137-go-file-target-task.md` at
`2b804f95fa038c53ac7934cdc423d937ad6ec18f`. Tested implementation inputs are
`examples/go/Makefile` and `tests/test_go_makefile.py` in this commit.

- `python3 -m unittest discover -s tests -p test_go_makefile.py -v`: passed all
  nine focused tests. They cover installation, reuse, parallel prerequisites,
  tool directory paths containing spaces, version changes preserving older and
  unversioned files, a non-executable existing file, and failed download,
  installer, and non-executable staged output leaving no destination or staging
  residue. Existing formatting, lint and test cases remain covered.
- `make check`: passed all 69 tests, exit 0. Output and status are retained in
  `/tmp/newproject-139-make-check.log`.
- Real installation on darwin/arm64 with GNU Make 3.81 and Go 1.26.2:
  `make -C examples/go 'TOOLS_DIR=/tmp/newproject-139-real/tools with spaces' tools`
  passed with the official installer; raw output and status are in
  `/tmp/newproject-139-real/install.log`. Running the installed binary with
  `version` reported golangci-lint 2.15.0. Repeating the same make command
  returned 0 and reported nothing to be done. The directory listing contained
  only `golangci-lint-v2.15.0`, confirming staging cleanup. These results are
  saved in `/tmp/newproject-139-real/reuse.log`. No user-home tool was changed.

The real installation covers this host architecture; other platforms use the
same official installer but were not independently exercised here.
