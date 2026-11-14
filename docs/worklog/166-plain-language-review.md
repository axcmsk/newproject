# Plain-language instruction review

## Reviewed inputs

- Reviewed source: `71110c39cb258378bc327f6bc6bfd5279d04b99b`.
- Comparison base: `5d2d38e56093f05ae23e0f3e3df899bab46b7d82`.
- Specification: the user request and LEAD's direct-route brief supplied in the
  review handoff: simplify complex instructions into plain programmer language,
  make conditions and actions explicit, preserve rule meaning and synchronize
  templates. Preserve permissions, conditions, exceptions, scope and role
  authority; keep short clear prohibitions.
- Scope: `docs/workflow/PROCESS.md`, `docs/workflow/PROJECT-RULES.md`,
  `docs/workflow/roles/REVIEWER.md`, their three corresponding files under
  `template/base/`, and `template/heavy/docs/workflow/HEAVY.md` and `LIMITS.md`.
- Review date: 2026-11-14. REVIEWER performed independent static review and did
  not edit the reviewed instructions or execute project checks.

## Findings and verdict

**ACCEPTED.** No blocking findings or semantic differences were found in the
eight-file diff. The brief is consistent with the supplied user requirement.

The rewritten direct-route rules retain LEAD's implementation, evidence,
correction, routing and conditional-closure duties and the same role limits.
Transfer to delegated work retains the required inputs, explicit ownership
transfer and approval before dependent work. Release conditions, static-only
review, conditional acceptance and review of editorial changes remain intact.

The project rules preserve file ownership restrictions and the requirement for
configured checks before submission or commits. REVIEWER's scope exclusion and
prerequisite exception are unchanged. Heavy wording preserves both conditions
for permitted operational changes, optional journal-related activities and the
contract/integration-risk exception for repeating the full check sequence.
Allowance resumption retains its two alternatives, the strict above-30-percent
threshold and the applicability of other stops.

The revised wording separates compound sentences into explicit conditions,
actions and lists without adding permissions or removing obligations. Existing
short prohibitions remain clear.

## Evidence

- Read the complete source diff and relevant surrounding workflow sections.
- Compared root and base copies directly: PROCESS and REVIEWER are identical.
  PROJECT-RULES differs only by the existing root repository-purpose section;
  all content from Project configuration onward is identical.
- Read README and Makefile to identify configured checks. Inspected LEAD's saved
  `/tmp/plain-instructions-checks-final.log`: Ruff formatting reports nine files
  already formatted, Ruff lint reports success, and unittest reports 75 tests
  passing with `OK`. LEAD supplied `make check` exit 0 for the reviewed inputs
  and reported `git diff --check` success. These are implementer-run results,
  not checks executed by REVIEWER.
- Confirmed the pinned source HEAD and the eight changed paths. The working tree
  initially contained only unrelated untracked `.idea/` data, which was preserved.

## Limitations and next owner

Runtime coverage is excluded by LEAD's explicit review-scope clarification:
only Markdown instructions changed, with no executable code or test changes,
and runtime coverage cannot establish wording equivalence. No coverage report
was inspected or claimed. Semantic acceptance rests on static comparison;
automated checks provide repository regression evidence only.

LEAD owns closeout and verification that the review-report commit adds only this
report above the reviewed source. The report commit does not change the accepted
source version or authorize publication. To preserve unrelated `.idea/` data and
respect the report helper's clean-tree requirement, report committing is to occur
in a clean attached worktree at the same pinned source, as directed by LEAD.
