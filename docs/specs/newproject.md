# Project creation

## Approved user intent

Provide `python3 newproject.py [--heavy] NAME` to create a sibling of this
repository from template/base, optionally composed with template/heavy, and
initialize Git on main without a commit.
The user approved the boundaries below and specifically requested extensive tests.

## Contract

- Resolve the repository from the script location, independently of working directory.
  NAME is one directory name, never an absolute or nested path. Reject empty names,
  `.`/`..`, either path separator and control characters. Names with spaces and
  Unicode are supported; shell metacharacters must never be evaluated.
- Accept a nonexistent target, an existing empty directory, or a directory containing
  only its own real `.git` directory for an empty non-bare repository. Reject files,
  target symlinks (including broken links), `.git` symlinks/files, malformed repositories,
  repositories with commits/refs or staged entries, and any other target contents.
  A repository discovered in a parent is not the target's repository.
- On success the target contains the template tree, `tools/merge.py` and its own Git repository,
  on an unborn `main` branch, without staged entries, commits or remotes added by
  this program. Preserve pre-existing Git configuration. Changing the unborn branch
  name to main is intended. Never delete existing user files or Git history.
- Validate arguments, source tree, target state and Git availability before target
  mutation. Each selected source layer must be a nonempty real directory containing only
  regular files/directories; reject symlinks, special entries and any `.git` entry.
  The containing template directory must also be real.
  Copy hidden template files too. Apart from the merge helper specified below,
  do not copy repository history, worklogs, generator,
  caches or personal sibling `common` files unless actually part of the template.
- Use standard-library Python only, with a documented minimum version. Invoke Git
  without a shell and isolate Git operations from inherited GIT_* overrides that
  could redirect repository/index/config operations. Do not change global Git config.
- Repeated invocation after success fails clearly without changing existing content.
  Return zero on successful creation or requested help, nonzero on refusal/failure, with useful diagnostics
  including target path and any partial state left after mutation for creation errors.
  Argument syntax errors use the standard parser diagnostics described below. No automatic
  recursive rollback or deletion of pre-existing directories. Failures before
  mutation leave the target unchanged. Concurrent hostile filesystem replacement
  is outside scope, but do not overwrite files that appear during copying.
- No initial commit, push, publication, dependency install or interactive prompt.

## Variant composition

The common source is `template/base/`; `template/heavy/` contains only additions.
Normal creation uses base and does not inspect or require heavy. Heavy
creation preflights both layers, merging shared directories but refusing any
file/file or file/directory conflict before target mutation. Output has no layer
wrapper directories. All regular payload bytes/modes are preserved.

Use standard-library `argparse` with one required positional NAME, a boolean
`--heavy` flag and its standard `-h`/`--help`. The flag may precede or follow
NAME. Retain normal argparse option/terminator behavior, including repeated
boolean flags; do not implement special compatibility for dash-prefixed names
or add a separate ban on such names. `--` remains available as the standard
terminator. Missing/extra arguments and unknown options use argparse's normal
usage/error output and exit status 2, before template/Git/target operations.
Help prints usage and exits 0 without requiring templates or Git and without
creating a target. Domain validation of NAME and all creation safeguards remain
unchanged; creation/domain failures retain the existing diagnostics and status.

Heavy requires `template/heavy/AGENTS.add.md` and base/AGENTS.md as nonempty
UTF-8 regular files. During preflight, prepare output AGENTS.md as base text
with trailing newlines removed, two newlines, fragment text with trailing
newlines removed and one final newline; retain base mode. The fragment is not
copied to output. A base root entry named AGENTS.add.md is reserved and refused
for heavy generation. Every other collision is an error; no general overwrite
or templating mechanism is provided. A malformed fragment refuses before mutation.

Generated heavy AGENTS explicitly selects HEAVY.md and LIMITS.md. No runtime
file-existence check selects a mode. Both variants start on unborn main; heavy
task branches are a subsequent workflow obligation, not a generator side effect.
Heavy payload includes workflow/checkpoint/limit/journal documents, an empty
journal and the standalone journal writer. It contains no DiBBS history, active
state, fixture permissions or exception grants. The writer requires POSIX flock
for append, but its schema/help and the generator remain platform-independent
within their documented Python/Git requirements.

## Shared merge helper

Both variants install repository-root `tools/merge.py` at the same relative path
in the generated project. This is the sole helper source; do not duplicate it
in template layers or copy other repository tools. Preserve its bytes and mode.
Resolve it relative to the generator, independently of cwd. During preflight,
require a real tools directory and a readable regular merge.py, rejecting missing,
symlink or special sources before target mutation. Help and argument errors do
not require this source.

Selected layers may contribute a tools directory and other files beneath it,
but must not supply tools/merge.py (file or directory) or a non-directory tools
entry. Refuse these collisions before target mutation. Use exclusive file
creation as for template payloads; report partial state on later copy failures.

Both variants receive the common MERGE, MAIN-MESSAGE and BRANCH-MESSAGE guides
from base, with links from PROJECT-RULES, PROCESS and LEAD. Normal keeps optional
task branches; heavy requires them and delegates merging to the common procedure.
The helper may squash into main while preserving the source branch and reviewed
commits. No new HUMAN merge-approval gate or duplicated mode-selection rules.
Generation itself never runs the merge helper or creates commits/task branches.

## Required verification

Use isolated temporary directories and controlled Git configuration for tests;
never create real sibling projects during checks. Exercise the actual CLI and real
Git for success and repository-state checks, and focused injection for failures.
Cover new and empty targets; initialized empty repo (including non-main branch);
working-directory independence; exact copied content; main/unborn/unstaged state;
invalid names, Unicode/spaces/metacharacters; nonempty target and repeated run;
file/symlink/broken-link targets; inherited parent repo; existing commits, staged
entries, refs, bare/malformed Git, `.git` file/link; absent/invalid template;
missing Git and Git-init/copy failures; preservation of existing content/config;
Git environment isolation; no partial writes on preflight refusals and useful
partial-state diagnostics. Assertions must check state and intended failure
reason, not merely exit status. Run the complete suite and record commands,
Python/Git versions, tested source identity, results and limitations.

Also cover both CLI flag positions, standard help and argument errors without
mutation, -- termination without custom dash-name handling, repeated boolean
flags, argument refusal, missing/invalid selected layers and normal independence from
heavy, shared directory union, file/file and ancestor collisions, exact AGENTS
composition and fragment exclusion, mode preservation, real-template normal and
heavy generation, and installed journal default-path behavior from another cwd.
Journal tests use synthetic history and temporary logs, including validation,
corrections, malformed history preservation, unsupported locking, concurrent
appends and duplicate-ID races. Never read or modify a real work journal.

Verify installed helper bytes/mode and shared guides in both generated variants.
Exercise an actual merge with each installed helper in isolated generated repos,
checking the result, message and preserved source. Cover missing/invalid/unreadable
helper sources, selected-layer path collisions, allowed shared tools directories,
normal independence from heavy, help without helper, and copy-time refusal without
overwrite. Preserve all existing tests and README checks.
