# Extract branch message rules

HUMAN approves BRANCH-MESSAGE.md as the counterpart to MAIN-MESSAGE.md. Baseline:
1f79edfd9df626c48512b0de5f8871cd8b7a6b99 on codex/main-message-rules.
LEAD extracts the five existing work/report prefixes and selection guidance
from PROJECT-RULES into BRANCH-MESSAGE. PROJECT-RULES retains the routing links,
shared commit ownership, check and history rules. No new types, script behavior,
template or generator changes. HUMAN's explicit no-merge hold remains active.

Documentation short route: REVIEWER Astra/high statically reviews the committed
scope and commits only docs/worklog/073-branch-message-review.md, then releases
ownership. Prior tests and Ruff results in 055 remain valid: executable, test,
configuration and template inputs are unchanged. LEAD inspected the local links
and diff; git diff --check passed. No merge or push.
