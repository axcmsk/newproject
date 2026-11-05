# Task and review process

[AGENTS](../../AGENTS.md#scope) defines which changes need this process.
Role guides define responsibilities; [LEAD](roles/LEAD.md#model-settings)
holds the model settings. Read the sections needed for your assigned work.

## Task inputs and contexts

Use separate, bounded worker contexts without the full HUMAN conversation or
unrelated history. Give each worker its role guide and required inputs.

LEAD writes a complete task specification: goal, scope, inputs and sources,
constraints, allowed changes, deliverables, required checks and acceptance
criteria. Include material decisions and their reasons. Pin sources to a
commit and path or another fixed snapshot; a mutable path alone is not enough.
DEVELOPER and REVIEWER use the same specification and its required sources.

LEAD also supplies operational instructions: exact specification reference,
review reference when available, assigned roles and settings, agreed steps,
allowed writes, expected reports, and what to do next or return to LEAD.
DISPATCHER reads these instructions and forwards the specification reference
unchanged. It need not read or summarize the substantive specification.

REVIEWER checks the specification against its source requirements, as well as
implementation against the specification. Ask for missing context when needed.
LEAD may cite a specific HUMAN decision in reply. Put binding clarifications
back into the specification for all workers. HUMAN has final authority, but a
HUMAN decision does not prove technical correctness. Record accepted risks as
risk acceptance, not technical approval.

## Short route for small tasks

Use this route for clear, bounded documentation or behavior-preserving
mechanical changes with focused checks and no unresolved design decision.
Changes to application behavior, schema/data, security/authority, concurrency,
recovery or runtime follow the standard route below. Role and process documents
use the documentation route, including review of any authority changes before
those changes are relied on. Direct content work under
AGENTS remains exempt; no route waives required checks or permissions.

LEAD gives one short assignment: goal, baseline, allowed changes, required
inputs/checks and stopping point, with routing fields included. No separate
start, handoff or completion document is needed unless it adds a decision or
limitation not recorded elsewhere.

- For documentation, LEAD prepares the frozen diff and REVIEWER checks it.
  When committing is authorized, commit the accepted documents and review together. No delegated DEVELOPER is needed for document authoring. Before committing,
  run the configured checks required by PROJECT-RULES, even for documentation.
  Complete these checks before sending the frozen documents to REVIEWER.
- For mechanical code changes, each role prepares its own files. Freeze source and related documents before decisive checks using a saved
  snapshot with content hashes. DEVELOPER saves the required
  results and proof that behavior is preserved, including affected callers.
  REVIEWER checks that source and its saved results. Results need not be
  committed before review; combine them with the accepted review at closeout.

For uncommitted review inputs, name the base commit, exact paths and Git blob
IDs or a saved patch. Keep them fixed during review; save each reviewed version
and verdict before replacing it, including failed rounds. Recheck affected
edits, not identical content merely because it was committed.

When committing is authorized, a writer may commit exact files prepared and released by other roles without
editing them or including unrelated work. Combine related records at normal
handoffs; preserve urgent blockers and recovery information when needed.
Commit counts are not quotas.

## Work and review

Use this standard route when the short route does not apply.

1. LEAD writes the specification and sends it directly to REVIEWER.
2. REVIEWER sends all specification findings, questions and verdicts directly
   to LEAD. LEAD revises the specification and returns the affected version
   for review. REVIEWER does not write a separate developer assignment.
3. LEAD releases the exact approved version, or a version covered by explicit
   review conditions, to DISPATCHER. DISPATCHER starts dependent work only
   after all applicable review conditions are met.
4. DEVELOPER implements only the assigned scope and supplies changed files,
   the tested source version, exact commands, outcomes, relevant failure output
   and remaining limitations.
5. After all configured checks pass on the frozen version, DISPATCHER sends
   that version and saved results to REVIEWER. REVIEWER reviews independently of
   the developer's self-checks. DEVELOPER fixes implementation findings and
   reruns the relevant checks without fresh LEAD permission for each fix.
   Keep required reviews, frozen inputs and execution permissions. Changes to
   requirements, scope or permitted effects return to LEAD and review.
6. DISPATCHER reports completion to LEAD only when acceptance conditions pass
   and blocking findings are resolved. Include the result, review references,
   check evidence and limitations. Report a blocker without claiming completion.
7. LEAD assesses suitability and reports the outcome to HUMAN. LEAD resolves
   substantive questions within HUMAN's instructions or asks HUMAN for a
   needed decision. Stay within the authorized scope; acceptance does not
   authorize a later stage or publication.

### Checks and verdicts

For logic work, only DEVELOPER runs tests, builds, validators, linters and
other executable checks. CI may run the agreed checks. REVIEWER reads
requirements, code, tests, fixtures, assertions, diffs and saved results; it
does not execute project code, rerun checks or trigger CI. Assess requirement
coverage, missing edge cases, meaningful assertions and whether tests detect
relevant failures. Request missing checks from DEVELOPER through DISPATCHER.
Distinguish reported results from
conclusions reached by static review.

Each review names the exact reviewed specification and source version,
covered scope, findings, limitations, verdict and next owner/action.
Findings include a location, consequence and a verifiable closure condition.
Optional stylistic preferences do not block acceptance. Use these verdicts:

- `ACCEPTED`: the named scope passes review.
- `CHANGES_REQUESTED`: the assigned author must resolve the listed findings.
- `BLOCKED`: a decision, required input or evidence is missing.
- `ACCEPTED_SUBJECT_TO_CHECKS`: acceptance is pending the explicit conditions.

A missing verdict, mismatched source, unclear evidence condition or unexpected
result returns to REVIEWER. Routing, requirements, scope or authority questions
go to LEAD. Do not infer approval from silence or narrative.
Record findings and decisions in the task's review document.

### Conditional acceptance

REVIEWER may list exact checks for DEVELOPER to run on unchanged reviewed code,
or exact non-executable wording corrections for the document's author to make.
Name the base version, files, literal changes or checks, and permission for
closure without another review. For each condition, give an ID, saved evidence
location (file and field or line), expected value or marker and any matching
rule. Include source identities and meaningful assertions/final-state results,
not just a wrapper exit code. Mark conditions that only REVIEWER may close.

DISPATCHER may close a condition only when all named comparisons match.
Read only the named evidence locations. Do not assess sufficiency, interpret
warnings, accept substitute evidence or choose another check. Missing evidence,
changed code, a mismatch or an unexpected result stops closure and returns to
REVIEWER. REVIEWER resolves evidence questions and sends requirements, scope
or authority decisions to LEAD. DISPATCHER never judges a semantic difference
harmless.

Keep the reviewed inputs fixed while review is running. For permitted literal
corrections, retain the reviewed base, complete allowed change list, exact
corrected version and closure evidence. The acceptance record links all four;
it does not claim the corrected version was separately reviewed.

Other changes to a task specification or its behavioral sources require
review of the affected revision, including editorial changes not explicitly
covered by a conditional verdict. Resolve blocking findings before dependent
work. No extra HUMAN confirmation is needed for routine work already authorized.
