# Shared project merge workflow specification review

- Verdict: `ACCEPTED` for the specification.
- Reviewed source and review-start HEAD:
  `9115bc08c994507f95edf851dee40c04ae576711`.
- Baseline: `1aaf963e9975ab89cacc41b5a948dc5256c0dbd0`.
- Contract: task 074 and `docs/specs/newproject.md` at source.
- Scope: shared helper installation, workflow alignment and required verification.
  Implementation and generated-project execution are not yet accepted.
- Findings and conditions: none.
- Next owner/action: LEAD releases this exact contract through DISPATCHER;
  DEVELOPER implements and runs the expanded checks before implementation review.

The contract defines one authoritative helper source outside the template layers,
its fixed installed path, byte/mode preservation and cwd-independent lookup. It
requires source validation and selected-layer collision refusal before target
mutation, permits ordinary shared tools directories, retains exclusive destination
creation, and preserves help/error behavior without requiring the helper source.
These additions fit the existing layer union and preflight guarantees without
requiring a general copying framework or changing merge behavior.

Both variants receive the same three guides and helper. Normal keeps optional
branches; heavy retains its task branches/checkpoints while delegating merge mode
and procedure to the common rules. The assignment explicitly removes the old
heavy no-ff/approval restriction and deferred-integration wording while preserving
reviewed source history, role boundaries and no publication authority.

Required verification covers installed bytes/mode, both real generated-project
merge paths, message/result/source state, helper-source failures, layer collisions,
allowed directories, normal independence, help and copy-time no-overwrite behavior,
alongside existing regressions. Fresh implementation checks are required because
code and template inputs will change; old results cover only this spec checkpoint.

REVIEWER performed static inspection only. Review began at the exact source with
a clean tree. Commit only this report after HEAD/index/path verification, return
its actual hash separately and release ownership. No checks, source edits, merge
or push were performed.
