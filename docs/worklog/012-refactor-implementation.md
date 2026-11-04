# Refactor implementation evidence

Assignment: `docs/worklog/011-refactor-task.md`, frozen v2 at
`/private/tmp/newproject-refactor-task/011-refactor-task-v2.md`, SHA-256
`fa78bb3be143bc812063bf2a55b4d1dbef187b4c8444ed4bbb9fe5e158ca490d`.
Baseline: `1c8b3d276b260259297f25a85a6e3875bb57bd13`.

Before decisive checks, saved copies of the reviewed files in
`/private/tmp/newproject-refactor-implementation/` (`gitignore` is the copy of
`.gitignore`). The following identities identify both the saved copies and the
checked working files; Git blob IDs are calculated without staging:

| Path | SHA-256 | Git blob ID |
| --- | --- | --- |
| `newproject.py` | `d29ada69d91569b7ffe6089855b4965b76d65de8d8bf2105fdd9ee57958f7b30` | `42764cacea9b01384f5b99780625566fa965db03` |
| `tests/test_newproject.py` | `03d399d1950bb2c6f0243e56770d16ef63efeb31410a362555683b66f6cd20a9` | `0682035f29b6bb61d6b776961e5cf6915acef49b` |
| `.gitignore` | `2ae588e5272f8e21829ee6c5a5bb3a9dbbd545f20baca25693bafe45df1f6021` | `0fd623a049c0bbf64df9ff69a393e4926ee717a0` |
| `README.md` | `add6d6833e05bec6885d3d07a0a8a41979eade2d8a151b98205eb5ad9195a2eb` | `6800c3f0d4a58e17212af1b0d9b9c1ca896408ea` |
| `ruff.toml` | `9e4bbda689c57f626f6e52041d84ef9e020e9d5e01137f595f81837d260e7efc` | `71b61368bf924aa772e50377ce5360bbaee47be4` |

## Comparison to baseline

The CLI and injected-failure tests still call `main()` or the script as before;
assertions were retained. Test edits only split multiple statements for lint.
`main` retains target and environment construction, exception handling and
mutation tracking. It calls extracted input/source validation, Git setup and
version check, target validation, initialization, and copy in the same order as
the baseline. Git arguments and sanitized environment, target checks and refusal
messages, exclusive file creation and metadata copy remain unchanged. The
mutation marker remains after successful target mkdir and before either Git
mutation, so preflight and partial-state diagnostics retain their distinction.
The suite covers successful new, empty and existing repositories, refusals,
environment isolation, and injected traversal, init and copy failures. This is a
source comparison and test evidence, not independent review or proof of every
possible filesystem condition.

## Checks

Environment: Python `3.9.6`, Git `2.54.0`, Ruff `0.17.3` on this machine.
Ruff was installed in `/private/tmp/newproject-ruff-venv`, not globally. The
initial network-restricted installation failed to resolve the package host;
installation with permitted network access succeeded. The first plain Ruff run
reported eight findings (EXE001, I001, UP022,
PLW1510, C401); an explicit E4/E7/E9/F run also identified existing E701/E702
test formatting. Test statements were split, and `ruff.toml` now fixes the
intended E4/E7/E9/F selection locally. No formatter was adopted.

Decisive commands, run from the repository against the identities above:

- `python3 -m unittest discover -s tests -v`: exit 0, 11 tests, `OK` (2.591s).
- `/private/tmp/newproject-ruff-venv/bin/python -m ruff check newproject.py tests/test_newproject.py`: exit 0, `All checks passed!` The local configuration is picked up by the plain command documented in README.
- `git diff --check`: exit 0, no output (also rerun after adding `ruff.toml` and this report).

No real sibling project was created. Checks were run on Python 3.9.6 only; other
supported Python versions were not exercised. No commits were made.
