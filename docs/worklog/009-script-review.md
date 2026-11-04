# Script implementation review

## Round 1: identity and scope

Role: independent REVIEWER, task `/root/script_dispatch/reviewer`.
Baseline: `ae40b4c2641e0c8ed4ed9b55872f81ab19166303`.
Specification and assignment are the unchanged accepted inputs in
`/private/tmp/newproject-script-spec-v1/newproject.md` and
`/private/tmp/newproject-script-spec-v1/006-script-task.md`, identified by
specification review `007-script-spec-review.md` as Git blobs
`6cdbbb0dd383efc2d0f300e55d2d2469e053ec0d` and
`e31c286f861b5ca7a7bc4d542fc3f1bdba684576`, respectively.

Reviewed files were read from `/private/tmp/newproject-implementation-v1`.
The source identities supplied by DISPATCHER and the saved developer evidence
are these SHA-256 values:

| Path | SHA-256 |
| --- | --- |
| `newproject.py` | `62fa656357ceb870fff3bc7a7a9cfe2f2c5f53718ff7ffc5f18592c5b29849ab` |
| `.gitignore` | `6feaded4e28ea86e001a6751b4e3d960e8b7c31b9616ff9936b79297086e809b` |
| `tests/test_newproject.py` | `33792f50246e8b4d6cc263158d4e77edc5a78c48fd39a397f4019af23031521f` |
| `README.md` | `e8f13fd9994dfdbc87478c371cfeae138ecff266c9bf0a980802557222b6faab` |
| `docs/workflow/PROJECT-RULES.md` | `d1589a994e33cf1d54fb9e2a91d1b54ded2700eaeba54bdc18c56dd580dcbd19` |

Static review covered implementation against the contract, test assertions and
coverage, saved evidence in `008-script-implementation.md`, and LEAD's README
and project-configuration changes. No project code, tests, validators or other
executable project checks were run. Hash identities and execution results are
the supplied evidence, not independently reproduced results. Repository status
was inspected before writing this review; no reviewed artifact was edited.

## Findings

### R1 — Incomplete template traversal can report success

Location: `newproject.py:43-48`, `90-99`; tests at `129-142`.

`os.walk` has no error handler. An unreadable child directory can be recorded
as a valid directory while its enumeration error is silently ignored. The copy
then creates that directory without its contents and reports success. Invalid
entries hidden beneath the unreadable directory are not validated either.
This violates complete source validation before mutation and exact template
copying. Python documents that traversal errors are ignored by default:
[os.walk documentation](https://docs.python.org/3/library/os.html#os.walk).

Closure: DEVELOPER must make traversal errors abort preflight, and save a focused
regression demonstrating a child enumeration failure after some entries have
already been discovered. Assert a useful error identifying the failed traversal,
nonzero result, and absence of new target state (or byte-for-byte preservation
of a pre-existing accepted target). A controlled failure injection is suitable;
the test must not depend on whether the runner can bypass directory permissions.

### R2 — Ambient Git templates can violate successful repository state

Location: `newproject.py:19`, `88-99`; tests at `144-154`.

Removing `GIT_*` variables does not neutralize `init.templateDir` from Git
configuration. `git init` can copy a configured template's index, refs, objects
or remote configuration into the new repository. The script neither controls
this initialization input nor verifies its resulting state before reporting
success. It can therefore return zero with staged entries or imported history
and configuration contrary to the contract. This is an inference from this
call site and Git's documented template copying behavior:
[git-init template directory](https://git-scm.com/docs/git-init#_template_directory).

Closure: DEVELOPER must ensure new/empty targets initialize into the required
own, unborn `main`, unstaged repository without introducing history or remotes
through ambient templates. Save a real-CLI/real-Git regression with an isolated
Git config selecting a populated Git template, and assert the actual resulting
branch, refs/HEAD, index and remotes. Preserve existing accepted repositories'
configuration. The implementation technique remains DEVELOPER's choice.

### R3 — README gives an unsupported command form

Location: `README.md:46-48`; `newproject.py:17`, `33-35`;
`tests/test_newproject.py:75-77`.

The README tells users to insert `--` before dash-leading names, but the script
requires exactly one argument and treats it literally. The documented invocation
`python3 newproject.py -- -dash` is refused, while the tested and implemented
form `python3 newproject.py -dash` succeeds.

Closure: LEAD should correct the README to describe the existing one-name CLI
and give the actual dash-leading-name form. No parser extension is needed by
the approved specification. Return the corrected frozen documentation for review
with the implementation fixes.

### R4 — The test environment is not fully controlled

Location: `tests/test_newproject.py:25-28`, `39-41`;
`newproject.py:19`; README `70-71`.

Tests copy all inherited environment variables. Fixture-building Git commands
therefore retain inherited `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` and
configuration overrides. These can redirect setup commands, including `git add`
and `git commit`, outside the temporary fixture. Setting HOME does not remove
an inherited XDG configuration location. Moreover, the script strips the
test-provided `GIT_CONFIG_NOSYSTEM`, so that variable does not isolate the Git
commands launched by the CLI. The report's claim of isolated settings is not
established for either execution path.

Closure: DEVELOPER must isolate both fixture Git and CLI Git from uncontrolled
inherited repository/configuration settings, while retaining deliberate override
inputs in the environment-isolation case. Save a regression or equivalent
meaningful evidence with deliberately contaminated inherited settings, asserting
all fixture effects remain temporary and external sentinel repositories/config
files remain unchanged. Document how HOME, XDG and system configuration are
controlled for the real Git processes used in the decisive run.

### R5 — Refusal assertions do not establish unchanged contents

Location: `tests/test_newproject.py:43-47`, `60-62`, `122-127`.

The shared refusal helper only checks the program's own "Target unchanged"
claim. The invalid-Git cases compare path names, which would still pass if HEAD,
config, refs or index bytes were changed in place. The repeated invocation case
does not compare target state at all. These assertions do not meet the explicit
verification requirement for preservation and no partial writes on preflight
refusals.

Closure: DEVELOPER must add meaningful before/after target-state assertions for
existing Git refusals and repeated invocation, including file bytes and symlink
identity where applicable; assert nonexistent targets remain absent for relevant
preflight failures. Include preservation of the pre-existing config/index/history
data, not only directory entries or error text. Save the updated full-suite result.

## Evidence assessment and limitations

The supplied report states that all eight test methods passed under Python 3.9.6
and Git 2.54.0, with a 2.121-second run and `OK`; it also records the frozen source
and an earlier corrected fixture syntax error. The grouped tests meaningfully
cover many required success/refusal paths, Unicode and shell metacharacters,
parent repository discovery, retained custom configuration, missing Git,
initialization failure and destination collision. Exclusive file creation is a
useful protection against overwriting a file appearing during copy.

Those reported passes do not resolve the cases and weak assertions above.
Testing on one platform is an openly stated limitation, not itself a blocking
finding. Hostile concurrent filesystem replacement remains explicitly excluded.
The Git-template scenario and traversal-error scenario were assessed statically,
not reproduced by REVIEWER. No findings are raised against `.gitignore` or the
reviewed PROJECT-RULES documentation addition.

## Verdict and next owner

`CHANGES_REQUESTED` for implementation snapshot v1 and its associated README.
R1, R2, R4 and R5 return through DISPATCHER to DEVELOPER for ordinary fixes and
developer-owned executable checks. R3 returns to LEAD as documentation owner.
Preserve this snapshot and its evidence, freeze the revised implementation and
documentation, rerun the complete suite, and return the new identities and saved
results for independent review. No condition is delegated for automatic closure;
REVIEWER must assess the revised round before acceptance.

## Round 2: identity and scope

Role: the same independent REVIEWER. The baseline, accepted specification and
assignment are unchanged from Round 1, including their frozen paths and Git blob
identities recorded above. Round 1 and its failed verdict remain preserved.

Reviewed files were read from `/private/tmp/newproject-implementation-v2`.
The supplied SHA-256 identities recorded in `008-script-implementation.md`,
Round 2, are:

| Path | SHA-256 |
| --- | --- |
| `newproject.py` | `ae2decacfca8e005d24fc0f6004d083cfb66d1af2bec2f17cf3b0726d91f7c3c` |
| `.gitignore` | `6feaded4e28ea86e001a6751b4e3d960e8b7c31b9616ff9936b79297086e809b` |
| `tests/test_newproject.py` | `26390f08051900601884d837a2e8e5f9a203dae56a6e79c7c734f10cf788fac6` |
| `README.md` | `e3b190c23273c335c55994e19487c1e12c145e4b9cd1686c8187485b66fb21f2` |
| `docs/workflow/PROJECT-RULES.md` | `d1589a994e33cf1d54fb9e2a91d1b54ded2700eaeba54bdc18c56dd580dcbd19` |

This round covered all R1–R5 closure conditions, the complete revised script and
test file, the corrected README, unchanged project configuration and ignore
file, and the new saved execution evidence. The review remained static; no
project code or executable project checks were run and no implementation or
documentation artifact under review was edited.

### Resolution of prior findings

- **R1 closed.** `newproject.py:45-48` installs an error handler that raises a
  preflight refusal on traversal failure. The regression at
  `tests/test_newproject.py:174-192` yields initial source entries before injecting
  a child enumeration failure, then checks nonzero status, traversal-specific
  diagnostics identifying the child, and unchanged state of an existing empty
  target. The injection is independent of runner permissions.
- **R2 closed.** `newproject.py:94-95` supplies an explicitly empty temporary
  Git template, preventing ambient initialization templates from importing
  repository state. Existing accepted repositories use the separate branch
  update path, retaining their configuration. The real Git/CLI regression at
  `tests/test_newproject.py:194-208` configures an ambient template containing a
  staged index and a remote, then checks the common success assertions for
  unborn `main`, unstaged state and absent remotes, plus empty refs and absence
  of an imported index. The explicit empty source also excludes objects and
  refs, although the contamination fixture itself does not contain a commit.
- **R3 closed.** The corrected README requires exactly one name argument and
  states that dash-leading names are accepted directly. This agrees with the
  parser and the real CLI `-dash` case at `tests/test_newproject.py:93-95`.
  No unsupported `--` instruction remains.
- **R4 closed.** Fixture setup at `tests/test_newproject.py:25-29` removes
  inherited Git variables, replaces HOME and XDG_CONFIG_HOME with temporary
  locations and disables system Git configuration. Script-invoked Git likewise
  removes inherited Git variables and explicitly disables system configuration
  at `newproject.py:20-21`; the temporary HOME/XDG paths remain in effect for
  tests. Deliberate override cases are supplied separately. The regression at
  `tests/test_newproject.py:210-227` checks a contaminated CLI invocation against
  a sentinel repository and configuration file using byte-level state snapshots.
  The reported decisive full-suite command also contaminates the inherited
  environment, exercising fixture sanitization throughout the suite.
- **R5 closed.** The state helper at `tests/test_newproject.py:44-57` records
  file bytes, directory identities and symlink destinations. Repeated creation
  at lines 78-80 and all invalid Git fixtures at lines 140-145 compare complete
  before/after states, including config, HEAD, index and stored history where
  present. Missing-template/invalid-template and missing-Git tests retain checks
  that no target was created. These are meaningful state assertions beyond
  the error text and directory-name comparison from Round 1.

### Evidence, findings and limitations

The saved Round 2 evidence identifies the frozen source before decisive checks
and records the exact contaminated-environment command invoking
`python3 -m unittest discover -s tests -v`. DEVELOPER reports all 11 methods
passed in 2.606 seconds with `OK`, under Python 3.9.6 and Git 2.54.0. The evidence
also describes the environment isolation and retains the earlier round. Those
are reported execution results, not results independently reproduced here.

The revised tests retain the earlier meaningful success/refusal coverage and
add targeted regressions for the identified defects. No blocking findings remain
and no new findings are raised in this round. The corrected README and reviewed
PROJECT-RULES addition are consistent with the implemented CLI and workflow.

Coverage remains one reported Python/Git/platform combination. Traversal and
copy boundary failures are deterministic in-process injections; the relevant
success, Git-template and environment cases exercise the subprocess CLI and real
Git. Hostile concurrent filesystem replacement remains outside the accepted
specification. These limitations do not prevent acceptance of the named scope.

### Verdict and next owner

`ACCEPTED` for the exact v2 implementation, tests and documentation identified
above, against the unchanged accepted specification and assignment. R1–R5 are
closed by this independent review; no conditional checks remain outstanding.

Next owner: DISPATCHER. Report acceptance, both review rounds, exact v2 identities
and the developer's saved check evidence to LEAD for suitability assessment and
authorized local closeout. This verdict does not authorize a real sibling project,
push, publication or deployment.
