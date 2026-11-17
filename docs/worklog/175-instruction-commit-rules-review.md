# Instruction commit requirements review

## Inputs and scope

LEAD's direct-route brief records the user's approval to include commits in
the requirements applied equally to agent instructions and program code,
without duplicating project commit rules. Review only this list addition in
the Agent Instructions section of `agent-personal/ENGINEERING.md`.

- Personal repository base: `8363b2daacedc26d166e35c920780bfdb9b280db`.
- Reviewed source: `987034bb3e92f714070809d30b3b1135d6652f30`.
- Frozen newproject HEAD: `a446c9ba63bea8efea477ee9ed6df19a947e683c`.
- Only allowed report: `docs/worklog/175-instruction-commit-rules-review.md`.

## Review and evidence

No findings. The complete pinned diff adds commits alongside checks and
independent review in the existing same-requirements sentence. It preserves
the surrounding instructions and introduces no separate commit policy,
format, sequence, or authorization. This matches the approved refinement.

LEAD reports passing an assertion for the exact sentence substitution and
staged `git diff --check`. REVIEWER inspected the diff and repository state
statically and ran no executable checks. The personal repository has no
configured check suite. Newproject executable sources remain unchanged;
previously inspected passing checks in `/tmp/common-check.log` remain
applicable to those sources. The unrelated personal `.idea/` was preserved.

## Verdict

`ACCEPTED` for the named brief and reviewed source. Return to LEAD for closeout;
report writer ownership is released after the report helper commits this file.
