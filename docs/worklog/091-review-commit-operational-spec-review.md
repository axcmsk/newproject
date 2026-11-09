# Explicit operational paths: specification review

Verdict: `ACCEPTED` for the planned contract only.

Reviewed checkpoint and initial HEAD:
`280fcca540825e1a21798086d728088944e6ecad`, on
`codex/review-commit-allowed-dirty`. Baseline:
`941708481d179ddb2e7fdb2653023e5ff7ced673`. The index and working tree were
clean at review start. Only permitted reviewer write:
`docs/worklog/091-review-commit-operational-spec-review.md`.

## Scope and findings

Static review covered `docs/specs/review-commit.md`, task 090, and the baseline
helper, REVIEW-COMMIT procedure and heavy operational-write rules, under the
repository's REVIEWER and process boundaries. No blocking findings.

The extension keeps operational permission separate from report commit scope.
Exact, explicitly assigned paths do not grant new write authority; the caller
must exclude pinned inputs and verify STATE-block/journal semantics and writer
ownership. The helper remains responsible for mechanical file and Git guarantees,
not interpreting those documents or choosing operational paths automatically.

Requiring tracked regular entries in both HEAD and index, with index entries
equal to HEAD, excludes staged and partly staged operational changes. Disjoint
report/operational sets, exact literal path handling, unsafe-type/parent refusal
and the existing global hidden-index-flag refusal avoid ambiguous path coverage.
Clean listed files and ignored-but-tracked files have explicit treatment.

Snapshots of every listed operational file's bytes, permissions and index entry
before staging, rechecked before and after commit, provide verifiable preservation
conditions. Snapshots may not be refreshed after a filter or hook changes them.
The expected tree, sole-parent topology and final clean index retain report-only
commits; only original listed operational changes may remain unstaged. Failures
preserve the observable state and do not authorize automatic repair or retry.

The required tests cover normal and refusal cases, exact report-only commit
results, content/mode/index preservation, clean listed paths, hidden flags,
partly staged states and hook/filter effects, plus installed behavior in both
generated variants. The requirements are mechanically testable without claiming
protection from concurrent writers or hostile hooks. Strict mode remains required.

Pending status is explicit. The runtime helper and workflow instructions are
unchanged in this checkpoint. Later implementation and root/base/heavy adoption
must remain in this branch and receive independent acceptance; the existing
heavy manual exception remains effective until then. This review neither
implements the option nor authorizes merging the pending contract into main.

## Evidence and limitations

Task 090 records 53 passing unittest cases (19.491s), passing configured Ruff
lint and format checks (eight files), and a passing working-tree whitespace
check on unchanged baseline executable/template inputs. LEAD additionally
reported successful `git diff --cached --check` on the exact checkpoint inputs
in the sequential commit command, exit code 0, tool chunk `ba0fcd`.
These results cover existing behavior, not the planned extension.

REVIEWER ran no project checks. Saving this report uses only the already accepted
strict helper procedure, without the new option, and does not change checked
inputs. Implementation correctness and execution evidence remain for the later
implementation review.

## Handoff

Commit only this report as a direct child of the initial HEAD using the existing
strict helper, verify the report-only result, and release writer ownership to
LEAD. Return the report commit separately from the approved contract identity.
This stage ends at contract acceptance; no DISPATCHER handoff, implementation
or merge is requested by this report.
