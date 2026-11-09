# Python check helper cleanup

Short-route assignment on baseline `fec52b31596e411a716266ac2d11aa8d121d0234`,
branch `codex/check-helper`. LEAD released the existing specification edit for
unchanged inclusion. The tests now use an independent literal target list, omit
unused temporary virtual-environment symlink setup while retaining the bounded
real formatter substitution, and use `python_check.py` in fake argv. The helper
docstring reflects format, lint, tests order. Runtime behavior is unchanged.

Checked SHA-256:

- `tools/python_check.py`: `3a506fff4aad80086594ae8281d517f35d7311028a7e8b354c98433906a614b8`
- `tests/test_python_check.py`: `03bab9e31662eb766451a03c9ca3b9b83ca6c591667d12628aa744968e6010ea`
- LEAD-released `docs/specs/python-check.md`: `39930bf5d4ea36b1435d2c9bf0a31642de86e3a60f4f2d6bcd37ee94792b4539`, unchanged.

Python 3.9.6, Git 2.54.0, Ruff 0.17.3. The actual configured command
`python3 tools/python_check.py --reformat` exited 0: format 0 (ten files
unchanged), lint 0, tests 0 (69 passed in 27.225s). The temporary-file formatting
test passed. `git diff --check` and final `git diff --cached --check` passed.
No unrelated files changed; independent static review is pending.
