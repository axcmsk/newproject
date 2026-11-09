# Operational-path instructions

HUMAN requested updating instructions after approval of the --allow-dirty
contract. Baseline a5682ab79ff227e8b3fbcfbbd6839cf120ead804; approved contract
docs/specs/review-commit.md at 280fcca540825e1a21798086d728088944e6ecad, with
ACCEPTED review docs/worklog/091-review-commit-operational-spec-review.md at
baseline. Continue codex/review-commit-allowed-dirty; no merge or push at this stage.

LEAD owns root/base docs/workflow/REVIEW-COMMIT.md, template/heavy/docs/workflow/HEAVY.md
and this record. Add instructions for exact assigned operational paths, caller
authority/block/journal checks, helper invocation, tracked/unstaged prerequisites,
snapshot preservation and separate operational closeout. Keep root/base identical.
Explicitly defer activation until implementation is accepted; retain strict mode
and the existing heavy exception meanwhile. No helper code, generator, role
authority, accepted contract or runtime behavior changes in this stage.

Use the documentation short route: LEAD prepares instructions, runs configured
README checks and commits; REVIEWER Astra/high statically checks the pinned
instructions against the approved contract. Only reviewer write:
docs/worklog/093-operational-review-instructions-review.md. Commit that report
using the current strict helper without --allow-dirty, verify report-only parent
and release ownership to LEAD. This review accepts the instructions as pending,
not as evidence that the option is implemented. Follow PROCESS and shared
ownership/check rules. Implementation remains a subsequent stage in this branch.

## Checks

With executable inputs unchanged from baseline and the updated template texts,
LEAD ran `python3 -m unittest discover -s tests -v`: 53 tests passed (23.047s).
`.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`
passed; `.venv/bin/python -m ruff format --check tools newproject.py tests
template/heavy/scripts` passed (8 files). `git diff --check` passed and `cmp`
confirmed root/base REVIEW-COMMIT are identical. These results cover current
behavior, not the unimplemented extension. Final staged diff check is part of
the sequential commit command; its actual result is passed to REVIEWER.
