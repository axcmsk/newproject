# Language starter implementation review

## Identity and scope

- Reviewed implementation and frozen HEAD:
  `97bbddb8d095d889d5177be198f6004f858c09f1`.
- Specification: `docs/worklog/151-language-templates-task.md` and
  `docs/specs/newproject.md` at `032d6174b504bef1463e4abc1abf826417225c56`.
- Specification report: `docs/worklog/152-language-templates-spec-review.md`,
  commit `4f64160f36cfeaf70f22b4f5be7f4e723c4db058`.
- C1 corrected source: `683d122000b9023065d591a685245851cbff0ef1`.
  Its README-only diff matches the permitted literal correction and wrapping;
  DISPATCHER closed the condition before implementation.
- Implementation scope: `newproject.py`, `tests/test_newproject.py`,
  `examples/go/.gitignore`, `examples/python/{Makefile,ruff.toml,.coveragerc,.gitignore}`,
  and `docs/worklog/153-language-templates-results.md`.
- Sole report: `docs/worklog/154-language-templates-review.md`.
- Worktree: `/private/tmp/newproject-language-templates`, initially clean.
- Independent static review of source, tests, diffs and saved evidence; no
  project code, checks or coverage were executed by REVIEWER.

## Implementation and test assessment

Argparse selects only go/python, retains last-value semantics, and runs before
source/Git/target operations. Without a language, the new examples path is not
inspected. The selected payload uses the existing scanner and is composed after
base/heavy with directory union and file collision refusal. Heavy's consumed
AGENTS fragment remains reserved. Existing helper-path validation runs on the
combined entries before target mutation; copy exclusivity and Git safeguards
remain unchanged. The language change does not execute tools, create application
metadata, or install dependencies.

Python starter targets use adaptable paths and the documented unittest/Ruff
conventions. Coverage remains separate from check, uses fresh erase/run/combine
and text/HTML/JSON reports, and carries absolute data/config paths for subprocess
collection. Its config measures the project rather than root-repository aliases
and omits tests/.venv. Ignore rules cover generated artifacts and caches. Ruff
rules retain the baseline selection and adapt repository-specific prose.
Go recipes and root check/coverage configuration are unchanged.

Five added test methods exercise both languages with/without heavy, shared
directory merging, hidden bytes/modes and unborn/unstaged main, option order and
repetition, help/errors without sources or Git, neutral independence, malformed
selected sources and irrelevant unselected sources. Collision cases include
base, heavy, AGENTS, helper ancestors and both helper paths. Real language
payloads are compared byte-for-byte and mode-for-mode with canonical sources.
Existing neutral, target-safety, helper and real-template tests remain present.

## Saved checks and coverage inspection

Read `/tmp/newproject-language-implementation-check.log`: formatting and lint
passed, and all 75 tests passed with saved exit status 0. Read
`/tmp/newproject-language-coverage.log`: the configured coverage sequence passed
with saved exit status 0 and produced the documented text/JSON/HTML reports.

Read `/private/tmp/newproject-language-templates/coverage.json` for the measured
checkpoint inputs identified in report 153. It reports 179/186 statements in
newproject.py and 616/649 overall, with no branch measurement. Inspected the
generator's missing lines 47, 91, 163-164, 194, 199 and 203 alongside source:
they are unchanged template/AGENTS/Git error guards, not new language logic.
The new language-selection/composition statements are measured as executed;
the assertions above supply behavioral evidence beyond that coverage fact.
The remaining missing statements are in unchanged helpers/journal code. No
coverage percentage is used as an acceptance threshold.

Read the real Python-starter logs under `/tmp/newproject-language-smoke/`:
dirty format returned 2 and its saved comparison returned 0; reformat changed
the fixture; check passed formatting/lint and its test; coverage emitted JSON
and HTML. The fixture JSON reports only example.py, consistent with test
omission, and no repository-specific paths were required. Exact commands and
artifact paths are retained in report 153. These are DEVELOPER's executions,
not reviewer reruns.

## Limitations, findings and verdict

Executed environment: Python 3.9.6, Git 2.54.0, Coverage.py 7.10.7, GNU Make
3.81 on macOS arm64. Other platforms were not exercised. Existing Go recipes
were not downloaded/run again; their unchanged behavior and canonical payload
identity are supported by baseline evidence and retained tests. Coverage is
statement coverage and does not establish exhaustive branch behavior.

No blocking findings.

Verdict: `ACCEPTED` for the implementation and evidence at
`97bbddb8d095d889d5177be198f6004f858c09f1`.
Next owner: DISPATCHER returns acceptance and this report commit to LEAD for
closeout. No push or main merge is authorized by acceptance.
