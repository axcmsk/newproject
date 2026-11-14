# Unified task routes

Before editing, LEAD records the agreed outcome: replace the overlapping short
and direct routes with three choices, independent of file type:

1. Obvious correction without behavior or meaning/requirement/authority changes:
   edit and check, no task specification or independent reviewer required.
2. Clearly easier for LEAD to implement than explain to DEVELOPER: record a few
   lines of intended result and acceptance/checks before implementation; no
   separate specification file required. LEAD implements and runs checks;
   independent REVIEWER reviews the brief and result together.
3. Delegation: full specification and existing standard route. If direct work
   proves unsuitable, transfer brief, changes, findings and evidence, expand
   the specification as needed and transfer ownership explicitly.

Preserve existing routine content exemption, independent review for changes to
behavior/rules, check/evidence/coverage/commit/permission obligations. Align
root and base AGENTS, PROCESS, PROJECT-RULES and LEAD guide. No special data
process or provision, no CV changes, no code or test changes. HUMAN explicitly
withdrew the earlier data-process provision. Baseline: `bc98622522cfbf168ab5796d09256139c83d0bde`, these same policy files. Earlier requests in this chat
are superseded by these decisions where inconsistent.

LEAD owns these policy edits; independent REVIEWER Astra/high owns only report
159-unified-routes-review.md. Required checks: make check and static consistency
and diff inspection. Stop at local checked changes and reviewed report; no push.

## Evidence

`make check` passed (exit 0): Ruff format/lint and 75 unittest tests.
Checked inputs: baseline plus the eight policy files in this task’s checkpoint;
no executable code changes. Raw output: `/tmp/unified-routes-checks.log`.
`git diff --check` passed. Static inspection: no stale short-route references;
root/base AGENTS, PROCESS and LEAD match. PROJECT-RULES shares the same route
wording and retains existing project-specific differences.

Review uses the existing isolated worktree to preserve unrelated `.idea/`
content in the original checkout. REVIEWER owns only report 159 there;
LEAD brings the released report commit back after review.
