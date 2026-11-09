# Review instructions by workflow mode: review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`9fafb093e5c99f8fcb3721278d2a5e38629fb6a1`, on
`codex/review-instructions-by-mode`. Baseline:
`1e463d57882559e0845402542076d628a641a4cb`. The index and working tree were
clean at review start. Only reviewer write:
`docs/worklog/100-review-instructions-by-mode-review.md`.

## Scope and conclusions

Static documentation short-route review covers task 099, root/base REVIEW-COMMIT
and the heavy operational-write section, against HUMAN's mode-separation decision
supplied in the task. No blocking findings.

The common guide contains only the strict report-only procedure and no
`--allow-dirty` mention. Root and base copies have identical Git blob identities.
They retain pinned HEAD, assigned report paths, exclusive writer ownership,
normal hooks, distinct source/report identities and common failure handling.

Heavy explicitly extends only the working-tree allowance and provides the fixed
STATE/journal command. Each option requires explicit permission and exclusion
from pinned inputs; other paths cannot be substituted. Without either permission,
the base command applies. Pinned, unpermitted and other operational paths require
buffering outside the repository until release. This is not an automatic allowlist.

The STATE operational-block and journal checks remain REVIEWER's responsibility;
the helper is limited to file preservation and report isolation. Regular tracked
files with no staged changes, clean final index/reports, unchanged unstaged
operational changes and separate DISPATCHER closeout are retained. The heavy
guide names its override and reuses the base failure rules instead of duplicating
or weakening them. Its common-procedure link no longer uses the removed anchor.

The checkpoint changes no helper, generator or generic helper contract. Narrower
workflow instructions therefore do not remove the script's accepted generic
capability or broaden operational authority.

## Evidence and limitations

Task 099 records 59 passing tests (24.162s), passing configured Ruff lint and
format checks (eight files), a passing working-tree whitespace check, identical
root/base guides and no stale workflow/template anchor references. These checks
cover baseline executable code with the changed template texts. LEAD additionally
reported successful `git diff --cached --check` immediately before the exact
checkpoint commit in a sequential command, exit code 0, chunk `ced9b3`.

REVIEWER inspected the changes and saved evidence statically and ran no tests or
project checks. Adding this report does not alter checked inputs. Report saving
uses only the accepted helper's strict invocation under REVIEW-COMMIT authority.

## Handoff

Commit only this report directly atop the initial HEAD, verify the report-only
child and clean repository state, then release writer ownership to LEAD. Return
the report commit separately from the accepted checkpoint. LEAD may integrate
under the established merge procedure; REVIEWER performs no merge or push.
