# Individual check selection: implementation

Corrected approved contract `docs/specs/check.md` at
`11cf4cc60d9f353946c86d10b77c98dff31dae30` (Git blob
`799c623f228cae0188e933f62ad2a6dcb911e1c6`), covered by conditional acceptance
in 114 and exact closure in 113. Starting HEAD was `11cf4cc60d9f353946c86d10b77c98dff31dae30`
on `codex/check-helper`, initially clean.

The helper accepts `--only format|lint|tests`, runs and reports only that step,
and rejects `--reformat` with lint or tests before starting checks. The default
full sequence and failure/interruption behavior remain intact. Tests cover each
selection and exact arguments, formatter write/check variants, flag propagation,
argument orders and invalid combinations, and selected failures, launch errors
and interruption. Existing full-run and temporary-file formatting tests remain.
Selected tests may themselves require Ruff; the wrapper does not skip tests.

Checked SHA-256:

- `tools/python_check.py`: `3117185dce9f4862291736beaefbdb3786ee4fdf99ee8132048a97df1dabc331`
- `tests/test_python_check.py`: `62008616207650e88e2602367a65af2a2f93657b163fd00c1b99ff6f5a2cb7fc`

Python 3.9.6, Git 2.54.0, Ruff 0.17.3. Final
`python3 tools/python_check.py --reformat` exited 0: format exit 0 (ten files
unchanged), lint exit 0, tests exit 0 (69 passed in 23.875s). Focused helper
tests passed before the full run. `git diff --check` and final
`git diff --cached --check` passed. Earlier successful full runs were repeated
after test coverage and help wording changes; no executable failure remained.
No unrelated files changed. Independent implementation review is pending.
