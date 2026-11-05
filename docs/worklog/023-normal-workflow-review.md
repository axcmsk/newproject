# Normal workflow review

## Reviewed identity and scope

- Source and review-start HEAD: `d984af68bac8ba42e2619ce3ee79f759c37aa518`.
- Baseline: `f30e6ed`, the source commit's parent.
- Assignment: `docs/worklog/022-normal-workflow-task.md` at the source commit.
- Scope: README and root/template PROCESS and PROJECT-RULES changes;
  consistency with AGENTS and existing LEAD, DISPATCHER, DEVELOPER and REVIEWER
  responsibilities; assignment and saved check evidence.
- Reviewer write boundary: only `docs/worklog/023-normal-workflow-review.md`;
  no commits or edits to reviewed inputs.

## Verdict

`CHANGES_REQUESTED`

### R1 — Remove the superseded short-route instructions

Locations: `docs/workflow/PROCESS.md:97-109` and
`template/docs/workflow/PROCESS.md:97-109` at the reviewed commit.

The newly added short route requires checked commits before review and separate
review-report commits. The retained text immediately below it still directs
authors to commit accepted documents and review together, says mechanical-change
results need not be committed before review, and defines uncommitted review
inputs. These contradictory instructions leave an ordinary task free to follow
the former route, defeating the explicitly authorized checkpoint and exact-commit
review policy.

Closure: remove or reconcile the obsolete block in both copies so the short
route has one unambiguous commit-before-review sequence, with report commits
after review and checked correction commits before affected re-review. Preserve
the failed review and return the new exact source commit for static review.

## Other conclusions and evidence

The two PROCESS copies are identical. PROJECT-RULES differs only by the existing
root-specific repository-purpose section; its shared policy is aligned. The new
ownership, authority, uncertain-session recovery and proportionate-evidence
sections fit the assignment, preserve existing role separation and conditional
acceptance, and introduce no heavy state, journal, budget or fixture subsystem.
No generator implementation or test changes appear in the reviewed diff.

The assignment reports 11 passing unit tests, passing Ruff lint and format
checks, and a passing whitespace check on the prepared source. README documents
the same executable check commands. These are reported results, not independently
executed reviewer checks. Review was static only; no project code, tests,
validators, linters, builds or CI were run. Read-only Git inspection established
a clean initial working tree on `main`, and HEAD remained the reviewed commit
before writing this report.

## Next owner

LEAD owns the wording correction, applicable check evidence, preservation of this
review, and the new checkpoint commit. Return the affected revision to REVIEWER;
this verdict does not authorize closure without re-review.
