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
- Every staged, unstaged and nonignored untracked change belongs to the supplied
  exact paths. Only additions and modifications of regular files are permitted;
  reject deletions, conflicts, type changes and renames. Detect renames as
  addition/deletion pairs so a source deletion cannot be hidden.
- At least one permitted change. Ignored files remain untouched; an explicitly
  supplied ignored untracked report is rejected rather than force-added.

Reject Git environment overrides that redirect the repository, worktree, index
or object storage instead of operating on an unintended repository state.
Use literal path handling and NUL-delimited Git output where filenames occur.

## Commit and result

Stage exactly the changed report paths, including their complete working-tree
contents. Revalidate HEAD, branch, operation state and permitted change scope
before committing. Capture the expected index tree, then run normal `git commit`
with the supplied message, preserving hooks and signing configuration.

Success requires exactly one new commit with the recorded HEAD as its sole
parent, on the original branch, with the captured tree, and a clean index and
worktree (nonignored untracked files included). Check operation state again.
Report the resulting full commit ID. A hook changing committed content or leaving
additional changes must not be reported as success.

On refusal or any command/postcondition failure, exit nonzero with actionable
diagnostics. Leave the state for inspection: never reset, abort, discard changes,
retry a commit, bypass hooks, push or switch branches. A failure after staging
may leave the index changed; a commit or hook failure may already have created a
commit. Report the observed HEAD when possible and explain this uncertainty.

## Scope and verification

This task adds the helper, focused integration tests using temporary repositories,
and a README usage link. It does not install the helper into generated projects,
change role instructions, or make its use mandatory yet.

Tests cover success with new/modified/staged reports and literal filenames;
incorrect HEAD, paths, repository state, messages, operations, ignored reports,
foreign changes and unsafe file types; hook refusal and hook changes to the
commit/worktree; preservation on failure. Use configured README tests, lint and
format checks. Do not claim protection from concurrent writers outside the
exclusive ownership assumption.
