# Sequential repository checks: specification review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`59da9b0c8fe096a5ca2587e6d68222563f083cf4`, on `codex/check-helper`.
The specification was introduced at
`d9640903daae407fe186d1c84c6f97c1ea6c8285`; the later checkpoint updates task
routing only. Baseline: `1be232c2bfd84912688c9f9491168873e73d87b1`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/102-check-helper-spec-review.md`.

## Scope and conclusions

Static review covers `docs/specs/check.md`, task 101 and the existing README check
commands, under the repository's standard specification-review process. No
blocking findings.

The proposed helper is a bounded repository-specific wrapper. Its literal command
arguments match the documented lint, formatting-check and unittest invocations.
The sequence is explicit: lint, format check, tests, with no parallel execution.
Ruff uses the local virtual-environment interpreter; tests use the invoking
interpreter. Repository-root execution is independent of the caller's directory.
No dependency installation, format fixes, Git mutation or template/generator
adoption is introduced.

Failure handling distinguishes launch errors and nonzero child results, attempts
all three checks after ordinary failures and returns success only for three
successes. User interruption is explicitly separate: stop the sequence, do not
start remaining checks and do not claim completion. Output labels/commands flush
before child execution, child output streams directly, and the final summary
names each result. Help and parser errors require no check execution or Ruff.
These requirements are coherent and testable without introducing a scheduling
or logging framework.

The verification scope covers commands/order/cwd, continuation, statuses/output,
parsing and interruption using bounded substitutions or fixtures, with an explicit
ban on recursively launching the real suite from wrapper tests. Final validation
uses the actual helper and retains all three underlying results plus its overall
result. The ordinary check ownership and checkpoint rules remain unchanged.

README and any repository-specific reference adoption are routed through LEAD
before final implementation checks and the source checkpoint. No worker may
merge into main or push: completed work must remain on `codex/check-helper` under
HUMAN's latest instruction.

## Evidence and limitations

Task 101 records 59 passing unittest cases (28.701s), passing configured Ruff
lint and formatting checks (eight files), and a passing working-tree whitespace
check on unchanged baseline executable/template inputs. LEAD additionally
reported successful staged whitespace checks before both documentation commits
in sequential commands, exit code 0, chunks `b95927` and `a4382f`.

REVIEWER ran no project checks. These results cover the existing repository,
not the unimplemented wrapper. Adding only this report does not alter checked
inputs. Implementation and final documentation still require their own checked
source checkpoint and independent acceptance.

## Handoff

Commit only this report using the accepted strict report-helper invocation with
the initial HEAD above; verify the report-only direct child and clean repository
state, then release writer ownership to LEAD. Return the report commit separately
from the approved specification identity. LEAD may release this exact checkpoint
to DISPATCHER for implementation. Leave all resulting work on the task branch.
