# Go tool file dependency

HUMAN explicitly approved replacing the phony tools recipe's executable test
with a Make file dependency. HUMAN subsequently approved including the version in the binary filename,
with installation into a temporary directory followed by a rename. Changing
the pinned version therefore selects a new file dependency and installs it
when missing. Older versions remain available. An existing non-executable file is considered present by Make
and may fail on invocation rather than being replaced.

Baseline: `8fde45560feba1d3c3cc8a3c68f51c7402c5fe81`,
`examples/go/Makefile`, `tests/test_go_makefile.py`, `README.md`, and approved
contract `docs/worklog/133-go-makefile-task.md`. The versioned filename and existence semantics
above supersede the previous contract; all other behavior stays unchanged.

Make the tool path a non-phony file target. `format`, `lint`, `reformat` and
phony `tools` depend on that file target. Keep check as the default target,
shared parallel installation, quoted invocation and support for tool directory
paths containing spaces. Remove the redundant shell existence conditional;
keep installation failure propagation and successful-install validation.
Use `$(HOME)/go/bin/golangci-lint-$(GOLANGCI_LINT_VERSION)` by default, keeping
the optional TOOLS_DIR override. Install with the existing official installer
into a unique temporary directory, verify the resulting executable, then move
it to the versioned destination only on success. Clean up temporary files on
success/failure. Preserve an existing unversioned binary and other versions.
A failed installation must not leave the versioned destination appearing ready.
Do not add stamps, runtime version checks, new targets or tools.

LEAD owns this specification and README. DEVELOPER owns Makefile, focused
changes to tests/test_go_makefile.py, and docs/worklog/139-go-file-target-results.md.
REVIEWER owns docs/worklog/138-go-file-target-spec-review.md and
docs/worklog/140-go-file-target-review.md. Use existing role assignments/models.
Work only in /private/tmp/newproject-go-makefile; preserve original root .idea.
LEAD releases prepared README/spec paths for developer checkpoint commits.
DISPATCHER routes approved spec and checked implementation as in PROCESS.

Checks: configured `make check` plus focused regression coverage for missing
tool installation, existing-file reuse, accepted non-executable behavior,
version changes selecting a new binary while retaining old versions,
preservation of an existing unversioned binary, installation failure cleanup
and absence of a false-ready versioned destination, parallel invocation,
and paths with spaces. Retain existing regression coverage. Isolated fake
downloads suffice for this dependency-only change: installer and formatter
commands are unchanged, with real-tool evidence at baseline 135/136.
No real home writes or generator changes. Also exercise the revised real
installation path into an isolated temporary TOOLS_DIR, checking resulting
filename and executable version, repeat reuse, and temporary staging cleanup.
The network download is authorized for this verification.
Checkpoint before independent review, commit report after review, return
accepted changes to original task branch without merging main or pushing.
