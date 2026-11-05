# Heavy implementation review

## Identity, scope and verdict

- Verdict: `ACCEPTED`.
- Reviewed implementation/source: `3b88345c6eb81db5c0e016e040e9a10463fd1b75`.
- Approved contract: `docs/worklog/025-heavy-task.md` and
  `docs/specs/newproject.md` at `71bf1e3eabbb679536bed8b0cff4adea0db0688b`.
- Specification acceptance: `docs/worklog/029-heavy-spec-review.md`, committed
  at `610a238` before implementation.
- Scope: generator and template relocation, transferred journal writer, tests,
  saved results, and consistency with the approved generated documentation.
- Findings: none requiring correction.
- Conditions: none.
- Next owner/action: DISPATCHER returns acceptance and evidence to LEAD;
  the assigned writer may commit this report after review release.

## Static assessment

The common template files move to base with unchanged blobs and modes. Normal
creation scans only base; heavy preflights the additive layer, rejects file and
directory conflicts, excludes the root fragment from output and composes AGENTS
using the specified newline rule while retaining the base file mode. Shared
directories are emitted once, and their additional children remain copyable.
Selected roots and entries are checked before Git or target mutation; existing
Git isolation, refusal handling and exclusive destination file creation remain.
The parser implements both flag positions, the terminator, literal flag names
and duplicate/missing/extra-argument refusal without introducing shell execution.

Comparison with the pinned DiBBS writer at
`767ced76e8f08810c11cf499cbcbc80a11f5238b:scripts/workflow/work_log.py`
shows branding removal, import/format changes, an equivalent default read mode
and a lint suppression, with validation and append semantics preserved. The
installed default log path resolves from the script location. Unsupported locking
is refused before log creation, while schema/help do not enter the append path.
History admission, exclusive locking, duplicate IDs, corrections and ambiguous
write diagnostics retain their original bounded behavior.

The tests retain the existing real-Git creation/refusal and failure-injection
coverage. Added tests exercise layer union and both ancestor-conflict directions,
flag/terminator parsing, exact AGENTS composition and mode, fragment exclusion,
invalid/missing/empty layers, unreadable metadata, and normal independence from
heavy. Real-template generation exercises both variants and invokes the installed
journal from another working directory. Journal tests use only temporary synthetic
history, preserve historical bytes, exercise validation/corrections and malformed
tails, simulate unsupported locking, and retain concurrent append/duplicate races.
Assertions inspect relevant diagnostics and final content/state rather than relying
only on nonzero status.

Generated document destinations and explicit heavy onboarding agree with the
base relocation and accepted policy. The two sibling common preference links
remain intentionally optional. The initial journal is empty; no real usage,
authority, historical log or DiBBS exception is transferred.

## Evidence, limitations and authority

`docs/worklog/026-heavy-implementation.md` binds its checked source to the
implementation commit containing that report and states no subsequent executable
input changes. It reports 25 passing tests, expanded Ruff lint and format checks,
and Python 3.9.6 / Git 2.54.0 / Ruff 0.17.3. It also records the corrected initial
unsupported-lock test assertion and final successful rerun. These are supplied
developer results; REVIEWER did not run project code, tests, validators or CI.
Execution on other platforms was not demonstrated. POSIX append locking remains
the documented platform limitation, and concurrent hostile filesystem replacement
remains outside the generator contract.

During review LEAD conveyed HUMAN's clarification that avoiding duplication is a
design preference, not an immutable architectural prohibition; possible additional
fragments or conditionals are ideas rather than current scope. The implemented
base-plus-heavy design remains within the authorized task. This acceptance does
not impose a future generic template engine or prohibit later authorized designs;
LEAD owns recording that clarification in the task wording after review release.

Review-start HEAD matched the exact source and the working tree was clean. At
closeout HEAD was unchanged and only this permitted report was added. REVIEWER
made no source edits or commits and releases writer ownership. Acceptance covers
the named local implementation; it does not authorize merge, push or deployment.
