# Heavy workflow extension

This project was created with the heavy workflow. Apply the normal
[PROCESS](PROCESS.md), [PROJECT-RULES](PROJECT-RULES.md) and role guides, plus
this extension. The additions below override only the named base provisions;
all other role boundaries, checks and acceptance conditions remain in force.
Explicit HUMAN decisions and higher-priority environment instructions prevail.

## Reading and ownership

All roles read this file and [LIMITS](LIMITS.md) before substantive work, on
resumption and when the policy changes; reuse unchanged inputs in an active
context. Role model settings remain in the base LEAD guide.

- LEAD reads all [STATE](STATE.md) and [TASK-CONTEXT](TASK-CONTEXT.md), owns
  substantive decisions and checkpoint cleanup, and supplies bounded contracts.
- DISPATCHER reads STATE's operational block, TASK-CONTEXT's routing and review
  fields, and [work-log-format](work-log-format.md). It maintains that block and
  the journal under the exclusive writer ownership already required by PROCESS.
- DEVELOPER and REVIEWER read TASK-CONTEXT and their pinned assignment and
  required sources. LEAD includes relevant STATE constraints in the assignment;
  workers need not reconstruct requirements from checkpoint history.

DISPATCHER may run `python3 scripts/workflow/work_log.py append`, `schema` and
`append --help` solely for journal work. This is a narrow exception to the base
execution boundary: it grants no test, validator, code-edit or general runtime
authority. DEVELOPER maintains and tests the tool. REVIEWER remains static-only.

## Task branches and checkpoints

This section replaces the normal optional-branch policy. Use a separate
`codex/<task>` feature branch for each new task or cycle. A newly generated
repository has an unborn main: make one checked bootstrap commit before creating
the first task branch. Bootstrap establishes the reviewed template and initial
project facts; substantive changes to requirements or policy still need review.

Keep main at accepted boundaries and follow [MERGE](MERGE.md) for integration.

## Live checkpoint and recovery

STATE is the sole live checkpoint, not a requirements source. DISPATCHER edits
only the block delimited by `operational-status:start` and `operational-status:end`.
LEAD owns the remainder. Both respect one-writer ownership. Record task/branch,
exact contract/source/review references, owner and next action, blockers, writer
and runtime ownership, sessions/resources, authority, stage baseline and latest
allowance sample references. Never invent observations or successful outcomes.

Update on material transitions: ownership, scope/authority, blockers, session
start/end, parking/resumption or limit boundaries. Combine coincident updates;
unchanged polling does not need a write or commit. Before dependent work, the
checkpoint must identify the accepted contract and permitted action.

On resumption, reconcile relevant Git state, retained sessions and resource
identity with the checkpoint. A saved stopped state is not a live inspection.
Do not start duplicate operations or reset uncertain resources. Preserve handles
and explicit unknowns until their outcomes are established.

LEAD cleans substantive STATE at stage completion when needed, or when it is
stale, bloated or contradictory. Preserve every live constraint in its authoritative
home; retain unresolved gates, permissions, sessions and next action in STATE.
Replace old detail with exact report or commit/path references before removing it.
Do not rewrite historical evidence or reset finding counts. No cosmetic cleanup
campaign or separate checkpoint copy is required at each handoff.

## Operational writes during review

At review start, LEAD may permit DISPATCHER to update STATE's operational block
and the journal outside the pinned inputs, naming their exact paths and allowed
scope in the assignment. This extends the base report-only
working-tree allowance, not REVIEWER's commit contents. Keep HEAD and reviewed
inputs fixed until review completes. Defer substantive STATE edits until release.

DISPATCHER releases writer ownership before REVIEWER writes and commits its
report. Verify allowed paths and block boundaries; operational changes must stay
unstaged and outside the report commit. Investigate unexpected changes without
discarding work.

Follow [REVIEW-COMMIT](REVIEW-COMMIT.md#operational-changes), passing a separate
`--allow-dirty PATH` for each assigned operational file. Check STATE block
boundaries and journal rules yourself; the helper checks file preservation and
report isolation. Without operational changes, use the helper without this option.
Apply the base source/report commit checks, then return ownership
to DISPATCHER for operational closeout. Operational records are outside source
acceptance and are committed separately from source and review reports.

For pinned or unlisted operational paths, buffer facts outside the repository
until release. Report urgent blockers and notify REVIEWER of facts affecting
scope or authority immediately.

## Assignments, journal and stops

Use [TASK-CONTEXT](TASK-CONTEXT.md) in the existing assignment and review, not as
a mandate for extra documents. Send pinned requirements unchanged. Keep the same
worker and reviewer for bounded corrections when practical; replacement contexts
inherit findings, budgets and ownership. Missing operational authority goes to
LEAD; evidence interpretation goes to REVIEWER.

DISPATCHER records meaningful transitions, checks, blockers and budget samples
in the append-only journal using its [format rules](work-log-format.md). Workers
supply compact facts at ordinary handoffs. The journal replaces neither STATE
nor raw verification evidence. No polling transcript, automatic monitoring,
extra delegation solely for logging or compulsory efficiency report is required.

Apply LIMITS independently of acceptance and resource safety. Stop affected work
on a limit, unknown required allowance, repeated blocker or unresolved authority.
Preserve a safe continuation; do not run extra checks merely to finish. A successful
gate needs no repeated HUMAN consent within an already authorized scope.

## Verification evidence and resources

In addition to normal evidence, retain exact source and command/arguments,
tool/runtime versions, available start/end/duration, stdout/stderr, individual
exit/status metadata, meaningful assertions and skipped-check reasons. Preserve
full execution-tool responses and session handles needed to establish terminality.
Keep failure diagnostics and uncertainty. Sanitize secrets and private data;
record any resulting evidentiary limitation rather than retaining credentials.
Commit evidence after the run at the relevant closeout boundary. Evidence and
operational records may be grouped together; REVIEWER commits its report separately.

Before an expensive full sequence, review changed code and assertions using
focused evidence. Run the mandatory cumulative sequence on ready, fixed source;
repeat only affected checks after narrow corrections unless the contract or a
concrete integration risk requires the full sequence. The base check-before-commit
rule remains applicable; additional execution gates must be explicit in the
reviewed task contract and cannot waive configured precommit checks.

For containers, databases or retained fixtures, the task must identify authorized
resources, one runtime owner, setup and cleanup boundaries, required identity and
final-state observations, and storage footprint plus headroom. Check free space
on the actual backing filesystem before setup. Worktrees do not isolate a shared
runtime. This template grants no permission over production, historical or
unrelated data, nor any blanket fixture-reset or deletion authority.

At creation, record each disposable resource's exact identity, owner, purpose
and cleanup scope. Review cleanup with setup/verification. Before authorized
cleanup, recheck identity, terminality and consumers (including stopped ones),
and preserve required evidence. Never use global prune, name-prefix-only selection
or force deletion. Retained resources need a reason, owner and release condition;
logs alone do not justify indefinite fixture retention. Preserve active or
uncertain resources until resolved, and report skipped cleanup explicitly.
