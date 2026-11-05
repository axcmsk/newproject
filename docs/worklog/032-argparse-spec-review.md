# Standard CLI parsing specification review

- Verdict: `ACCEPTED` for the specification.
- Reviewed source: `1cef241f0a9893a63c35f906449508acfdb17e47`.
- Baseline: `c08f743aa6c553fe59fd5b0384049b26106f9fb6`.
- Contract: `docs/worklog/031-argparse-task.md` and revised
  `docs/specs/newproject.md`, with the README help example, at the reviewed source.
- Scope: concise parser-change requirements, authority, regression boundaries
  and verification obligations. Implementation acceptance is excluded.
- Findings and conditions: none.
- Next owner/action: LEAD may release this exact contract to DISPATCHER for
  implementation. Reviewer writer ownership is released.

The contract consistently replaces bespoke argument parsing with standard
argparse semantics. It distinguishes help success and syntax-error status 2
from the retained domain/creation failures, requires parsing before source/Git/
target operations, accepts repeated boolean flags and preserves the standard
terminator without either custom dash-name compatibility or a separate ban.
The specification removes the superseded duplicate-flag refusal and unrestricted
dash-name behavior. Required help/error, normal/heavy, terminator and repeated
flag cases are testable without fixing version-dependent diagnostic prose.

Scope, write ownership, source references, review routing and checks are bounded;
template composition, journal behavior and domain safeguards remain unchanged.
The README addition matches the intended interface. Existing workflow rules are
unchanged, and no additional behavioral or authority conflict was identified.

The task records prior passing 25-test, expanded lint and format results on
unchanged executable inputs. Those supplied results remain applicable to this
documentation checkpoint; fresh implementation checks are still mandatory.
REVIEWER performed only static inspection, with no executable checks or commits.
Review-start HEAD matched the source and the working tree was clean. At closeout
HEAD remained unchanged and only this permitted review report was added.
