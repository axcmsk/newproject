# Heavy specification review

## Identity, scope and verdict

- Verdict: `CHANGES_REQUESTED`.
- Reviewed specification/source: `aef51db5f7f17910f8dee6a432740a6c8a51ea84`.
- Baseline: `236ea1a1d0336c1d53c7f6a07ca6a705217e7757`.
- Branch: `codex/heavy-template`.
- Contract: `docs/worklog/025-heavy-task.md` and `docs/specs/newproject.md` at
  the reviewed commit, with README, root PROJECT-RULES and the heavy documents.
- Acceptance scope: specification completeness and consistency, proposed layer
  composition, heavy policy, journal transfer requirements and verification plan.
- Excluded gates: implementation correctness, actual generation, installed
  journal behavior, mechanical base move and implementation check results.
- Next owner: LEAD resolves R1 and returns a checked correction commit for review.
- Conditions allowing closure without review: none.

The base move and journal implementation are deliberately pending specification
acceptance. References to their planned destinations are not treated as completed
implementation or as missing-specification defects.

## R1 — Reconcile live operational writes with the base review freeze

Locations: `template/heavy/docs/workflow/HEAVY.md:51-61,83-87` and
`template/heavy/docs/workflow/work-log-format.md:53-60`, in combination with
`template/docs/workflow/PROJECT-RULES.md` under "Checks, review and commit"
(the latter will move unchanged into base).

HEAVY requires material STATE and journal updates, while the journal instructions
defer writes only when the journal itself is frozen. The inherited base closeout
rule allows working-tree changes only in permitted review reports. HEAVY says it
overrides only named base provisions but does not name an exception here. A normal
budget stop, ownership transition or blocker during review can therefore require
an operational update that makes the prescribed review closeout fail, or tempt an
author to treat unreviewed operational edits as part of accepted source.

Closure: explicitly define the heavy review-start and closeout write boundary,
preserving exact reviewed inputs, expected HEAD, exclusive writer ownership and
reviewer-only report writes. If operational updates are allowed, identify their
owners and exact allowed paths/blocks outside pinned inputs, prohibit commits
during review, and distinguish those updates from source acceptance. Define
buffering for frozen operational inputs and defer substantive STATE changes until
release. Keep notification of facts affecting review authority/scope/assumptions.
Return the affected policy revision for static review.

LEAD confirmed the intended resolution in review correspondence: a named heavy
exception may allow DISPATCHER's STATE operational block and journal outside
pinned inputs; LEAD's substantive STATE edits wait for release. This is not yet
present in the reviewed source and is not a substitute for the correction.

## Other conclusions

The generator requirements define normal isolation from heavy, preflight layer
union/collisions, unsafe entry refusal, exact AGENTS composition and reserved
fragment exclusion, byte/mode preservation elsewhere, backward-compatible dash
names with explicit flag/terminator exceptions, and no generation-time commits
or task branches. Required real CLI/Git, refusal-state, composition, generated
journal-path and synthetic-history/concurrency tests provide a useful acceptance
plan without requiring real sibling projects or external services.

The heavy documents preserve base role/model and conditional-acceptance authority;
explicitly select the extension through generated AGENTS; define task branches
after the bootstrap commit, reviewed merge authorization, idle initial state,
ownership, resource identity and uncertain-session recovery. Numeric defaults
match the recorded HUMAN decision: 30% parking, 25% hard stop and a 15-point stage
threshold, plus three unsuccessful rounds on the same blocker. Unknown allowance,
scoped extensions, comparable windows and preservation at stops are distinguished
from fabricated measurements or inherited permissions.

Static inspection of the pinned DiBBS journal writer, limits, process and journal
format confirmed that the port requirements preserve schema/history admission,
locking, duplicate checks, correction semantics, provenance and write uncertainty
without transferring the real log or DiBBS-specific grants. The referenced
LIMITS, TASK-CONTEXT and PROCESS source names resolve under `docs/workflow/` in
that pinned repository. Generated Markdown destinations and the onboarding chain
are structurally coherent with the planned base move; actual generated-link
verification remains an implementation acceptance obligation.

## Evidence and boundaries

`docs/worklog/026-heavy-implementation.md` reports the unchanged baseline code's
11 passing unit tests and passing Ruff checks, with Python/Git/Ruff versions and
the pre-implementation command scope stated explicitly. Expanded commands remain
mandatory after implementation. These are supplied results, not reviewer-run
checks. REVIEWER performed only static reads and Git inspection; no executable
checks, source edits or commits were made.

Review-start HEAD was the exact reviewed commit and the working tree was clean.
At completion HEAD remained unchanged; the only working-tree addition was this
permitted report. Reviewer writer ownership is released to LEAD.
