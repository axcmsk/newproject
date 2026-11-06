# Draft merge helper implementation review

## Identity and verdict

- Verdict: `CHANGES_REQUESTED`.
- Reviewed source and review-start HEAD:
  `cdd81879e575a3026cd360c386935df332a4db96`.
- Approved contract: `docs/specs/merge.md` and `docs/worklog/039-merge-task.md`
  at `1c52fb226646499119d141c12788fc7a7e2036be`, accepted by review 043 at
  `703ca8e13c94e871c0689cdbe854bd6ec6e561e4`; initial acceptance chain is in 040.
- Evidence: `docs/worklog/041-merge-implementation.md` at reviewed source.
- Scope: merge.py, its tests and evidence against the amended draft contract.
- Conditions permitting closure without re-review: none.
- Next owner/action: DISPATCHER routes R1-R4 to DEVELOPER, then returns a checked
  correction commit and saved evidence for affected review. Scope changes go to LEAD.

## Findings

### R1 — Diverged squash still inherits ff-only configuration

Location: `merge.py:100-109`; `tests/test_merge.py:189-211,252-267`.

The squash command supplies no fast-forward policy override. With `merge.ff=only`
and clean but diverged histories, Git refuses the selected squash instead of
performing it. The existing configured squash fixture is fast-forwardable, so it
does not expose this failure; the other fixture tests real-merge mode. This
contradicts the contract's explicit configuration-independent mode behavior.
The [Git merge manual](https://git-scm.com/docs/git-merge) documents the ff-only
refusal on divergence.

Closure: ensure the chosen squash works on diverged clean histories despite
ff-only configuration, without automatic HEAD advance, mode fallback or persistent
config edits. Add a real-Git regression checking the one-parent result, supplied
message, final merged content, unchanged source and configuration. Preserve the
existing fast-forwardable and real-merge cases.

### R2 — A failed squash diff probe can still lead to a commit

Location: `merge.py:111-116`.

The no-net-change probe uses check=False and treats every nonzero return code as
changes. A Git error greater than 1 therefore reaches git commit, contrary to the
requirement to stop dependent operations on a Git error. Its diagnostic is lost.

Closure: distinguish no changes, changes and execution error; on the latter,
return a failing-command diagnostic and partial-state notice without attempting
the commit. Use bounded failure injection to prove that a diff error prevents
the commit and preserves the prepared state for inspection.

### R3 — Clean hook mutations are reported as success

Location: `merge.py:116-128`; hook coverage in `tests/test_merge.py:135-162`.

Post-commit checks verify branch identity, parents and cleanliness, but neither
the committed message nor the prepared merge content. A successful commit-msg
hook can rewrite the supplied message, or a pre-commit hook can stage an extra
tracked change that is included in the commit. Both leave expected parents and
a clean tree, so the helper reports success despite the contract's requirement
to report unexpected hook effects. Current tests cover only a rejecting hook.

Closure: detect and report these deviations from the supplied message and prepared
merge result, allowing the specified final-newline representation. Keep hooks
enabled and leave any resulting commit/state untouched for inspection. Add bounded
real-hook cases proving nonzero/error output rather than success after clean
message/content mutation. Any intentional relaxation of this contract belongs
to LEAD and specification review, not an implementation assumption.

### R4 — Required submodule and populated-rerere behavior lacks evidence

Locations: `tests/test_merge.py`; final paragraph of implementation evidence 041.

The evidence explicitly states that neither dirty submodules nor reuse of an
existing rerere resolution was exercised. Passing --ignore-submodules=none and
rerere.enabled=false is relevant static evidence, but the required verification
promises these operational boundaries. Enabling rerere with an empty cache does
not demonstrate that a previously resolved conflict remains unresolved here.

Closure: add focused temporary real-Git cases showing dirty submodule refusal
without mutation and that a known cached resolution is not reused: the intended
conflict remains unresolved, no commit/target advance occurs, and useful failure
output is preserved. Use local repositories only; no framework or network needed.

## Evidence and boundaries

The implementation otherwise stays within the small fixed-target interface and
uses local refs, source-exclusive subjects, pinned tips, operation-marker checks,
explicit status options, ignored-file protection and report-only recovery. Tests
and supplied evidence cover useful normal/refusal cases; the reported 35 passing
tests and expanded lint/format checks do not close the findings above. All code
assessment here was static; REVIEWER ran no project code, checks or test merges.

Review began with the exact source HEAD and a clean working tree. Only this report
is authorized for the review commit. Verify HEAD/index/report boundaries before
committing, return its hash separately to DISPATCHER, and release writer ownership.
The report commit preserves this failed verdict; it does not accept the draft or
authorize merging, pushing or adopting the helper.
