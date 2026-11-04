# Adopt Ruff formatting

LEAD assignment; short mechanical route. Baseline:
`e30d588570c3ddae8dee556cdf8ab5b872b1494b`.
User wants a formatter after discussing its omission. Keep implementation simple.
Use existing Ruff 0.17.3 defaults to format newproject.py and
tests/test_newproject.py, preserving runtime behavior and every test assertion.
No new lint rules, dependencies, features or template changes.

Required sources: baseline code/tests, docs/specs/newproject.md and current root
rules. LEAD prepared README commands and ruff.toml comment correction; these
and this assignment are frozen in /private/tmp/newproject-format-assignment.
Developer must include these documents unchanged in the final snapshot/review.

DISPATCHER: gpt-6-luna / low. Forward this exact assignment to DEVELOPER
(gpt-6.1-terra / medium) then REVIEWER (gpt-6-astra / high).
Developer owns script/test formatting and docs/worklog/015-format-implementation.md.
Use /private/tmp/newproject-ruff-venv or isolated tooling; no global installs.
Freeze final code/tests/docs before decisive checks. Run full unittest suite,
Ruff check, Ruff format --check and verify AST equality against baseline for
both Python files (ignoring locations), plus diff whitespace check. Save exact
commands, versions, source hashes and outcomes, with raw check output if practical.
No new tests needed for pure formatting if assertions and behavior are preserved.

Reviewer statically checks exact frozen diff, unchanged AST/check evidence,
README/config accuracy and scope; no project execution. Write
016-format-review.md with identities, verdict and next owner. Route ordinary
fixes through dispatcher, documentation changes to LEAD. Preserve review rounds.
Stop at accepted review and return to LEAD for authorized local commit. No push
or actual sibling projects. Use followup_task to resume idle agents.
