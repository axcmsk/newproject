# Merge-trigger simplification review

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `a38973ba93a33d5b5c73e51fb4e13b7f8d8093b5`.
- Baseline: `560eab11bcdc46c378bcb5a7172968b177529b2c`.
- Assignment: `docs/worklog/059-simplify-merge-trigger.md` at source.
- Scope: trigger wording in root MERGE, PROCESS, PROJECT-RULES and LEAD.
- Findings and conditions: none.
- Next owner/action: LEAD reports completion; no actual merge is required here.

All four entry points consistently say to use the procedure when a merge into
main is needed. This removes the blanket instruction to merge completed branches
without restoring a separate HUMAN-approval gate. MERGE retains explicit HUMAN
holds, required checks/review, helper use, ownership and failure handling. Source
preservation, repository-only scope and separate push/deployment authority remain.

Only documentation changes; the supplied prior 40-test and Ruff evidence remains
applicable to unchanged inputs. REVIEWER performed static review only. Review
began at the exact source with a clean tree. Verify HEAD/index/report-only boundaries
before committing this report, return its actual hash separately and release
writer ownership to LEAD. No source edit, executable check, merge or push was made.
