# Optional reformat mode: implementation

Approved specification: `docs/specs/check.md` at
`939b29f415fe7a4eee7b95504c6992cb0df20778`, accepted in 106 at
`00acdf212b6aaaa445694a4432bd8b951f5eb3bc`, the clean starting HEAD on
`codex/check-helper`. Assignment: 105.

`--reformat` selects formatter write mode, then lint and tests; the default
sequence remains lint, format check and tests. Both use the same targets and
retain failure continuation and interruption handling. Focused tests assert
flag propagation, exact commands and order, three steps, default behavior,
formatter failure and launch error continuation, and real formatting of an
unformatted file in a temporary fixture without recursively running the suite.

Checked source SHA-256:

- `tools/check.py`: `6c2339fa1f35d7364961aee1907bdc5023514625818e38de84dd415621fff16b`
- `tests/test_check.py`: `6d376433810fe72944bad1862942656befb62b97661eecc38e23f87a26f88247`

Python 3.9.6, Git 2.54.0, Ruff 0.17.3. The final actual command
`python3 tools/check.py --reformat` exited 0 with these sequential results:

1. Ruff format: exit 0; ten files left unchanged.
2. Ruff lint: exit 0; all checks passed.
3. Unittest: exit 0; 66 tests passed in 24.470s.

No unrelated files changed. `git diff --check` and final
`git diff --cached --check` passed. Under the approved project exception, no
additional format check or full suite was run on unchanged inputs. Initial focused
checks found import ordering and a temporary virtual-environment symlink that
could not locate Ruff; both were corrected and the focused seven tests passed
before the final run. Independent review remains pending.
