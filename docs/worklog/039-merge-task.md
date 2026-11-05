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
