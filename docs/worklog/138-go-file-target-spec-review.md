# Versioned Go tool dependency specification review

## Identity and scope

- Reviewed source and frozen HEAD: `2b804f95fa038c53ac7934cdc423d937ad6ec18f`.
- Reviewed paths: `docs/worklog/137-go-file-target-task.md` and `README.md`.
- Required baseline: `8fde45560feba1d3c3cc8a3c68f51c7402c5fe81`,
  `examples/go/Makefile`, `tests/test_go_makefile.py`, `README.md`, and
  `docs/worklog/133-go-makefile-task.md`.
- Sole report path: `docs/worklog/138-go-file-target-spec-review.md`.
- Worktree: `/private/tmp/newproject-go-makefile`, initially clean.
- Method: independent static review; no executable project checks were run.

## Assessment

The latest explicit HUMAN decision, recorded in the specification and relayed
by LEAD, authorizes both the versioned filename and temporary installation.
It supersedes the earlier manual-delete-on-version-change proposal, which was
held without a review verdict. The reviewed contract makes a changed version
select a different file target while retaining existing versions and an
unversioned binary. An existing non-executable destination is explicitly
accepted as present, with invocation failure rather than automatic replacement.

The requested non-phony binary target and shared dependencies preserve default
check behavior and single installation within one parallel Make invocation.
The contract retains quoted paths, directories with spaces, GNU Make 3.81,
ordinary error propagation, and test-only independence through its unchanged
baseline requirements. Installation must validate staging before publishing
the destination, clean temporary files, and avoid a false-ready target on
failure. Those requirements provide a verifiable boundary for file-target
semantics. No new runtime version check, stamp or generator feature is added.

Focused mocked regression coverage is required for the changed dependency and
failure behavior. The later explicit real-install requirement additionally
covers the revised staging/publish path, selected version, reuse and cleanup;
the sentence allowing fake downloads does not waive that separate real check.
Existing formatter evidence remains applicable because its behavior is not
being changed. README describes the new filename and lifecycle consistently.

## Check evidence and limitations

Read `/tmp/newproject-137-spec-check.log`: formatting passed for nine files,
lint passed, and 67 tests passed with recorded exit status 0. DEVELOPER and
LEAD confirmed that the checked executable inputs did not change in the
subsequent specification/README revision, so those results remain applicable.
These are saved DEVELOPER results, not checks rerun by REVIEWER.

Implementation details, path escaping, staging failure handling and required
new test results remain subject to the subsequent implementation review.

## Findings and verdict

No blocking findings.

Verdict: `ACCEPTED` for the specification and README at
`2b804f95fa038c53ac7934cdc423d937ad6ec18f`.
Next owner: LEAD releases this exact approved version to DISPATCHER; DEVELOPER
implements and supplies the required check evidence. No push or main merge is
authorized by this verdict.
