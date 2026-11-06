# Fixed merge target amendment review

- Verdict: `ACCEPTED` for the amendment.
- Reviewed source and review-start HEAD:
  `1c52fb226646499119d141c12788fc7a7e2036be`.
- Baseline: accepted specification/report checkpoint
  `ce541dd59f8b21a2a177ac9c4f2d4377f32e3ad8`.
- Scope: `docs/specs/merge.md` interface delta and the HUMAN correction appendix
  in `docs/worklog/039-merge-task.md`; no implementation acceptance.
- Findings and conditions: none.
- Next owner/action: LEAD releases this amended contract to DISPATCHER so the
  paused developer can resume within the existing assignment.

The amendment consistently removes TARGET from the CLI and fixes it to main in
one locally editable top-level constant. It explicitly excludes target options,
configuration discovery and fallback names. The caller must still have the target
checked out, and existing committed-tip, distinct-branch, safety and merge-mode
requirements remain applicable. A local master change is a small source edit,
not a new runtime mechanism. The delta introduces no conflict with the unchanged
verification plan or expands the prototype's authority.

The earlier specification acceptance remains applicable outside this delta.
The task explicitly distinguishes preliminary developer work from acceptance
checks; no additional implementation or coverage claim is made. Prior checks
cover unchanged existing executable inputs only, and the implementation still
requires its expanded checks and independent review.

This review was static only, with no checks, source edits or inspection of the
parked unfinished files. Review began at the exact source with a clean tree.
Only this report is authorized for the review commit; verify HEAD/index/report
boundaries, commit the report and return its actual identity separately before
releasing writer ownership. No merge or push is authorized.
