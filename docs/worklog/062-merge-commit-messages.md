# Conventional merge messages

HUMAN approves Conventional Commits for the final merge message only, keeping
internal step/fixup/docs/review/log prefixes and the helper unchanged. Baseline:
2a6135738261f4697a6fcc1165bdf0770aca693f. LEAD edits root MERGE and PROJECT-RULES
plus this brief; no generator, template, script, history or merge operation.
The rule covers both squash and two-parent result commits, with LEAD choosing
the message. Source: Conventional Commits 1.0.0,
https://www.conventionalcommits.org/en/v1.0.0/ (consulted 2026-11-08).

Documentation short route: REVIEWER Astra/high independently reviews and commits
only docs/worklog/063-merge-commit-messages-review.md, then releases ownership.
Prior 40 passing tests and README Ruff checks in 055 remain valid: all executable,
configuration, template and test inputs are unchanged. LEAD checked the diff,
links, standard syntax and git diff --check (passed). REVIEWER is static-only.
