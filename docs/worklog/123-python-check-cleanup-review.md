# Python check cleanup: review

Verdict: `ACCEPTED`.

Reviewed source and initial HEAD:
`fd27d39911649f70a2b37b2945eee745b805ede0`, on `codex/check-helper`.
Baseline: `fec52b31596e411a716266ac2d11aa8d121d0234`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/123-python-check-cleanup-review.md`.

## Scope and conclusions

Static short-route review covers the four assigned cleanup items in
`tools/python_check.py` and `tests/test_python_check.py`, evidence 122 and the
LEAD-released specification edit. No blocking findings.

All command-target assertions now use a separate literal `EXPECTED_TARGETS`
instead of the helper's own constant, so an accidental helper target change can
fail the tests. The expected list matches the specification. Only the unused
temporary virtual-environment symlink setup is removed; the bounded subprocess
substitution still invokes the repository's actual Ruff interpreter on the
temporary fixture, while preventing recursive suite execution. The formatted
content assertion remains.

All fake argv program names now use `python_check.py`. The helper docstring
correctly lists format, lint and tests in execution order. These wording/test
changes introduce no runtime command or control-flow change.

The specification consolidates verification requirements without losing the
existing conditions: both modes, targets/cwd, CLI propagation, default
non-writing behavior, no redundant formatting check, each selection and flag
order, dependencies within tests, failures/launch errors, results/output,
interruption, parser refusals, real temporary-file formatting, no recursion and
final full reformat validation with all outcomes. Its checked identity matches
the LEAD-released identity recorded in evidence 122.

## Evidence and handoff

All three SHA-256 identities in `docs/worklog/122-python-check-cleanup.md` match
the reviewed helper, tests and specification. Saved results report the actual
`python3 tools/python_check.py --reformat` overall exit 0, format 0 (ten files
unchanged), lint 0 and tests 0 with 69 cases passing in 27.225s. Python 3.9.6,
Git 2.54.0 and Ruff 0.17.3 are recorded; working/staged whitespace checks passed.
The diff contains only the scoped source, specification and evidence files.

REVIEWER ran no project checks. Adding this report does not alter checked inputs.
Commit only this report using the accepted strict review helper and recorded
HEAD; verify the report-only direct child and clean repository state, then release
writer ownership to DISPATCHER. Return the report commit separately from the
accepted source identity. Leave all work on `codex/check-helper`, without merge
or push.
