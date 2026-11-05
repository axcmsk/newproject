# Standard CLI parsing

HUMAN approved moving newproject.py to standard-library argparse and clarified
that dash-prefixed names need no bespoke support, but must not be separately
banned. Replace the manual parser; keep standard -h/--help, -- termination,
option errors and boolean flag behavior. Repeated --heavy is accepted normally,
not rejected by custom machinery. Retain name/path domain validation and all
creation safeguards. No template, journal, dependency or unrelated changes.

Baseline c08f743aa6c553fe59fd5b0384049b26106f9fb6 on codex/heavy-template.
Sources: docs/specs/newproject.md revised in this specification commit;
newproject.py, tests/test_newproject.py and README.md at baseline; current root
AGENTS and docs/workflow. Use standard route because CLI behavior changes.
LEAD owns spec/README; REVIEWER gpt-6-astra/high reviews spec directly with LEAD,
then implementation/results via DISPATCHER gpt-6-luna/low. DEVELOPER
 gpt-6.1-terra/medium owns code/tests and executable checks.

Allowed developer writes: newproject.py, tests/test_newproject.py,
docs/worklog/033-argparse-implementation.md. Reviewer may write only assigned
032-argparse-spec-review.md or 034-argparse-review.md. One writer; no source edits
by reviewer. Commit checked code before implementation review; preserve reports.
Stop after accepted local commits, no merge/push. No separate branch required
for this continuation of the generator changes on the current branch.

Acceptance: concise argparse parser; both normal/heavy creation preserved;
-h/--help exits 0 with useful NAME/--heavy usage even without source trees/Git;
missing NAME, extra positional values and unknown options exit 2 without mutation;
standard -- lets an otherwise valid dash-prefixed name pass domain validation;
no custom dash-name support or prohibition. Update tests expecting old parser
errors and duplicate-flag refusal. Keep focused real CLI assertions and all
existing creation/journal regression tests. Do not pin Python-version-dependent
error prose beyond stable relevant facts.

Required checks (DEVELOPER):
- python3 -m unittest discover -s tests -v
- .venv/bin/python -m ruff check newproject.py tests template/heavy/scripts
- .venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts

Before this specification checkpoint, these exact commands passed on unchanged
code/tests/configuration during the preceding README edit: 25 tests, Ruff lint
and formatting (4 files unchanged). The baseline includes that README-only commit.
Current edits are spec/README/task text only, so those results remain applicable.
No implementation starts before independent spec acceptance and LEAD release.
