# Simplify workflow wording

Before editing: shorten the requested example to “For example, correcting
spelling in explanatory documentation.” Review common rules and templates for
repetition and contradictions introduced by the direct route. Keep AGENTS as
scope authority, PROCESS as route authority, and PROJECT-RULES as Git/check
policy authority. Replace duplicated details with references where useful.
Clarify worker-only handoff instructions and delegated-only routing; use
implementer where direct LEAD is also allowed. Preserve all three routes,
nonbehavioral exemption, instructions-as-implementation principle, independent
review, check/coverage/evidence/commit boundaries and existing heavy overrides.

Baseline: 3bee347b7998513eb67f14e35d843d0206bd731d, root/base AGENTS and workflow
rules, README coverage instructions, heavy extension (read-only consistency).
Allowed edits: root/base AGENTS, PROCESS, PROJECT-RULES, LEAD/REVIEWER guides,
README and matching template coverage prose if necessary; this record and
report 163-workflow-cleanup-review.md. No executable, test, CV or data-process
changes. LEAD owns edits and checks; independent REVIEWER Astra/high owns only
report 163. Required checks: make check, diff and policy/link consistency review.
Acceptance: requested concise example, fewer repeated rules, no changed authority
or removed requirements, root/base alignment, checks and independent review pass.
Stop at local commits, no push.

## Evidence

`make check` passed (exit 0): Ruff format/lint and 75 tests. Checked inputs:
baseline plus the eleven policy/prose files in this checkpoint. Raw output:
`/tmp/workflow-cleanup-checks.log`. `git diff --check` and root/base parity checks
passed, preserving the root PROJECT-RULES purpose section. New links resolve to
existing route/check/Git sections. Static inspection included remaining role
guides and the heavy extension, which retains its explicit overrides.

Removed route duplication from AGENTS/LEAD, duplicate Git ownership prose from
PROCESS and repeated check ownership/reuse prose from PROJECT-RULES. The example
now appears only in PROCESS. Clarified worker handoffs, delegated review routing
and README coverage ownership to avoid implying mandatory DEVELOPER/DISPATCHER
on the direct route. Corrected grammatical agreement in the review exemption.
No review or check requirement was intentionally changed.

REVIEWER uses the existing clean worktree and owns only report 163; LEAD imports
its released report commit. Unrelated `.idea/` remains untouched.
