# Move repository checks to Make

## Assignment and sources

LEAD specification. Baseline: `1bf77c0c9b6b51ccc6e73e16c49b1d74789ac516`.
Sources: `tools/python_check.py`, `tests/test_python_check.py`, README development
instructions, `docs/specs/python-check.md`, and root/base PROJECT-RULES at that commit.
HUMAN requested moving checks into a Makefile after discussing ordinary Make
failure behavior without a custom summary. Python is already a project dependency.

## Required outcome

- A root Makefile offers `check` (default), `format` (check only), `lint`, `test`,
  and `reformat` (apply formatting only), all phony.
- Preserve Ruff commands, target paths, and unittest discovery. Use Python 3 for
  tests and the existing `.venv/bin/python` for Ruff. No new packages.
- `make check` performs format, lint, and tests, with ordinary Make failure
  behavior; no custom summary or promise to continue after failure. Independent
  prerequisites may run concurrently under explicit `-j`; normal invocation is
  sequential. `make reformat` followed by `make check` replaces the old combined
  mode. Document `make -C PATH check` for invocation outside the repository.
- Remove the obsolete Python wrapper and its wrapper-specific tests. Replace
  its active specification with a Make check contract and update current links.
- Update README and root/base PROJECT-RULES to describe configured project check
  commands without imposing Python-specific tooling on generated projects.
  Make is a development requirement of this repository; do not add Makefiles or
  language tools to generated projects. Preserve generator behavior.
- No relocation of merge/review helpers, historical worklog rewrites, or unrelated
  process changes. No push or merge to main in this assignment.

## Ownership and routing

LEAD owns this specification, README, check contract, and both PROJECT-RULES files.
REVIEWER (Astra/high) reviews specification first, then the committed result,
statically; report paths `126-make-spec-review.md` and `128-make-review.md` under
docs/worklog. DISPATCHER (Luna/low) coordinates DEVELOPER (Terra/medium) after
specification acceptance. DEVELOPER owns Makefile, removed wrapper/tests, any
focused replacement tests needed, and `docs/worklog/127-make-checks-results.md`.
DEVELOPER may commit exact released LEAD files without editing them.

## Checks and acceptance

Before specification commit, LEAD runs existing configured checks for its
documentation-only change. DEVELOPER runs `make check` and verifies individual
targets, non-mutating formatting, reformat behavior on a temporary fixture,
failure propagation, and outside-directory invocation. Use focused meaningful
checks; do not add a test framework. Record commands, results and source identity.
Check active references for obsolete commands. Commit checked implementation and
released documentation together; freeze inputs during independent review.
Acceptance requires passing configured checks, consistent instructions, preserved
underlying check coverage, and independent ACCEPTED review. Return to LEAD after
review; do not publish or merge.
