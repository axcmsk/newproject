# Shared project merge workflow implementation

Approved contract: `docs/specs/newproject.md` and `docs/worklog/074-project-merge-workflow.md` at `9115bc08c994507f95edf851dee40c04ae576711`; specification accepted in `docs/worklog/075-project-merge-spec-review.md` at `ad32e4e4b6d0b674ba5e9e05c7c4309db2402e0e`. Implementation started at that HEAD, with LEAD's exact released workflow and README edits present. The tested source is committed with this report. `tools/merge.py` remains unchanged.

The generator preflights the real helper directory and readable regular file, rejects reserved path collisions in selected layers, and installs the helper through the existing exclusive-copy path. Tests cover missing, symlink, special and unreadable helper sources; layer file/directory collisions; shared tools directories; help without the source; and injected copy-time collision preserving the appearing file. Existing normal independence and creation safeguards remain covered. Both real-template variants verify installed helper bytes/mode and all three guides, then perform actual isolated Git merges and check message, output content, clean status and preserved source tip.

Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3.

- `python3 -m unittest discover -s tests -v` — passed, 43 tests in 15.028s (`OK`).
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts` — passed (`All checks passed!`).
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts` — passed (`6 files already formatted`).
- `git diff --check` — passed.

A preliminary injected read test used an unresolved temporary-path spelling and did not reach its intended condition; the fixture was corrected to compare resolved paths, and the focused and full suites passed. Real merges were confined to temporary generated repositories; no development branch was merged or pushed. Checks ran on this host only; independent review remains pending.
