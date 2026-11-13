# Go tool file dependency

HUMAN explicitly approved replacing the phony tools recipe's executable test
with a Make file dependency. HUMAN accepts that changing the pinned version
does not reinstall an existing binary; update by removing it and running
`make tools`. An existing non-executable file is considered present by Make
and may fail on invocation rather than being replaced.

Baseline: `8fde45560feba1d3c3cc8a3c68f51c7402c5fe81`,
`examples/go/Makefile`, `tests/test_go_makefile.py`, `README.md`, and approved
contract `docs/worklog/133-go-makefile-task.md`. Only the existence semantics
above supersede the previous contract; all other behavior stays unchanged.

Make the tool path a non-phony file target. `format`, `lint`, `reformat` and
phony `tools` depend on that file target. Keep check as the default target,
shared parallel installation, quoted invocation and support for tool directory
paths containing spaces. Remove the redundant shell existence conditional;
keep installation failure propagation and successful-install validation.
Do not add stamps, version checks, automatic upgrades, new targets or tools.

LEAD owns this specification and README. DEVELOPER owns Makefile, focused
changes to tests/test_go_makefile.py, and docs/worklog/139-go-file-target-results.md.
REVIEWER owns docs/worklog/138-go-file-target-spec-review.md and
docs/worklog/140-go-file-target-review.md. Use existing role assignments/models.
Work only in /private/tmp/newproject-go-makefile; preserve original root .idea.
LEAD releases prepared README/spec paths for developer checkpoint commits.
DISPATCHER routes approved spec and checked implementation as in PROCESS.

Checks: configured `make check` plus focused regression coverage for missing
tool installation, existing-file reuse, accepted non-executable behavior,
version-edit reuse and explicit removal/reinstallation, parallel invocation,
and paths with spaces. Retain existing regression coverage. Isolated fake
downloads suffice for this dependency-only change: installer and formatter
commands are unchanged, with real-tool evidence at baseline 135/136.
No real home writes, network downloads or generator changes needed.
Checkpoint before independent review, commit report after review, return
accepted changes to original task branch without merging main or pushing.
