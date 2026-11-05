# Draft merge helper

HUMAN asked to develop the agreed helper in a branch for later LEAD handoff.
Baseline 99c70534b3344c94e1d012f0a0f8ea02c1a32bd0; branch codex/merge-script.
Contract: docs/specs/merge.md in this commit. Existing root workflow and
newproject.py/tests/ruff.toml at baseline provide process/style/check conventions.
This authorizes development and isolated test merges, not merging this branch,
rewriting reviewed project history, pushing or installing the helper in templates.

LEAD owns spec and brief/user docs. Standard route: REVIEWER gpt-6-astra/high
reviews specification directly with LEAD and commits report 040-merge-spec-review.md;
LEAD releases accepted contract to DISPATCHER gpt-6-luna/low; it forwards unchanged
to DEVELOPER gpt-6.1-terra/medium. Developer owns only merge.py, tests/test_merge.py
and 041-merge-implementation.md, with exclusive writer/runtime during implementation.
Reviewer owns only assigned review reports (042-merge-review.md for implementation),
commits them using review: after exact HEAD/report-boundary verification, then
releases writer. Ordinary fixes follow the same roles; material scope returns LEAD.
No other repository code, configuration, template or workflow changes are in scope.

Required checks: python3 -m unittest discover -s tests -v;
.venv/bin/python -m ruff check merge.py newproject.py tests template/heavy/scripts;
.venv/bin/python -m ruff format --check merge.py newproject.py tests template/heavy/scripts.
Developer may format/refactor its own files to meet existing rules. No blanket
lint disables, new dependencies or generic transaction machinery. Preserve real
Git semantics, useful errors and partial-state visibility. Stop after a tested,
independently reviewed draft branch and compact handoff, without adopting it as
a repository-wide workflow tool.

Pre-spec checkpoint evidence: prior LEAD checks on unchanged executable inputs
passed 26 tests, existing expanded Ruff lint and formatting (4 files). Current
changes are this brief and the new specification only, so results remain valid.
Expanded checks including merge.py are required after implementation.

## HUMAN interface correction

Target is fixed to main in one top-level constant, not a CLI operand. A repository
using master may change that constant manually; no discovery/default/extra option
is requested. The caller still checks out the target before invocation. Use the
revised docs/specs/merge.md in this amendment commit; all other semantics remain.
Developer paused before committing; unfinished new files are retained outside the
repository for safe review of the amendment and will be restored unchanged after
release. Only three preliminary focused tests had run, not acceptance checks.
Amendment review: docs/worklog/043-merge-main-spec-review.md. Existing configured
check inputs remain unchanged; prior passing results still apply to this docs-only
checkpoint. The implementation still requires all expanded checks.
