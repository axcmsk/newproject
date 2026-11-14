# Instructions as implementation review

## Identity and verdict

- Verdict: `ACCEPTED`; no findings or open conditions.
- Specification: `docs/worklog/160-instructions-implementation-task.md` at
  `ca1a1b8e62d7fb16b822ff22c1213f4d4bb7f060`.
- Reviewed source and frozen review-start HEAD:
  `ca1a1b8e62d7fb16b822ff22c1213f4d4bb7f060`.
- Baseline: `47ca65588e2ea4372bd5d2333c071bee16514793`.
- Independent REVIEWER scope: task record, six changed root/base policy files
  and their consistency with the existing three routes and shared check rules.
- Exclusive write: this report only, in the isolated review worktree. Source
  files were not modified.

## Assessment

AGENTS Scope now states the shared principle directly: code and agent
instructions are implementation, assessed by behavioral effect regardless of
file format. It explicitly rejects punctuation, file extension or the label
of a typo as sufficient grounds for exemption.

The revised example in AGENTS and PROCESS limits the obvious-correction route
to explanatory spelling changes that leave behavior and meaning unchanged.
The surrounding requirements, authority and process boundaries remain intact;
an instruction whose effect changes is not exempt merely because it resembles
a small textual correction. The three routes, independent review obligations,
check ownership, evidence, coverage, frozen-input and permission rules are
unchanged.

MAIN-MESSAGE references the shared principle rather than defining it separately.
Its relative link, `../../AGENTS.md#scope`, resolves to the corresponding AGENTS
file and existing Scope heading in both root and base trees. Its existing
commit-type distinctions remain consistent with the shared rule.

Each changed root policy file has the same Git blob identity as its base
counterpart. The complete diff contains only the six permitted policy files
and task record; no code, tests, CV material or data process changed.

## Evidence and handoff

Inspected `/tmp/instructions-implementation-checks.log`: Ruff formatting and
lint passed; unittest reports 75 tests and `OK`. LEAD reports `make check`
exit 0 and successful `git diff --check` for the checkpoint inputs. These are
supplied execution results. REVIEWER performed static review only and ran no
project tests, validators, coverage collection or CI.

Next owner: LEAD. Verify and integrate the report-only commit above the reviewed
source, then report completion within the authorized local scope. No push or
publication is authorized. Report writer ownership is released after a
successful report commit.
