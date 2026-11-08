# Local merge message guide

HUMAN requests a self-contained English MERGE-MESSAGE.md with the upstream link
as attribution rather than required reading. Baseline:
b4e951b4e28ce8d1ae2e1249cf898939a2ce6905. Documentation short route: LEAD writes
the guide, replaces MERGE's message paragraph with a local link and updates the
PROJECT-RULES reference. Include existing types with meanings, optional scope,
breaking changes and examples. Preserve both-mode applicability, internal prefixes
and the helper's lack of message inference/validation. No code/template/generator
changes, merge or push.

Sources: baseline MERGE and PROJECT-RULES; Conventional Commits 1.0.0,
https://www.conventionalcommits.org/en/v1.0.0/ (already consulted in task062).
REVIEWER Astra/high independently reviews and commits only
067-local-merge-message-review.md under docs/worklog, then releases ownership.
Checks055 (40 tests and README Ruff commands) remain valid with executable,
configuration, template and test inputs unchanged. LEAD inspected links and diff;
git diff --check passed. Reviewer performs static review only.
