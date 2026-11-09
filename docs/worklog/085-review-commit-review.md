# Review commit helper implementation review

Current verdict: `ACCEPTED` for corrected source
`a53116c9ab5a8e50222d1ef6a2a28063749a5c36`; see the follow-up review below.
The original review is preserved in the following sections and in commit
`783c95ea57b4127d9932a5d5cfc667bef6c55ba0`.

## Original review

Verdict: `CHANGES_REQUESTED`.

Approved specification: `docs/specs/review-commit.md` at
`f214677c7bac64ade6621767cc6712e1ccaaa8b9`, accepted in report 083.
Reviewed source and initial HEAD:
`5e62f0208025cc3370fd4afb53c9ca950a6e6dd0` on
`codex/review-commit-helper`. The index and working tree were clean at review
start. Allowed reviewer write: `docs/worklog/085-review-commit-review.md` only.

## Findings

### R1 — Hidden tracked changes can pass both scope and cleanliness checks

Location: `tools/review_commit.py:54-77`, used before staging and again at
`tools/review_commit.py:180`.

`changes()` relies exclusively on `git status` to identify dirty paths. Git index
flags `assume-unchanged` and `skip-worktree` can suppress reporting of worktree
changes. A tracked foreign file carrying either flag can be modified while an
ordinary report also changes. The foreign modification is then absent from the
preflight and final status output, allowing the helper to commit the report and
print success with an unrelated modification still present. Exclusive writer
ownership does not remove a preexisting index flag or hidden change. This
violates the specification's requirement to reject every foreign unstaged change
and to verify a clean final worktree.

Closure: make scope and final-state verification reliable for these index states,
or explicitly refuse states whose cleanliness cannot be established, preserving
the caller's flags and files. Add temporary-repository regression coverage for
both flags on a modified tracked foreign file, asserting nonzero exit, unchanged
HEAD, unchanged report staging and preserved foreign contents/flags. Also cover
a hook introducing a hidden tracked modification so the final cleanliness
condition cannot incorrectly report success. DEVELOPER may choose the mechanism;
no index-flag mutation or cleanup is requested.

### R2 — Required unsafe-change categories lack regression evidence

Location: `tests/test_review_commit.py:69-101`.

The foreign-change test covers only an untracked file; deletion is exercised
only as a missing explicitly supplied report. There are no integration cases
for staged or unstaged tracked foreign changes, a rename whose source deletion
must remain visible, conflicts, or index/worktree type changes. These are
explicit refusal categories in the approved contract. The current passing suite
does not establish those safety boundaries or preservation on those refusals.

Closure: add focused cases for those categories. Assert nonzero exit before any
report staging/commit, unchanged HEAD, and preservation of the preexisting index
and affected file contents or types. For rename coverage, include the report
destination in the allowed paths while leaving its deleted source outside them,
so the test proves the deletion is not concealed. Rerun configured checks and
save evidence for the corrected source version.

## Evidence and limitations

Static review covered the helper, all six new integration tests, the scoped
commit diff and `docs/worklog/084-review-commit-implementation.md`. The two saved
SHA-256 identities match the reviewed files. Saved evidence reports 49 tests
passing, Ruff lint passing, and all eight checked files already formatted on
Python 3.9.6 and Git 2.54.0. Those results cover the submitted implementation;
they do not supply the missing cases above. The whitespace check is recorded as
passing before the implementation report was added.

No helper, tests, project validators or other executable project checks were run
by REVIEWER. Findings are from static reasoning, not claimed runtime reproductions.
The existing checks for literal paths, pending operations, hook refusal,
committed-tree changes and untracked post-hook residue are consistent with the
contract on the inspected paths. No generator or role changes were included.

## Handoff

After committing only this report on the recorded initial HEAD, REVIEWER
releases writer ownership to DISPATCHER. DISPATCHER returns R1 and R2 to
DEVELOPER under the existing task scope, obtains a checked correction commit and
requests static review of the affected implementation and evidence. This report
does not authorize integration or constitute conditional acceptance. Its commit
identity is returned separately; the reviewed source identity remains unchanged.

## Follow-up review

Verdict: `ACCEPTED`.

Reviewed corrected source and initial HEAD:
`a53116c9ab5a8e50222d1ef6a2a28063749a5c36`, on
`codex/review-commit-helper`. The index and working tree were clean at review
start. The approved specification remains `docs/specs/review-commit.md` at
`f214677c7bac64ade6621767cc6712e1ccaaa8b9`. Scope: the correction diff from
`783c95ea57b4127d9932a5d5cfc667bef6c55ba0`, closure of R1/R2, and updated
implementation evidence. Only this review report is assigned to REVIEWER.

R1 is closed. Every `changes()` call now reads NUL-delimited `ls-files -v`
entries and refuses skip-worktree and assume-unchanged flags before relying on
status. This runs before staging, before committing and during final verification.
It leaves flags intact. Regression cases cover both flags on modified tracked
foreign files and assert refusal, unchanged HEAD/index entries, preserved file
contents and preserved flags. The hook case creates an assume-unchanged foreign
modification after committing, asserts nonzero exit with the index-flag
diagnostic, and verifies that the created commit, flag and modified file remain.

R2 is closed. Added cases cover tracked foreign changes both unstaged and staged,
a staged rename with only its report destination permitted, unmerged index
entries, a worktree symlink, and a symlink index entry with a regular worktree
file. The common assertion compares HEAD and all staged entries before/after
refusal. Individual assertions preserve relevant contents, deleted-source state,
or symlink/index type. These are meaningful safety and preservation assertions,
not merely wrapper exit-code checks.

The corrected SHA-256 identities recorded under "Corrections after review 085"
in `docs/worklog/084-review-commit-implementation.md` match the reviewed helper
and test files. Saved evidence reports 53 passing tests and passing configured
Ruff lint and formatting checks on Python 3.9.6 / Git 2.54.0. These remain
DEVELOPER execution results; REVIEWER ran no helper, tests or executable project
checks. Adding this report does not alter their checked inputs.

No blocking findings remain in the reviewed scope. The helper conservatively
refuses flagged index entries even when the corresponding files are unchanged;
it does not attempt to repair them. Exclusive writer ownership remains a
required assumption, and acceptance does not grant broader authority or make
the helper mandatory.

After committing only this report on the recorded initial HEAD, REVIEWER
releases writer ownership to DISPATCHER. DISPATCHER may report implementation
acceptance and the exact source/report/check references to LEAD. Integration
remains LEAD's responsibility under the existing task and project workflow.
