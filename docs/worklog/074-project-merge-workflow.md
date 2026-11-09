# Install the shared merge workflow

HUMAN approves a feature branch, common merge/message instructions and helper for
both normal and heavy projects, then one final merge after checks and review.
Baseline: 1aaf963e9975ab89cacc41b5a948dc5256c0dbd0.
Branch: codex/project-merge-workflow. Source contract: docs/specs/newproject.md
in this commit; preserve its existing guarantees. Sources at baseline:
newproject.py, tests/test_newproject.py, tools/merge.py, root workflow docs,
template/base and template/heavy/docs/workflow/HEAVY.md.

LEAD owns specification, README and workflow docs. Copy the three current root
MERGE/MAIN-MESSAGE/BRANCH-MESSAGE guides into base; align shared PROJECT-RULES,
PROCESS and LEAD sections. Heavy retains mandatory task branches and checkpoints,
but replaces its no-ff/extra approval rule with the common procedure and preserves
reviewed source commits. Remove obsolete root-only/deferred-integration statements.
No merge algorithm changes, external publication or unrelated workflow changes.
Keep the script source solely in tools/merge.py; generator copies it to both
variants with preflight and exclusive-copy safeguards in the contract.

Standard route: REVIEWER Astra/high reviews this contract into 075-project-merge-spec-review.md.
LEAD then releases docs and contract through DISPATCHER Luna/low to DEVELOPER
Terra/medium. Developer owns newproject.py, tests/test_newproject.py and evidence
076-project-merge-implementation.md. It may commit exact LEAD-released docs without
editing. Run meaningful real-Git generated-project tests and preflight failures,
then full unittest and README Ruff checks. REVIEWER writes/commits
077-project-merge-review.md after the checked implementation commit. Use new
numbered reports for failed reviews; no rewriting reviewed history.

For this specification-only commit, checks055 remain valid: code, tests, templates
and configuration are unchanged. LEAD checks diff whitespace. Implementation
must run fresh checks because executable and template inputs will change.
After acceptance, LEAD uses the current helper to merge the branch with a feat
message, retains the source branch and does not push.
