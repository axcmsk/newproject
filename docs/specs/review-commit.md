# Review report commit helper

`tools/review_commit.py` is a Python 3.9+ standard-library CLI requiring Git.
It saves reports after a review; it does not assess or grant acceptance.

## Invocation

From the repository root:

```sh
python3 tools/review_commit.py --head FULL_HASH -m "review: description" docs/worklog/NNN-review.md
```

`--head` is the full object ID recorded at review start, not a symbolic ref or
abbreviation. One or more positional arguments are exact repository-relative
report paths. The caller holds exclusive writer ownership for the entire call;
the helper does not implement locking against other writers. Required project
checks must already cover the reviewed inputs. The helper does not run them.

### Explicit operational paths

The optional repeatable `--allow-dirty PATH` permits an exact operational file to
remain unstaged while committing reports. Without it, retain existing behavior.
For example:

```sh
python3 tools/review_commit.py --head FULL_HASH -m "review: description" \
  --allow-dirty docs/workflow/STATE.md \
  --allow-dirty docs/workflow/work-log.jsonl \
  docs/worklog/NNN-review.md
```

The paths above illustrate the interface; callers must use the actual paths
explicitly authorized in the assignment. This option does not itself grant write
permission. Operational files must lie outside the pinned review inputs. The
caller checks ownership, the authorized STATE block and journal rules; the
helper does not interpret document contents or validate append-only history.

Each operational path must be a canonical repository-relative exact filename,
with no directory, glob expansion, `.`/`..` component, `.git` component or symlink
in the file or parent components. Treat characters literally, as for reports.
Require an existing regular tracked file with a regular-file entry in HEAD and
the index. No required path prefix or filename suffix applies. Deduplicate repeated
arguments. Report and operational path sets must be disjoint.

Operational index entries must equal HEAD: reject any staged content or mode
change, addition, deletion, conflict, type change or rename. Worktree state may
be clean or an unstaged modification of the regular file, including a mode
change; reject deletions, symlinks and special file types. Untracked operational
files are outside this extension. Tracked files remain eligible even if ignore
rules match their names. Preserve the existing global refusal for index flags
that hide worktree changes, including assume-unchanged and skip-worktree.

## Preconditions

Before staging anything, require:

- An existing non-bare repository, invocation at its root, and a local attached
  branch with HEAD equal to the supplied full hash.
- No merge, rebase, cherry-pick, revert, sequencer or bisect operation in progress.
- A nonempty single-line message beginning with `review: ` and a nonblank subject.
- Canonical relative paths below `docs/worklog/`, with `.md` suffix, no `..`,
  absolute paths, pathspec expressions, symlinks (including parent components),
  or directories. Each argument identifies an existing regular file. Duplicate
  arguments may be deduplicated.
- Every staged change belongs to the supplied report paths; unstaged changes
  may additionally belong to the explicitly allowed operational paths above.
  Nonignored untracked changes must be reports. Only additions and modifications
  of regular report files are permitted; reject deletions, conflicts, type changes
  and renames. Detect renames as
  addition/deletion pairs so a source deletion cannot be hidden.
- At least one report change, regardless of operational changes. Ignored files
  remain untouched; an explicitly supplied ignored untracked report is rejected
  rather than force-added.

Reject Git environment overrides that redirect the repository, worktree, index
or object storage instead of operating on an unintended repository state.
Use literal path handling and NUL-delimited Git output where filenames occur.

## Commit and result

Stage exactly the changed report paths, including their complete working-tree
contents. Revalidate HEAD, branch, operation state and permitted change scope
before committing. Capture the expected index tree, then run normal `git commit`
with the supplied message, preserving hooks and signing configuration.

Before staging, snapshot every allowed operational file's exact bytes and
permission bits, and its index entry (mode, object ID and stage). Recheck these
snapshots before commit and after commit, including for initially clean listed
files. Never stage or otherwise change operational paths. A change to these
snapshots, including by a hook or clean filter, is a failure, not permission to
refresh the snapshot. Existing exclusive ownership remains required; this is
not protection against concurrent writers or hostile hooks.

Success requires exactly one new commit with the recorded HEAD as its sole
parent, on the original branch, with the captured tree and a clean index.
Reports must be clean; only the original allowed operational changes may remain
in the worktree, with unchanged snapshots. No other tracked or nonignored
untracked changes may remain. Check operation state again.
Report the resulting full commit ID. A hook changing committed content or leaving
additional changes must not be reported as success.

On refusal or any command/postcondition failure, exit nonzero with actionable
diagnostics. Leave the state for inspection: never reset, abort, discard changes,
retry a commit, bypass hooks, push or switch branches. A failure after staging
may leave the index changed; a commit or hook failure may already have created a
commit. Report the observed HEAD when possible and explain this uncertainty.

## Scope and verification

The helper is used by the [report commit procedure](../workflow/REVIEW-COMMIT.md).
The generator installs its single source into both project variants; see
[Project creation](newproject.md). Integration does not change helper behavior.

Tests cover success with new/modified/staged reports and literal filenames;
incorrect HEAD, paths, repository state, messages, operations, ignored reports,
foreign changes and unsafe file types; hook refusal and hook changes to the
commit/worktree; preservation on failure. Use configured README tests, lint and
format checks. Do not claim protection from concurrent writers outside the
exclusive ownership assumption.

For the extension, add focused integration coverage for multiple operational
paths, duplicate/literal paths, clean listed files, unstaged content/mode changes,
and tracked files matching ignore rules. Verify report-only commit topology/diff,
unchanged operational bytes/modes/index entries and unchanged dirty status.
Cover overlap, invalid or untracked paths, staged/partly staged operational
changes, deletions, renames, conflicts, unsafe types/parents, hidden index flags,
unlisted dirt and operational-only changes; refusal before staging must preserve
HEAD, the index and all files. Hook/filter changes to operational content, mode or
staging must fail without automatic repair, even when a commit already exists.
Retain existing strict-mode, hook and generator tests. Exercise the installed
extension in both generated variants when implementing it.

Implementation must update root/base REVIEW-COMMIT and heavy instructions in the
same branch. Replace heavy's direct-commit exception with explicitly assigned
operational paths passed to the helper, preserving block/journal checks, pinned
inputs, writer handoff and separate operational closeout. No broad ignore option,
automatic path discovery, semantic journal parser, locking service, stash or
temporary index is part of this extension.
