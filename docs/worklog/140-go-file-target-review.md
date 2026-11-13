# Versioned Go tool dependency implementation review

## Identity and scope

- Reviewed implementation and frozen HEAD:
  `de293ca2929a8d65801ea7172ec49ffd11fb23e9`.
- Approved specification: `docs/worklog/137-go-file-target-task.md` at
  `2b804f95fa038c53ac7934cdc423d937ad6ec18f`.
- Specification acceptance: `docs/worklog/138-go-file-target-spec-review.md`,
  commit `c51a221619844b4cc8a78659660fd2444e5eb28f`.
- Reviewed paths: `examples/go/Makefile`, `tests/test_go_makefile.py`,
  `docs/worklog/139-go-file-target-results.md`.
- Sole allowed report: `docs/worklog/140-go-file-target-review.md`.
- Worktree: `/private/tmp/newproject-go-makefile`, initially clean.
- Method: independent static review of requirements, changes, assertions and
  saved results. REVIEWER ran no project code or executable checks.

## Assessment

The binary filename includes the selected version. Its non-phony file target
is shared by format, lint, reformat and tools; check remains the default target
and test remains independent. Spaces are escaped in Make target/prerequisite
syntax, while actual shell paths remain quoted. Existing destination files,
including non-executable files, satisfy the Make dependency as explicitly
authorized. Changing the version selects a new destination and does not alter
older or unversioned binaries.

Installation creates a unique staging directory beneath TOOLS_DIR, so the final
move stays on the destination filesystem. Curl and installer failures exit
before publication. The staged executable is checked before the final move,
and the move's status is the recipe's result. The cleanup trap removes staging
on normal success and failure. The former shell existence conditional is gone;
there are no stamps, runtime version probes or automatic removal of old tools.
Formatter/linter/test commands remain unchanged.

Regression coverage retains prior target, ordering, reuse, parallel Make,
space-containing paths, formatting and failure tests. Added cases exercise
version selection with old/unversioned preservation and non-executable-file
reuse. Failed installer and invalid staged-output fixtures create partial
files, and assertions require both no versioned destination and no staging
residue. Those checks meaningfully cover the changed publication boundary.

## Saved evidence

Read `/tmp/newproject-139-make-check.log`: nine files pass formatting, lint
passes, and all 69 tests pass with recorded exit status 0, including all nine
focused Go Makefile tests. The developer evidence also records their separate
focused invocation. Source identity is the Makefile and tests in the reviewed
checkpoint.

Read `/tmp/newproject-139-real/install.log` and `reuse.log`. The documented
command `make -C examples/go 'TOOLS_DIR=/tmp/newproject-139-real/tools with spaces' tools`
installed v2.15.0 through the official installer into a unique staging path;
the saved installation status is 0. The installed binary reports 2.15.0.
Repeating tools reports nothing to do with status 0, and the final listing
contains only `golangci-lint-v2.15.0`, demonstrating staging cleanup. These are
DEVELOPER's saved executions, not a reviewer rerun.

Real execution covered darwin/arm64 with GNU Make 3.81 and Go 1.26.2. Other
platforms were not executed here. Coordination between separate concurrent
Make invocations remains outside the unchanged contract. No generator or
user-home tool change is included.

## Findings and verdict

No blocking findings.

Verdict: `ACCEPTED` for the implementation and evidence at
`de293ca2929a8d65801ea7172ec49ffd11fb23e9`.
Next owner: DISPATCHER returns this verdict and report commit to LEAD for
closeout. No push or merge into main is authorized by acceptance.
