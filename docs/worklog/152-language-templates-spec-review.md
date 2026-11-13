# Language starter specification review

## Identity and scope

- Reviewed source and frozen HEAD: `032d6174b504bef1463e4abc1abf826417225c56`.
- Specification: `docs/worklog/151-language-templates-task.md` and
  `docs/specs/newproject.md` at that commit.
- Also reviewed: `README.md`, `template/base/README.md`, and both
  `examples/{go,python}/docs/LANGUAGE.md` guides.
- Required baseline: `de0423e34d7073e25fbbeafa40f05839d73c6665`, with source
  paths named in task 151, including generator, layer sources, configured
  checks/coverage, existing tests and current workflow requirements.
- Sole report: `docs/worklog/152-language-templates-spec-review.md`.
- Worktree: `/private/tmp/newproject-language-templates`, initially clean.
- Independent static review; no project code or executable checks run.

## Assessment

The specification defines optional Go/Python selection independently of heavy,
standard argparse behavior, selected-source validation, additive collision
preflight and byte/mode preservation. Neutral creation neither requires the
examples tree nor adds a Makefile or language configuration. LEAD relayed
HUMAN's explicit confirmation of that neutral behavior during review; it
matches the written contract. The common README describes an optional guide
without adding a broken Markdown link in neutral output.

Existing target, Git, exclusive-copy and helper-reservation safeguards remain
binding. Language sources cannot replace AGENTS or helper paths. Canonical Go
files remain in examples/go; the Python starter adapts the repository conventions
without inventing an application layout or installing dependencies. The guides
identify editable defaults, tool environments and optional coverage artifacts.
Generation itself performs no language tool execution.

The verification plan covers language/heavy combinations, CLI errors and help,
unselected-source independence, source validation and collisions, payload
identity, neutral preservation and output Git state. It retains baseline
safety tests, requires a real Python-starter fixture and requires the configured
coverage run with source identity and accessible coverage.json. Implementation
review must inspect missing statements alongside changed code and tests.

Read `/tmp/newproject-language-spec-check.log`: nine files passed formatting,
lint passed, and 70 tests passed with saved exit status 0. These are DEVELOPER's
saved checks covering the specification checkpoint, not reviewer executions.
No implementation acceptance or new coverage claim is made at this stage.

## Finding and condition C1

Location: the final sentence of README.md's "Optional Python coverage report"
section. It says generated projects do not include the coverage target or
dependency, contradicting the newly specified Python starter.

Required literal correction, authorized on the reviewed base:

Replace:

> The generated projects do not include this reporting target or dependency.

with:

> Neutral projects do not include a coverage target; the Python starter includes an adaptable coverage target and documents its optional dependency.

Whitespace wrapping may change only around this replacement. No other source
or specification change is covered by this condition.

Saved evidence location: `README.md`, final paragraph of "Optional Python
coverage report", in LEAD's corrected checkpoint. Expected marker: the exact
replacement text above after joining wrapped lines with single spaces. The
old sentence must be absent. Closure must record the reviewed base, this report,
the corrected commit and its README-only source diff. The report commit itself
is expected between the reviewed base and correction.

LEAD may make the literal correction and retain the same configured check
results because executable check inputs are unchanged. DISPATCHER may close C1
without another review only when the named text comparison and permitted-diff
comparison match exactly. Any other source change or mismatch returns to REVIEWER.

## Verdict and next action

Verdict: `ACCEPTED_SUBJECT_TO_CHECKS`, pending C1 only. No other blocking
finding or binding ambiguity remains.
Next owner: LEAD applies and checkpoints the literal correction, supplies the
corrected commit and closure evidence to DISPATCHER, then releases implementation
only after C1 is closed. This condition does not claim the corrected version
was separately reviewed. No push or main merge is authorized.
