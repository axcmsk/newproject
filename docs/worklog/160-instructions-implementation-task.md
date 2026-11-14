# Agent instructions as implementation

Before editing: promote the established commit-rule principle into root/base
AGENTS Scope: code and agent instructions are implementation; assess changes by
behavioral effect regardless of file format. MAIN-MESSAGE should reference that
shared principle. Clarify the obvious-correction example in AGENTS and PROCESS
as spelling in explanatory text without changing behavior or meaning; punctuation,
file extension or calling a change a typo does not itself justify exemption.
Preserve existing review and check obligations and the three routes.

Baseline: 47ca65588e2ea4372bd5d2333c071bee16514793, AGENTS.md and
`docs/workflow/{PROCESS,MAIN-MESSAGE,PROJECT-RULES}.md`, base equivalents.
Allowed writes: root/base AGENTS, PROCESS, MAIN-MESSAGE, this record and report
161-instructions-implementation-review.md. No CV, data-process, code or test
changes. LEAD owns policy edits and make check; independent REVIEWER Astra/high
owns only report 161. Acceptance: explicit shared principle, valid reference,
accurate nonbehavioral example, aligned root/base policy, passed configured
checks and independent static review. Stop at local commits; no push.

## Evidence

`make check` passed (exit 0): Ruff format/lint and 75 tests. Checked inputs:
baseline plus the six policy files in this checkpoint. Raw log:
`/tmp/instructions-implementation-checks.log`. `git diff --check` passed.
Each changed root policy matches its base counterpart; the relative link to
AGENTS Scope resolves in both trees. No executable source changed.
Review takes place in the clean existing review worktree, preserving unrelated
untracked `.idea/` in the original checkout. LEAD imports only the released
report commit after review.
