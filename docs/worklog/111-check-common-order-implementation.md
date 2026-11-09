# Common check order: implementation

Approved specification `docs/specs/check.md` at
`efae4c464ad25a03bfb0f1a73b12ac390275a3cf`, accepted in 110 at
`0b0ed3e6f1275faa738eab800eadf64f2d9bb3f4`, the clean starting HEAD on
`codex/check-helper`. Assignment: 109.

Both modes now run format, lint and tests in that order. Only the default
format command adds `--check`; the mode-dependent ordering branch was removed.
Tests assert the default order, arguments and summary, the reformat order and
failure continuation, and the adjusted error labels. Other behavior is unchanged.

Checked source SHA-256:

- `tools/check.py`: `f29e60f2f2534523f7df7099360f71795f58f4e46941a82161a77014f6598023`
- `tests/test_check.py`: `d6d03f031918bb75138098b1b18de05f014984105b0579ffdb2216cc584c3df5`

Python 3.9.6, Git 2.54.0, Ruff 0.17.3. The final actual command
`python3 tools/check.py --reformat` exited 0: format exit 0 (ten files unchanged),
lint exit 0, tests exit 0 (66 tests passed in 27.930s). The focused seven helper
tests also passed. No unrelated files changed. `git diff --check` and final
`git diff --cached --check` passed. No additional full suite or format check was
run on unchanged inputs under the approved exception. Independent review is pending.

## Naming follow-up

HUMAN chose `python_check`; following checkpoint
`ae9039bf5998ca6020c5c857b6387ee4b1bcb9b4`, LEAD released the naming updates
in README, specification, PROJECT-RULES and 109. Their SHA-256 identities are,
respectively, `71ef9110a1dae776ab680ae28593aab5854497c7b6afaa6f1d17b32a6deac70c`,
`3c1388bc4362c36cda167affa37059bfb0e74ca4bd808e28fd87fe3b3d9e741e`,
`c46749aa17507f938a96390889735011c7f6ae9078f4c75ed2c8a4ba7d6a7bb9` and
`9ac068fbcf0c743b89230d5741e50f7872f87fda75b2c2c26dd91bcae79e7ec4`.
The helper and test were mechanically renamed to `tools/python_check.py` and
`tests/test_python_check.py`; only the test fixture's helper path changed.
No compatibility alias was added.

Final source SHA-256: helper
`f29e60f2f2534523f7df7099360f71795f58f4e46941a82161a77014f6598023`, test
`388c434db82cce23d23ca70e1fa3088ccd68032912ee2779c2ce94a60d11cdf7`.
Python 3.9.6, Git 2.54.0, Ruff 0.17.3. The actual configured command
`python3 tools/python_check.py` returned 0: format check 0 (ten files already
formatted), lint 0, tests 0 (66 passed in 27.270s). `git diff --check` and
final `git diff --cached --check` passed. No unrelated changes were observed;
independent review of the combined outcome remains pending.
