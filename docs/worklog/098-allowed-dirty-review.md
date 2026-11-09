# Allowed operational changes: implementation review

Verdict: `ACCEPTED`.

Reviewed source and initial HEAD:
`c9d2ab7321fa486d3d4567ef85ca80492bb5fb16`, on
`codex/review-commit-allowed-dirty`. The index and working tree were clean at
review start. REVIEWER owns only `docs/worklog/098-allowed-dirty-review.md`.

Approved behavioral contract: `docs/specs/review-commit.md` at
`280fcca540825e1a21798086d728088944e6ecad`, accepted in report 091 at
`a5682ab79ff227e8b3fbcfbbd6839cf120ead804`. Task 096 defines implementation and
joint activation review. The implementation baseline is
`609d0c7c0076b21405a34574cd5d9f1e6ed31b2d`.

## Scope and conclusions

Static review covered `tools/review_commit.py`, `tests/test_review_commit.py`,
`tests/test_newproject.py`, evidence 097, task 096 and the released activation
edits to the specification, root/base REVIEW-COMMIT and heavy instructions.
No blocking findings.

Operational path validation requires exact canonical paths, safe parent/file
types and one regular stage-zero index entry matching the regular HEAD entry.
It rejects untracked, staged, partly staged, conflicted and unsafe states before
report staging. Report/operational sets are disjoint; repeat arguments are
deduplicated. The existing hidden-index-flag rejection remains global. Status
handling allows only an unstaged modification for a dirty listed operational
path and excludes those paths from the report staging set.

Every listed operational file is snapshotted before the first status/staging
sequence, including clean files. Snapshots retain exact bytes, permission bits
and index entries. Rechecks before staging, before commit and after commit
detect filter/hook changes without refreshing the baseline or repairing state.
The existing pinned branch/HEAD, operation-state, expected-tree, sole-parent,
report-cleanliness and failure-diagnostic checks remain. No option means the
same strict scope. The entry point remains short, with environment rejection
still preceding diagnostic Git authorization.

Tests provide meaningful preservation assertions for duplicate/literal/multiple
paths, clean files, ignored tracked files and content/mode changes. They compare
commit identity, sole parent, exact report diff, operational index entries and
dirty status. Refusal cases inspect HEAD/index and relevant file state for
overlap, unsafe/untracked paths, staged and partly staged content, staged modes,
deletion/rename, conflicts, hidden flags, unlisted dirt and operational-only work.
The filter test detects modification before a commit; hook cases detect content,
mode or staging changes after a commit and retain the changed state. Existing
strict-mode tests remain. Both generated variants exercise the installed option
after strict refusal, verifying report-only topology and preserved operational
contents/mode/index/dirt.

Activation removes pending wording without altering the approved behavioral
requirements. Root/base REVIEW-COMMIT files match exactly. Their staged-only
report boundary and explicit operational permission agree with the implementation
and contract. The heavy link targets the renamed operational section and its
manual exception is removed. Exact assignment, caller STATE/journal checks,
pinned inputs, exclusive ownership and separate operational closeout remain.

## Evidence and limitations

All eight recorded file identities in evidence 097 match: three implementation/
test files and five released documents, counting root/base separately. Saved
results report 59 passing tests (25.181s), passing configured Ruff lint and
format checks (eight files), and passing working/staged whitespace checks on
Python 3.9.6 and Git 2.54.0. REVIEWER inspected these results and test assertions
statically and ran no project tests or checks.

The helper does not interpret operational documents or grant permission. It
continues to depend on exclusive writer ownership and does not claim protection
against concurrent writers or hostile hooks. No existing generated projects are
updated. Report saving may use the now accepted implementation under the existing
administrative REVIEW-COMMIT authority; that is not a test execution.

## Handoff

Commit only this report directly atop the recorded source, verify the report-only
child and clean repository state, and release writer ownership to DISPATCHER.
Return the report commit separately from the accepted source identity. DISPATCHER
may return implementation and joint instruction acceptance to LEAD for integration
under the established workflow; this report performs no merge or push.
