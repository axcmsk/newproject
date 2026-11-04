# Small script refactor and lint

Owner: LEAD. Baseline: 1c8b3d276b260259297f25a85a6e3875bb57bd13.
Route: short, behavior-preserving mechanical refactor under PROCESS.
User asks to structure the 90+ line main function and asks whether linters ran.
Prior checks were unittest, static review and diff whitespace checks, not lint.
User preference: keep the tool simple; simplify rather than add machinery.

Required sources: newproject.py, tests/test_newproject.py,
docs/specs/newproject.md, README.md at the baseline commit; current root rules.
Extract cohesive helpers for input/source/target validation, Git operations and
copying so main reads as orchestration. Preserve CLI arguments, return codes,
diagnostics, preflight ordering, mutation tracking, environment isolation and
filesystem/Git effects. Keep one script, standard-library runtime and Python 3.9+.
No new features, architecture layers, runtime packages or template changes.

DEVELOPER (gpt-6.1-terra / medium) owns newproject.py, tests/test_newproject.py,
minimal lint-only configuration/development dependency file if useful, and
012-refactor-implementation.md. Keep test assertions intact; change tests only
as required by extraction or lint, adding targeted regression coverage if a real
gap is found. Run full unittest suite and Ruff lint on script and tests; formatter
check is welcome if adopted consistently. Prefer isolated temporary tooling or
local environment; do not install global packages. If unavailable, report actual
reason rather than claiming lint passed. Scope permits acquiring Ruff as dev tool.
No web research is required for a local refactor; use installed tool help.
Freeze code/tests/config before decisive checks and save identities, exact commands,
versions, outcomes and limitations. Compare affected callers and error paths to
baseline as evidence of preservation.

DISPATCHER (gpt-6-luna / low) forwards exact assignment, routes developer result
to independent REVIEWER (gpt-6-astra / high), and manages routine corrections.
Reviewer writes 013-refactor-review.md, statically assesses frozen source,
regression strength, behavior preservation and saved lint/test evidence. Do not
execute project checks or edit reviewed code. Preserve rounds. Requirements or
scope questions return LEAD; suggest README tooling instructions to LEAD early.
LEAD owns substantive documentation, supplies README changes for the same review,
and commits accepted changes. No pushes or actual sibling projects.

Tooling clarification from LEAD: Ruff 0.17.3 is available in an isolated temporary
environment. README now documents an optional local .venv with that pinned tool;
include this README revision in the reviewed snapshot. DEVELOPER may update
.gitignore for .venv/ and .ruff_cache/. No dependency file or formatter is required.
