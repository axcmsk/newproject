# Commit rules and report ownership review

## Identity, scope and verdict

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `377c2140436f25b1e211e8030e9a8c1be4d86251`.
- Baseline: `2243ed6d3424cd3a22d2ea76daa3be0c450059b1`.
- Assignment: `docs/worklog/035-commit-rules-task.md` at the reviewed source.
- Scope: root/base PROJECT-RULES, PROCESS and REVIEWER guide; heavy operational
  review writes, evidence grouping and journal closeout wording.
- Findings and conditional requirements: none.
- Next owner/action: LEAD verifies the returned report commit's parent and
  report-only delta, then closes out the authorized local documentation task.

## Static conclusions

The English type definitions consistently distinguish stages, current-stage
corrections, supporting documentation, independent reviews and operational
records. Selection is by content; standalone documentation uses step and
accompanying documentation uses docs. Existing wrong prefixes do not block
review or justify history rewriting. No automated enforcement, retrospective
renaming or merge-selection rule is introduced.

Shared commit classification and ownership live in PROJECT-RULES. The REVIEWER
guide defines its specific report-only boundary, exact HEAD/index checks,
exclusive ownership and separate return of the report commit identity. PROCESS
routes specification reports to LEAD and implementation reports through
DISPATCHER. A completed report can preserve any verdict; its commit does not
imply acceptance. Parent/delta verification explicitly recognizes the expected
report commit without relabeling the reviewed source or invalidating unchanged
check results. Conditional acceptance remains intact.

The heavy extension explicitly allows only preauthorized operational changes
outside pinned inputs to remain in the working tree. It does not extend staged
or committed report contents, requires exact path/block inspection, leaves
operational edits unstaged, and transfers writer ownership back after the
report commit. Its evidence/journal wording no longer groups those records into
the reviewer's report commit. Substantive STATE edits and unexpected changes
remain outside this exception.

Root/base PROCESS and REVIEWER guides are identical. PROJECT-RULES shared policy
matches, with only the intentional root repository-purpose section differing.
Executable check ownership and REVIEWER's static-only role are preserved; Git
inspection and the report commit do not authorize tests, validators or CI.

## Evidence, authority and commit boundary

The assignment records passing 26-test, expanded Ruff lint/format and whitespace
checks on the source checkpoint. These are supplied LEAD results, not reviewer-run
checks. No executable inputs changed during this review; adding only this report
does not require repeating those checks. Review consisted of static document,
diff and Git inspection, with no project execution or source edits.

HUMAN's explicit task authorization permits this reviewer to commit its own
report independently of the proposed policy's verdict. The sole permitted write
and commit path is `docs/worklog/036-commit-rules-review.md`. Review began on main
with the exact source HEAD and a clean working tree. Before the report commit,
verify that HEAD still matches, the index contains no unrelated changes, and
only this report is changed; stage this path explicitly and inspect its staged
delta. Return the actual report commit hash separately, preserving the reviewed
source identity above, then release ownership. No merge, push or publication is
authorized by this review.
