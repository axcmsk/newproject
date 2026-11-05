# Merge Git-policy amendment review

- Verdict: `ACCEPTED` for the policy amendment.
- Reviewed source and review-start HEAD:
  `07c6ec185055ba656a5286a275514f3768a25888`.
- Baseline: `bc3327e27512c9b59fb3522b1092449e6f42e912`.
- Scope: the HUMAN-authorized rerere/hook changes in `docs/specs/merge.md`
  and `docs/worklog/039-merge-task.md`; no implementation acceptance.
- Findings and conditions: none.
- Next owner/action: LEAD releases the revised contract for the existing
  correction round; DISPATCHER routes the remaining work and evidence.

The revised specification clearly honors repository rerere reuse and index-update
settings, without enabling or disabling them. A nonzero merge result still stops
dependent work, even if Git has applied a cached resolution. Successful hooks may
change the message or content; the helper passes the supplied message with verbatim
cleanup and performs no pre/post semantic comparison. Formal source/target,
parent-topology and status checks remain, as do error reporting and no automatic
recovery. The verification plan distinguishes ordinary unresolved conflicts from
the newly permitted populated-rerere case and requires successful hook coverage.

This explicit authority supersedes R3 and the rerere-disable requirement within
R4 of review 042; it does not retroactively declare the prior implementation
accepted. R1, R2 and submodule coverage remain open. Updated rerere/hook evidence
must demonstrate the newly selected behavior in the same bounded correction round.
No new review of HUMAN's policy choice or generic Git-control framework is required.

The task preserves the branch-only handoff and explicitly forbids merging to main
before HUMAN inspection. Parked corrections were not reviewed or executed here.
Committed executable inputs are unchanged; previous check results apply to this
documentation checkpoint only, not to unfinished corrections.

Review was static, with no checks or source edits. Review began at the exact source
with a clean tree. Only this assigned report may be committed after HEAD/index/path
verification; return the actual report hash separately and release writer ownership.
