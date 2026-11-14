# Two routes, mandatory review

HUMAN requests removing the obvious-correction route and all related review
exemptions, retaining only direct LEAD implementation and delegation. On the
direct route, the original user request suffices if it makes the change and
verification clear; otherwise LEAD adds a few lines before work. No separate
specification document is required. Checks and independent review apply to both
routes, including content and typo corrections. Preserve existing report-commit,
conditional acceptance, coverage, ownership and permission procedures.

Baseline: df7d37c383d58eeaac10c28fb0c87af7ccd07aa5. Sources: root/base AGENTS,
PROCESS, PROJECT-RULES and LEAD guide; latest HUMAN decisions in this chat.
Allowed edits: these eight policy files, this record and independent report
165-two-routes-review.md. Inspect remaining active rules, README and heavy
extension for stale exemptions; preserve historical worklogs. No code, tests,
CV or data-process changes. LEAD owns edits/checks. REVIEWER Astra/high owns only
report 165. Acceptance: exactly two routes, no obvious/routine-content review
exemption, retained request usable by REVIEWER, root/base consistency, make
check and independent static review pass. Stop at local commits, no push.

## Evidence

`make check` passed (exit 0): Ruff format/lint and 75 tests. Checked inputs:
baseline plus the eight policy files in this checkpoint. Raw output:
`/tmp/two-routes-checks.log`. `git diff --check` and root/base parity passed.
Repeated scan of AGENTS, active workflow rules, README and templates found no
remaining obvious-correction/routine-content review exemptions or three-route
references. Existing conditional acceptance and report/operational procedures
remain intact; historical worklogs are not active instructions and were retained.
Final diff inspected for both routes, retained-request handoff and check evidence.

Review uses the existing clean worktree; REVIEWER owns only report 165 and LEAD
imports its released commit. Unrelated `.idea/` remains untouched.
