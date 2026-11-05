# Heavy assignment and review fields

Extend the normal [task inputs](PROCESS.md#task-inputs-and-contexts) in the existing
brief/specification. One handoff transfers work; it need not create a new file.
Use commit/path references and the same contract for author, executor and reviewer.
Do not require workers to reconstruct requirements from history.

## Routing card

LEAD supplies DISPATCHER:

- Task/stage, route, branch/baseline and exact contract/review references.
- Next role/action, requested model/effort from the base LEAD guide, and actual
  settings only when known.
- Dependencies explicitly ready/blocked, their authority references, allowed
  files/resources, exclusive writer/runtime owners and retained sessions.
- Current LIMITS revision, stage baseline/latest allowance sample references,
  original observation times, window/reset and any explicit scoped extension.
- Expected report, recipient, acceptance scope, excluded gates and stopping point.

DISPATCHER forwards the contract unchanged. Missing routing or authority goes
to LEAD. The substantive contract retains the base goal, scope, requirements,
checks, acceptance criteria and source/decision references; list all mandatory
inputs explicitly, including relevant retained STATE constraints.

## Review operational header

Start the existing review with:

- Verdict from PROCESS and exact reviewed contract/source commit and paths.
- Acceptance scope and excluded gates, findings and exact detail references.
- Next owner/action and whether a LEAD decision is needed (name the question).
- Conditions: none, or the complete comparisons required by
  [conditional acceptance](PROCESS.md#conditional-acceptance), including IDs,
  saved evidence field/line, expected values, matching rules, source identities,
  assertions/final-state evidence and reviewer-only closure conditions.

No new verdict or acceptance authority is introduced. Missing evidence, mismatches
or interpretive questions go to REVIEWER; operational authority goes to LEAD.
The header may not contradict the report or enlarge its scope. Preserve original
historical reports; add an explicit mapping when reusing older evidence.

## Checkpoint fields

DISPATCHER copies operational facts to STATE's marked block at material changes,
not the entire contract. LEAD maintains substantive constraints outside the block.
Use the lifecycle and recovery rules in [HEAVY](HEAVY.md#live-checkpoint-and-recovery).
