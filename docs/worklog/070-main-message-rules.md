# Main message rules

HUMAN requests renaming MERGE-MESSAGE to MAIN-MESSAGE, choosing type by result
rather than file extension, and applying these rules to standalone commits made
directly on main as well as merge results. Agent instructions can implement a
feature or fix even when only Markdown changes. Baseline:
3edc0029d45db5a06474e9b82097a83792b65666. Branch: codex/main-message-rules.
HUMAN explicitly says not to merge yet; leave checked and reviewed work here.

Documentation short route: LEAD edits MAIN-MESSAGE (rename), MERGE and
PROJECT-RULES plus this brief. Preserve internal checkpoint/report prefixes,
existing review requirements and helper behavior. No templates, generator,
code changes, history rewriting, merge or push. Historical worklogs retain
historical paths. REVIEWER Astra/high checks the committed scope and commits
only docs/worklog/071-main-message-rules-review.md, then releases ownership.

Sources: baseline MERGE-MESSAGE, MERGE, PROJECT-RULES, PROCESS and role rules.
Checks055 (40 tests and both README Ruff commands) remain valid: executable,
test, template and configuration inputs are unchanged. LEAD inspected the diff and
current document links; git diff --check passed. REVIEWER performs static review.
