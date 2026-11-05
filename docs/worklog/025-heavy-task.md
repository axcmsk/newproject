# Heavy project variant

## Authority, baseline and routing

HUMAN requests a heavy variant as an addition to normal, feature branches for
heavy projects, the DiBBS journal writer, and a --heavy creation flag, preferring to avoid
duplicated common files. HUMAN selected template/base plus template/heavy and
prefers small generation-time edits to runtime file-existence checks; reserve
such optional reads for common preferences. Working fragment name: AGENTS.add.md.
HUMAN sets heavy defaults: park at <=30% weekly remaining, hard stop at <=25%,
15 percentage points per stage. Retain the proposed three-round same-blocker stop.
No DiBBS-specific exceptions or live/historical state are transferred.

Baseline: 236ea1a1d0336c1d53c7f6a07ca6a705217e7757.
Work branch: codex/heavy-template. This repository still uses normal rules;
heavy policies are generated deliverables, not active limits for this task.

Sources: docs/specs/newproject.md, root AGENTS and docs/workflow at baseline;
DiBBS at 767ced76e8f08810c11cf499cbcbc80a11f5238b:
scripts/workflow/work_log.py, tests/tooling/test_work_log.py,
docs/workflow/work-log-format.md, LIMITS.md, TASK-CONTEXT.md and PROCESS.md.
The sibling checkout provides these source files; use the pinned Git contents,
not unrelated working changes. It is a read-only reference, not this task's rules.

LEAD authors this contract, current specification, README and workflow content.
REVIEWER gpt-6-astra/high statically reviews the specification directly with LEAD,
then implementation/results through DISPATCHER. DEVELOPER gpt-6.1-terra/medium
runs checks, implements code/tests and ports the journal writer. DISPATCHER
 gpt-6-luna/low routes the exact accepted contract without interpreting it.
One repository writer at a time. Initial developer checks precede the spec
checkpoint/review; no implementation before spec acceptance and LEAD release.
Only local commits; stop after independent acceptance, no push/deploy/merge.

## Generator contract

Retain the existing creation contract except the explicit changes here:
- Common template files move unchanged to template/base/ (including hidden
  files). Heavy-only payload lives in template/heavy/. No symlinks; the chosen
  layout shares common policy files and each generated project is standalone.
- CLI accepts [--heavy] NAME and NAME --heavy. Accept -- to end option parsing,
  e.g. -- --heavy creates a normal project literally named --heavy and
  --heavy -- --heavy creates a heavy one. Other dash-prefixed names remain
  ordinary names for backward compatibility. A bare --heavy now requires NAME.
  Duplicate --heavy, missing NAME or multiple names refuse before mutation.
- Normal copies only base; it does not validate or depend on heavy. Heavy
  preflights both trees before mutation, combines shared directories and rejects
  every file/file and file/directory collision. Reject links/special entries,
  .git entries and traversal errors as before, including unsafe template root
  and selected source roots. Missing/empty base or selected heavy refuses.
- Required template/heavy/AGENTS.add.md is generation metadata, not output.
  Read it and base/AGENTS.md as UTF-8 during preflight; both must be nonempty
  regular files. Heavy output AGENTS.md is base text, trailing newlines removed,
  two newline characters, then fragment text with trailing newlines removed and
  one final newline. No other templating, substitution or content rewriting.
  Never emit AGENTS.add.md. Reject a base output with that reserved root name
  for heavy generation to avoid accidentally shipping the fragment name.
- All other bytes and modes are copied unchanged; the generated AGENTS keeps
  the base file's mode. No base/heavy directories appear in the output.
- No runtime existence tests select a workflow. Normal AGENTS stays normal;
  generated heavy AGENTS explicitly requires HEAVY.md and LIMITS.md, which
  select role-specific additions without duplicating the base role guides.
- Retain preflight/no-overwrite/partial-failure/Git isolation safeguards, main
  unborn with no initial commit/remotes, and standard-library Python 3.9+.
  Creation never activates feature branches itself: heavy policy starts the
  first task branch after an initial checked bootstrap commit on main.

## Heavy workflow content (LEAD-owned)

Provide HEAVY.md, LIMITS.md, STATE.md, TASK-CONTEXT.md, work-log-format.md and an
empty work-log.jsonl under docs/workflow, plus the AGENTS.add.md fragment.
HEAVY extends only the named normal rules and owns heavy role additions:
- Mandatory codex/ task branches, checked checkpoints, --no-ff merge only after
  review/required checks and merge authorization; preserve reviewed commits,
  never squash/rebase/amend them. No automatic push or publication.
- STATE is the sole live checkpoint, with operational block owned by DISPATCHER
  and substantive context by LEAD. Update material transitions, not every poll;
  reconcile actual Git/session state on resumption, preserve recovery references.
- Routing card pins source/contract, stage, ready/blocked dependencies, owners,
  allowed resources, expected outcome, stop, limits revision and sample references.
  Reviews use the base exact-condition rules, no second acceptance system.
- Append-only journal, provenance and timestamp discipline, supplied measurements
  only, no task-cost inference, no polling log or background monitoring.
- LIMITS has user-selected values above, independent weekly/stage stops,
  unknown-allowance pause, safe preservation, no fresh baseline on retries,
  comparable-window accounting, scoped HUMAN extensions only, three-round stop.
- More detailed execution evidence and bounded runtime ownership/cleanup:
  source/command/versions/status/stdout/stderr/meaningful assertions/session,
  preserve failure ambiguity; exact resource identity, ownership, consumers,
  terminality, storage headroom and reviewed cleanup scope. No inherited DiBBS
  fixture permissions, production-data authority or migration exceptions.
- DISPATCHER can execute only journal append/schema/help as a narrow exception
  to base developer-only execution; no arbitrary validation/tests or code edits.
  No new model targets; inherit normal role settings.
- New project state starts idle, with no fabricated authority, budgets, usage,
  sessions, findings or historical records. Numeric policy is distinct from an
  unknown observed allowance. Limits are read before substantive work, but
  safe initialization and requesting missing measurements remain possible.

## Journal tool (DEVELOPER-owned)

Port the pinned DiBBS writer to template/heavy/scripts/workflow/work_log.py,
retaining schema v2, v1/v2 history admission, commands and validation semantics.
Remove DiBBS branding, format/refactor only as needed for configured lint.
Retain exclusive local flock, duplicate-ID checks, append-only correction,
UTC/provenance, refusal of malformed/truncated history and uncertain-write
reporting. Do not turn it into a framework or add usage polling. Journal append
requires POSIX flock; unsupported platforms fail clearly, schema/help remain
available. Document this limitation. No host dependencies or real journals.
Adapt existing focused tests to a synthetic historical fixture rather than the
real DiBBS log; keep concurrency and duplicate-race tests. Cover unsupported
locking and generated-project default log location outside its working directory.

## Checks and acceptance

DEVELOPER owns all executable checks. Required commands after implementation:
python3 -m unittest discover -s tests -v
.venv/bin/python -m ruff check newproject.py tests template/heavy/scripts
.venv/bin/python -m ruff format --check newproject.py tests template/heavy/scripts

Retain all current creation tests adapted to base layout. Add actual CLI/real
Git temporary-fixture coverage of normal/heavy, both flag positions, terminator,
literal dash names, duplicate/missing arguments; payload union and exact composed
AGENTS, fragment exclusion, mode preservation; missing/invalid/unreadable selected
layers, collisions (both ancestor directions) and no target mutation on refusal;
normal independent of invalid/missing heavy. Use real templates in an integration
creation test for both variants; exercise the installed journal from another cwd
and verify its default journal path. No real sibling projects, Docker or services.
Keep failure injection coverage for copy/traversal/Git failures; capture precise
failure reasons and final state, not just nonzero status.

Review all generated local Markdown links and the heavy onboarding chain,
base/heavy separation and limits boundary wording. README describes usage,
layout, feature-branch bootstrap, journal commands, platform limits, and expanded
check commands. Root project rules describe the two source layers without
activating heavy policy here. Historical task reports remain unchanged.

Reserve reports: 026 developer checks/implementation; 027 spec review;
028 implementation review. Further rounds get new numbered reports.
Allowed developer writes: newproject.py, tests/, ruff.toml if narrowly necessary,
heavy/scripts/workflow/work_log.py under template, 026 report, and mechanical
move of old template common files into base after spec acceptance. LEAD alone
writes requirements/user docs; transfer writer ownership before each role writes.

## Specification correction R1

Heavy explicitly extends the base review-time report-only allowlist: LEAD may
preauthorize DISPATCHER writes to the STATE operational block and journal outside
pinned inputs. HEAD/inputs stay fixed and no commits occur during review. Keep
single-writer transfers; defer substantive STATE edits. At closeout verify all
allowed paths/block boundaries; operational changes are outside source acceptance.
Buffer facts for frozen or unlisted operational paths and report urgent blockers.
No check input changed by this documentation correction; initial results remain
applicable. Revised specification review is reserved as 029-heavy-spec-review.md.

## Final HUMAN clarification

Avoiding duplication is a maintainability preference, not a permanent prohibition.
A normal/AGENTS.add.md fragment or simple conditional templates are possible
future options, not required deliverables. The current base plus heavy fragment
composition remains sufficient. This clarification does not change collision
refusal, validation or any other generator behavior, and adds no runtime scope.
The script and current payload have independently passed implementation review
at 3b88345; review this wording delta separately in 030-heavy-clarification-review.md.
