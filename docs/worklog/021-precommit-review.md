# Precommit policy review

Independent REVIEWER static review of the documentation short route.

## Exact inputs

Baseline: `028beb003d1dc3f4958a7db8b4bd0c7244cf13d0`.
Frozen root: `/private/tmp/newproject-precommit-rules-v1`.
Paths below are relative to that root; identities are SHA-256.
The working copies matched these identities at review time.

| Input | SHA-256 |
| --- | --- |
| `docs/worklog/020-precommit-task.md` | `7ee379c63c6c53a634d2b41e7471643352ee4b9651e53596df2b47e7cffd1dd4` |
| `docs/workflow/PROJECT-RULES.md` | `1ca937209fc986daf0bf24e6da9a4ba57ec1abd9108ea59528bb52ea6c1b18de` |
| `docs/workflow/PROCESS.md` | `345046069f8aefb32971d94242bb7973643edc9314907e88c44f511a79369120` |
| `template/docs/workflow/PROJECT-RULES.md` | `89824f657eb37de35cfec2a49841dc361502eeab1d975288c86efda34540ab82` |
| `template/docs/workflow/PROCESS.md` | `345046069f8aefb32971d94242bb7973643edc9314907e88c44f511a79369120` |

Required context: root and template AGENTS, REVIEWER guide, baseline PROCESS,
and README's documented commands. No project code, tests, linter, formatter or
CI was executed by REVIEWER.

## Scope and findings

The four policy documents satisfy the requested requirement to run configured
tests, lint and formatting checks before every commit, including documentation.
They require passing results, distinguish absent checks from unavailable
configured checks, and require reruns when checked inputs change. Formatting
uses check mode. No new tooling, hooks or runtime implementation is mandated.

The added policy is identical in root and template PROJECT-RULES; PROCESS is
identical across both copies. Removing the former documentation execution
exemption resolves its conflict with the new requirement. LEAD may execute
checks for documentation-only work; logic checks remain DEVELOPER-owned and
REVIEWER remains static-only. The documentation route still requires only the
assignment and independent review, without a delegated document author.

No blocking findings in the four policy documents.

Closeout observation: the assignment's last paragraph allows check evidence
only in the final response, but PROJECT-RULES limits that option to routine
work without a worklog. This task has a worklog. Record commands, outcomes and
the checked version in existing task evidence, or explicitly resolve the
task-specific evidence exception. This does not require another evidence file
or changes to the accepted four policy documents.

## Verdict and next action

`ACCEPTED` for the four named policy documents, by static review only.
This verdict does not assert that precommit checks have passed or authorize
skipping them.

Return directly to LEAD. Resolve the evidence-location observation, run all
configured README checks for the version to be committed, and record actual
results and source identity. Commit the accepted documents and records only
after those checks pass. No further review of identical policy content is
needed; changed policy text requires review of the affected revision.

## Revision 2 review

User clarification via LEAD requires changes, passing configured checks,
independent review, then commit. Reviewed frozen root:
`/private/tmp/newproject-precommit-rules-v2`, same baseline as above.

| Input | SHA-256 |
| --- | --- |
| `docs/worklog/020-precommit-task.md` | `54bf95ea77a3d3c09aceb5e0813f5c8a0493429a6f35f51ab0907f37402c5a94` |
| `docs/workflow/PROJECT-RULES.md` | `43c0e8a17c7fa8b817072718080b1fc6320fd4fd1b553ae0eae8f7e174755ebb` |
| `docs/workflow/PROCESS.md` | `20f1c503763a753ba431dc8275fc60efc2471360c1bfadf8773db2006be0bdbd` |
| `template/docs/workflow/PROJECT-RULES.md` | `0a50501272dd967e9981698adfa665865c23367e3d56e17859769c115701f28b` |
| `template/docs/workflow/PROCESS.md` | `20f1c503763a753ba431dc8275fc60efc2471360c1bfadf8773db2006be0bdbd` |

The revised assignment records passing unittest, Ruff lint and Ruff formatting
results before this submission, with exact checked source/configuration blobs.
The recorded blobs match current files. REVIEWER inspected these saved results
and source identities, without rerunning checks. The v1 evidence-location
observation is resolved. Root/template policy remains aligned.

Finding V2-1: both PROCESS files, short route for mechanical code changes,
still permit freezing source with a commit before decisive checks. This conflicts
with the new explicit checks, review, commit order and can direct a premature
commit. Closure: remove that pre-check commit option and require a saved
snapshot with content hashes in this step. No application changes or additional
check report are needed.

Verdict: `CHANGES_REQUESTED` for revision 2 due to V2-1. Next owner: LEAD,
apply the matching correction in both PROCESS copies and return the frozen
revision for static review. Other reviewed changes have no blocking finding.

## Revision 3 final review

Reviewed frozen root: `/private/tmp/newproject-precommit-rules-v3`, same
baseline. Working copies match these frozen identities.

| Input | SHA-256 |
| --- | --- |
| `docs/worklog/020-precommit-task.md` | `fd97aef444b267860d822206bd3ea4da8cf38d6f156a0d86ac7f95f640898535` |
| `docs/workflow/PROJECT-RULES.md` | `43c0e8a17c7fa8b817072718080b1fc6320fd4fd1b553ae0eae8f7e174755ebb` |
| `docs/workflow/PROCESS.md` | `88efd788eca4ca6b1404f71bc285644b8739576faaac917f5d285a8ed1894e21` |
| `template/docs/workflow/PROJECT-RULES.md` | `0a50501272dd967e9981698adfa665865c23367e3d56e17859769c115701f28b` |
| `template/docs/workflow/PROCESS.md` | `88efd788eca4ca6b1404f71bc285644b8739576faaac917f5d285a8ed1894e21` |

V2-1 is closed: both PROCESS copies now use a saved snapshot with content
hashes before decisive checks, removing the premature commit option. The only
other change since v2 is the assignment's frozen-directory reference. Check
evidence and checked executable inputs are unchanged. No unresolved findings.

Final verdict: `ACCEPTED` for the v3 assignment, four policy documents and
saved check evidence within this documentation-only scope. Results are LEAD's
reported executions: 11 unittest tests passed, Ruff lint passed, and Ruff
format check reported two files already formatted, all exit 0. REVIEWER did
not execute project code or rerun these checks.

Next owner/action: LEAD may commit these exact accepted documents with this
review under the standing local-commit authorization. Preserve the checked
inputs and evidence; rerun affected checks and obtain review of affected policy
changes if further substantive edits occur. No push is authorized.
