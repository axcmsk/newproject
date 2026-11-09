# Review helper entry point refactor

Baseline: `af3bc705ffe6258138e2dbf2f7a73246cab86373` on
`codex/review-commit-allowed-dirty`, initially clean. LEAD assigned a small
behavior-preserving mechanical refactor under the short route: shorten the
entry point by extracting coherent responsibilities, preserving CLI behavior,
messages, Git check and mutation order, hooks and environment safety. No
`--allow-dirty` behavior, requirements, generator or other documentation changes
are included. Allowed implementation and evidence paths are
`tools/review_commit.py` and this record; independent static review is pending.

Argument parsing, environment validation, message/repository validation, report
commit sequence and failure reporting now have named functions. The entry point
keeps argument parsing before exception handling and only enables diagnostic Git
after environment validation succeeds. The Git calls, conditions and error
messages retain their prior order. The former C901 suppression is no longer
needed. No tests were changed.

Checked `tools/review_commit.py` SHA-256:
`21c2259df3c5c6740dba54640088c9c844cdce3caa2f027670e91b0c5bb03957`.
Python 3.9.6; Git 2.54.0.

- `python3 -m unittest discover -s tests -v`: 53 tests passed (21.594s).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`:
  passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`:
  passed; eight files already formatted.
- `git diff --check` and final `git diff --cached --check`: passed.

The suite exercises temporary repositories, including installed helper success,
refusals, hooks and unsafe environment handling. No real report commit was made
with the refactored helper; this checkpoint uses Git directly. The unchanged
suite and developer inspection are evidence, not independent acceptance.

## Naming correction

After checkpoint `f8122e9d5f8ec551bacb21060ce3677a7adc49e8`, LEAD noted
that `validate_repository` also checks the message. It was renamed `preflight`
without changing behavior. Corrected script SHA-256:
`5a55c281bd5f3f18aff1dcd287215c74546b2b6449d23310d7d3af066ff542ac`.
The same full unittest command passed 53 tests (21.805s); both README Ruff
commands passed again (eight files formatted). Final `git diff --cached --check`
passed for the correction and this evidence.
