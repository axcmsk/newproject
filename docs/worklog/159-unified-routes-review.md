# Unified task routes review

## Identity and verdict

- Verdict: `ACCEPTED`; no required corrections or open conditions.
- Specification: `docs/worklog/158-unified-routes-task.md` at
  `f8d81d37d0faf8af338364431b00d01882c85182`.
- Reviewed source and frozen review-start HEAD:
  `f8d81d37d0faf8af338364431b00d01882c85182`.
- Baseline: `bc98622522cfbf168ab5796d09256139c83d0bde`.
- Independent REVIEWER scope: the task record and eight changed root/base policy
  files, including consistency with retained role, check, coverage, authority,
  conditional acceptance and report-commit rules.
- Exclusive allowed write: `docs/worklog/159-unified-routes-review.md` in the
  isolated `codex/unified-routes-review` worktree. Source files were not edited.

## Findings and assessment

No blocking findings. The three routes match the final task requirements and
replace the overlapping short/documentation and direct routes. Selection is
explicitly based on the work rather than the file type:

1. Obvious corrections need checks but no task specification or independent
   review when behavior, meaning, requirements, authority and process are
   unchanged. A comment typo is expressly covered. Routine exempt content keeps
   lightweight handling within the stated boundaries. AGENTS explicitly gives
   these scope rules priority over role/check ownership rules, so LEAD can
   perform the applicable checks for an exempt correction in a code file.
2. Direct work requires a retained brief before implementation when doing the
   work is clearly easier than explaining it to DEVELOPER. The brief records
   intended change, scope and verification, is included in the review handoff,
   and serves as the specification without requiring a separate file. LEAD
   implements, checks, saves evidence and submits the exact brief and source to
   an independent REVIEWER for joint review. The prior mandatory standalone
   specification requirement is superseded consistently.
3. Delegation retains the full specification and standard approval/implementation
   sequence. If direct work ceases to be clearly easier, transfer is required,
   with the brief, changes, findings and evidence, any necessary specification
   expansion and explicit writer/runtime ownership transfer. Missing
   specification approval precedes resumed dependent work.

Independent review remains required for behavior/rule changes, including in
text files. Authority changes require review before reliance. Retained REVIEWER
rules keep review static-only; direct-route substitutions reconcile routing and
check ownership with the other role guides. Configured coverage, execution
recovery, source/evidence identity, checked commits, frozen inputs and report
history remain required. Conditional closure still permits only the prescribed
comparisons and sends mismatches or semantic evidence questions to REVIEWER;
LEAD does not gain self-acceptance authority.

Root/base AGENTS, PROCESS and LEAD have identical Git blob identities. Shared
PROJECT-RULES content is identical; the root-only repository purpose section is
unchanged. No stale short-route references were found in active root/base/heavy
policy or README. No new link targets, special data process, CV edits,
executable source changes or test changes were introduced.

## Evidence and limitations

Inspected LEAD's `/tmp/unified-routes-checks.log`: Ruff formatting and lint pass;
unittest reports 75 tests and `OK`. LEAD reports `make check` exit 0 and successful
`git diff --check` for the task's checkpoint inputs. These are supplied results;
REVIEWER executed no project tests, validators, coverage or CI. Acceptance is
based on independent static policy review and the supplied check evidence.

Next owner: LEAD. Verify that the resulting report commit changes only the
assigned report above the reviewed source, integrate it into the original
checkout and report the accepted local result. No push or publication is
authorized. Report writer ownership is released after the report commit succeeds.
