# Merge as part of development

HUMAN removes the default requirement for separate merge approval; explicit
holds may still apply. Baseline: 2a96c9cbe901ed124404d478d86739262b304d6a.
Documentation short route: LEAD updates only root MERGE, PROJECT-RULES, PROCESS
and LEAD plus this brief. Merging completed task branches into main becomes part
of authorized development after required checks and review. Preserve explicit
holds, helper use, source branches, check ownership and failure recovery.
No push/deployment authority, code changes, template or generator integration.

Inputs: the named workflow documents and tools/merge.py at baseline. REVIEWER
(Astra/high) independently checks consistency and authority boundaries, commits
only docs/worklog/058-default-merge-review.md and returns ownership to LEAD.
No new policy is relied on before review. This task changes documentation on
main; it does not merge another task branch.

Checks: the 40 passing tests and both README Ruff checks recorded in 055 remain
valid: executable, test, template and configuration inputs are unchanged. LEAD
inspected the diff, local links and git diff --check (passed). REVIEWER is static-only.
