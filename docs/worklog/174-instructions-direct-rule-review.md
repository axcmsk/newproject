# Direct instruction wording review

## Inputs and scope

LEAD's direct-route brief records the user's refinement: always treat agent
instructions as code. Review only the first-sentence substitution in the
Agent Instructions section of `agent-personal/ENGINEERING.md`.

- Personal repository base: `aea6e526867e6f349012df90af8d03bf37022e23`.
- Reviewed source: `8363b2daacedc26d166e35c920780bfdb9b280db`.
- Frozen newproject HEAD: `49977b8fc29c5894ed5ea7059b963b1024759210`.
- Only allowed report: `docs/worklog/174-instructions-direct-rule-review.md`.

## Review and evidence

No findings. The new sentence directly instructs the agent to always treat
agent instructions as code, regardless of file format, and preserves the
explanation that they define system behavior. The checks and independent
review sentence is unchanged. The complete pinned diff contains only the
requested sentence substitution and matches the user's refinement.

LEAD reports passing an assertion for the exact sentence substitution and
staged `git diff --check`. REVIEWER inspected the diff and repository state
statically and ran no executable checks. Personal instructions have no
configured test suite; newproject executable sources remain unchanged, so the
previously inspected passing checks in `/tmp/common-check.log` remain applicable
to those sources. The personal repository's unrelated `.idea/` was preserved.

## Verdict

`ACCEPTED` for the named brief and reviewed source. Return to LEAD for closeout;
report writer ownership is released after the report helper commits this file.
