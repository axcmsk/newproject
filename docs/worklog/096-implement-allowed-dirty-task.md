# Implement allowed operational changes

HUMAN now authorizes implementation and activation of --allow-dirty.
Baseline: 609d0c7c0076b21405a34574cd5d9f1e6ed31b2d on
codex/review-commit-allowed-dirty. Approved behavioral contract:
docs/specs/review-commit.md at 280fcca540825e1a21798086d728088944e6ecad,
ACCEPTED in 091 at a5682ab79ff227e8b3fbcfbbd6839cf120ead804. Prepared instructions
at 68b8e53c567d076dd9215ab031f17ee3de673cc5 were accepted in 093 at
af3bc705ffe6258138e2dbf2f7a73246cab86373. Refactored strict helper accepted in 095
at baseline. No requirement changes: implement the accepted contract exactly.

LEAD prepares and releases docs/specs/review-commit.md, root/base
docs/workflow/REVIEW-COMMIT.md, template/heavy/docs/workflow/HEAVY.md and this
assignment: remove pending notices, permit only assigned operational worktree
changes, and remove heavy's manual exception. These edits become active only
after independent acceptance of implementation and instructions together.
Keep small coherent functions and a short main. No broad ignore option, hidden
allowlist, journal parser, locking service or additional behavior.

DISPATCHER Luna/low forwards the exact approved contract and this routing to
existing DEVELOPER Terra/medium. Developer owns tools/review_commit.py,
tests/test_review_commit.py, tests/test_newproject.py and
docs/worklog/097-allowed-dirty-implementation.md. LEAD's released documents may
be staged and committed but not edited by DEVELOPER. Questions about requirements
return directly to LEAD. One writer at a time; no merge/push by workers.

Implement repeatable literal operational paths, preflight refusal before staging,
and snapshot preservation before and after the commit, including hooks/filters.
Cover all contract verification categories with meaningful state assertions in
temporary repositories, strict-mode regressions and installed helper behavior
in both generated variants. Run README suite, Ruff lint/format and diff checks;
record tested identities, commands/results/versions and failures. Commit ready
source plus released documents as fixup:, then release ownership.

REVIEWER Astra/high statically reviews exact final source, activation edits and
evidence against the approved contract; only writes
docs/worklog/098-allowed-dirty-review.md. Use accepted prior strict helper if
review requests changes; after acceptance, the new helper may save the report.
Verify report-only commit atop pinned source and release ownership. Corrections
go to their author; preserve failed reviews. LEAD integrates accepted branch
through tools/merge.py, preserving branch and reviewed history, and verifies the
resulting tree. No push, deployment or changes to existing generated projects.
