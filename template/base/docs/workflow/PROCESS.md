# Task and review process

[AGENTS](../../AGENTS.md#scope) defines which changes need this process.
Role guides define responsibilities; [LEAD](roles/LEAD.md#model-settings)
holds the model settings. Read the sections needed for your assigned work.

## Task inputs and contexts

Use separate, bounded worker contexts without the full HUMAN conversation or
unrelated history. Give each worker its role guide and required inputs.

For delegated work, LEAD writes a complete task specification: goal, scope,
inputs and sources, constraints, allowed changes, deliverables, required checks
and acceptance criteria. Include material decisions and their reasons. Pin sources to a
commit and path; a mutable path alone is not enough.
DEVELOPER and REVIEWER use the same specification and its required sources.
Direct implementation uses the brief defined below; obvious corrections need
no specification.

For worker handoffs, LEAD supplies operational instructions: exact specification reference,
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

## Shared ownership and authority

Allow one writer at a time for shared repository files and one runtime owner
for each shared execution environment, including across worktrees. Name owners
and allowed files/resources in the assignment; transfer ownership explicitly.
Read-only review may proceed while another role writes outside its pinned inputs.
REVIEWER writes and commits only its assigned reports under its
[report commit boundary](roles/REVIEWER.md#report-commits), and returns corrections
to the author.
No additional lease service or status file is required for an ordinary task.

The latest explicit HUMAN decision takes precedence over earlier requirements;
authorized specifications govern implementation. Summaries and historical reports
do not create new requirements. A review suggestion becomes binding only through
the authorized specification or a HUMAN decision. Resolve material conflicts
through LEAD; do not silently expand scope. Existing permission remains valid
within its stated scope, but successful checks do not authorize a later phase,
push, deployment or broader effects.

## Execution results and recovery

For each required check, retain the source identity, command, outcome and relevant
failure output, with evidence sufficient for its acceptance criteria. Capture
runtime/tool versions, raw output and final resource state when they matter to
reproduction or correctness; do not collect exhaustive logs by default or save
secrets. Mark skipped or unavailable checks explicitly.

Retain execution/session handles and tool status metadata until completion is
known. Empty output, a yield, a lost session or a vanished process is not proof
of success. Continue observing the same operation. If its outcome is uncertain,
stop dependent actions and reconcile its process and saved results before any
retry; never launch a duplicate or bypass a denied operation. Preserve enough
context to resume safely and report unresolved uncertainty.

After a correction, rerun affected checks. Repeat a full expensive sequence only
when the contract requires it or a concrete unresolved integration risk warrants
it. Do not weaken mandatory checks, and do not treat a new commit hash alone as
a reason to rerun unchanged checks.

## Choosing the route

LEAD chooses by the work involved, not by file type:

1. **Obvious correction without behavior changes:** make the correction and
   check it. No task specification or independent review is required, provided
   the correction does not change meaning, requirements, authority or process.
   For example, correcting spelling in explanatory documentation.
   Routine content exempt under AGENTS follows the same lightweight handling.
2. **Clearly easier to implement directly than explain to DEVELOPER:** record
   a brief assignment, implement, check and submit to independent REVIEWER.
   Use the direct route below.
3. **Delegation:** prepare a full task specification and use the standard
   work-and-review route below.

No route waives applicable checks, evidence, commits or permissions. Changes
that affect behavior or rules require independent review, including when they
appear in documentation. Role/process authority changes require review before
reliance on the new authority.

## Direct implementation by LEAD

Before implementation, LEAD records a few lines describing the intended change,
scope and how to verify the result. A separate specification document and
implementation details are not required. Keep the brief in an existing task
record or retained assignment, with source references sufficient for REVIEWER;
include it in the review handoff. This brief serves as the task specification
on this route. Resolve unclear requirements before dependent work.

LEAD owns implementation, checks, evidence and corrections, including the
coverage handoff in standard-route step 4 when configured. No delegated
DEVELOPER or DISPATCHER is required. References to DEVELOPER as implementer/check
owner and DISPATCHER as review router or conditional-closure owner apply to
LEAD, with the same limits.

After checks pass, LEAD commits the reviewable inputs and sends the exact brief,
source commit and saved evidence to independent REVIEWER. REVIEWER checks the
brief against its source requirements and the result against the brief together;
separate preliminary specification review is not required. Findings and the
committed report return directly to LEAD. LEAD resolves findings and submits
affected changes for review, preserving frozen inputs and prior reports.

If direct implementation turns out not to be clearly easier, LEAD transfers the
task to DEVELOPER. Pass the brief, current changes, findings and check evidence,
expand the brief into a full specification as needed, and explicitly transfer
writer/runtime ownership. Continue through the standard route, obtaining any
missing specification approval before dependent work resumes.

Follow PROJECT-RULES for [commits and ownership](PROJECT-RULES.md#git-workflow).
Combine related records at normal handoffs; avoid documents that merely repeat
existing information. Commit counts are not quotas.

## Work and review

Use this standard route for delegated implementation.

1. LEAD writes the specification, passes configured checks, commits it and
   sends that exact version directly to REVIEWER.
2. REVIEWER sends all specification findings, questions and verdicts directly
   to LEAD. LEAD revises the specification and returns the affected version
   for review. REVIEWER commits each completed report and returns its commit
   reference with the verdict. It does not write a separate developer assignment.
3. LEAD releases the exact approved version, or a version covered by explicit
   review conditions, to DISPATCHER. DISPATCHER starts dependent work only
   after all applicable review conditions are met.
4. DEVELOPER implements only the assigned scope and supplies changed files,
   the tested source version, exact commands, outcomes, relevant failure output
   and remaining limitations. When the project has configured coverage, include
   a coverage report for the reviewed source in the implementation handoff,
   with the command, measured source version and report paths accessible to
   REVIEWER. Name the project-documented machine-readable/text artifacts to
   inspect; HTML may supplement them for source browsing. DEVELOPER runs
   coverage; REVIEWER reads the report statically alongside code and tests.
   Coverage percentages are evidence, not an acceptance threshold by themselves.
   Do not introduce coverage tooling into projects where it is not configured.
5. After all configured checks pass, DEVELOPER commits the reviewable inputs.
   DISPATCHER sends that exact commit and saved results to REVIEWER, who reviews
   independently of the developer’s self-checks and commits its report.
   DEVELOPER fixes implementation findings and reruns relevant checks without
   fresh LEAD permission for each fix.
   Keep required reviews, frozen inputs and execution permissions. Changes to
   requirements, scope or permitted effects return to LEAD and review.
6. DISPATCHER reports completion to LEAD only when acceptance conditions pass
   and blocking findings are resolved. Include the result, review references,
   check evidence and limitations. Report a blocker without claiming completion.
7. LEAD assesses suitability and reports the outcome to HUMAN. LEAD resolves
   substantive questions within HUMAN's instructions or asks HUMAN for a
   needed decision. Stay within the authorized scope; acceptance does not
   authorize unrelated later stages or publication. When a merge into `main`
   is needed, LEAD follows [MERGE](MERGE.md).

### Checks and verdicts

For logic work, DEVELOPER runs tests, builds, validators, linters and
other executable checks, or LEAD does so on the direct implementation route.
CI may run the agreed checks. REVIEWER reads
requirements, code, tests, fixtures, assertions, diffs and saved results; it
does not execute project code, rerun checks or trigger CI, except for the report
commit procedure in [REVIEW-COMMIT](REVIEW-COMMIT.md). Assess requirement
coverage, missing edge cases, meaningful assertions and whether tests detect
relevant failures. Request missing checks from the implementer through the
route’s review handoff. Distinguish reported results from static conclusions.

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
Record findings and decisions in the task's review document. Committing a report
preserves its verdict; it does not itself establish acceptance.

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
