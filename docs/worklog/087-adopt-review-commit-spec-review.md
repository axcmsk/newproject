# Review helper adoption specification review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`27177ed212635cd19fa5bd0ecb704b0caffc9af9`, on `codex/adopt-review-commit`.
Baseline: `cad01efe53ed47950a54ea101e0195dd228756cd`.
The index and working tree were clean at review start. REVIEWER owns only
`docs/worklog/087-adopt-review-commit-spec-review.md`.

## Scope and conclusions

Static review covers task 086, the revised project-creation and report-helper
specifications, all changed root/base workflow instructions and READMEs, and
the heavy operational-write exception. Required sources include AGENTS,
PROJECT-RULES, PROCESS, REVIEWER and BRANCH-MESSAGE. LEAD supplied the HUMAN
decision to adopt the helper in root instructions and generated projects in one
outcome branch. No blocking findings.

The REVIEW-COMMIT procedure preserves assigned-report-only ownership, the pinned
review-start HEAD, prior check requirements, normal hooks, separate source/report
identities and release of ownership. Its failure instructions prohibit blind
retry, discarding state and manual bypass. The REVIEWER/PROCESS changes authorize
only this administrative execution; they do not grant test or general runtime
authority. The unchanged helper sources are not reimplemented by this task.

The changed PROCESS, REVIEW-COMMIT, LEAD and REVIEWER files have identical Git
blob identities in root and base. Referenced workflow documents exist at their
root/base paths; the heavy REVIEW-COMMIT link resolves through the composed base
layer. README wording agrees with the intended completed installation.

Heavy retains its existing operational-write permission and report-only commit
boundary. Its explicit manual override applies only to permitted operational
changes outside pinned inputs, with exact report staging, sole-parent/diff/index
verification and unstaged operational changes. Other dirt and unexpected helper
refusals do not qualify. A clean heavy review uses the shared helper. This is
a narrow compatibility rule rather than a general manual fallback.

The generator contract identifies exactly the two root helper sources, preserves
bytes/modes, requires source and selected-layer collision checks before mutation,
and retains exclusive creation and partial-failure preservation. Help and parser
errors remain independent of helper availability. Required tests exercise both
installed helpers and variants, unrelated-dirt refusal, source failures,
collisions, copy protection and exclusion of unrelated tools. Existing tests
remain required. No existing-project update, dependency change, initial commit
or helper execution during generation is authorized.

## Check evidence and limits

Task 086 records 53 passing unittest cases, passing configured Ruff lint and
format checks (eight files), and the checked baseline executable/template input
scope. LEAD confirmed that `git diff --cached --check` passed on the exact staged
checkpoint inputs immediately before creating `27177ed`; the sequential command
completed with exit code 0 (LEAD tool response chunk `14f368`). This clarification
records an already performed check and changes no requirement.

These are saved or LEAD-reported results, not REVIEWER executions. No project
code, tests, validators or report helper were run during this review. The generator
implementation is still pending and is not accepted by this verdict. Adding
only this report does not change checked inputs.

## Handoff

This initial policy review uses baseline report-commit authority and direct Git;
it does not rely on the execution exception under review. After committing only
this report directly atop the recorded HEAD, REVIEWER releases writer ownership
to LEAD. LEAD may release the exact approved checkpoint to DISPATCHER for the
implementation defined in task 086. Return the report commit separately from
the approved source identity; integration remains subject to implementation
checks and independent acceptance.
