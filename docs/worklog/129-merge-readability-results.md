# Merge helper readability: implementation evidence

- Assignment: short-route behavior-preserving extraction of post-commit result verification from `perform`, returning HEAD to its caller. No policy, mode selection, CLI or other behavioral changes; allowed source change is `tools/merge.py`.
- Baseline: `eb32adc8906143a87ae16238bb657a6a56931d41`; authoritative inputs: `tools/merge.py`, `docs/specs/merge.md`, `tests/test_merge.py`, and `Makefile` at that baseline.
- Change: moved the post-commit HEAD, parent, branch and clean-state verification into `verify_result`, called at the original location inside the same `try` block. It returns the same HEAD used by the success message. The same commands and conditions execute in the same order, including `or` short-circuiting; exceptions still reach the same handler with unchanged messages. The squash check and all other callers and effects remain unchanged.
- Checks on the changed source: `make check` passed (format and lint passed; 59 tests passed). The first `make check` stopped at formatting because the extracted condition needed reflow; after reflow the full command passed. No new tests were added for the extraction.
- Diff inspected with `git diff -- tools/merge.py`; only the described extraction and formatting reflow were present. Independent review remains required.
