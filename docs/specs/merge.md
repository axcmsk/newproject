# Merge helper

The helper lives in `tools/merge.py` and is used by this repository's
[merge procedure](../workflow/MERGE.md). The project generator installs the same helper in both project variants.

## Interface and scope

`python3 tools/merge.py SOURCE -m MESSAGE`, run inside the repository to merge.
Use standard-library Python 3.9+ and argparse, with standard help. SOURCE is an
exact local branch name, not an arbitrary revision expression. TARGET is fixed
to main in one top-level constant, editable locally for repositories using master.
There is no target argument, option, configuration lookup or branch-name fallback.
TARGET must already be checked out; do not switch branches. Require committed tips,
distinct branches, and a nonempty, non-whitespace message. Pass the supplied text
to Git without adding titles, trailers, hashes or inferring a Conventional Commit
type. Use Git's verbatim cleanup (normal final newline representation is
permitted); repository hooks may subsequently change the message or contents. No fetch, push, branch deletion or history rewrite.

This helper checks mechanical conditions only. It never reads reviews, runs test
suites, assesses changes, queries allowances or interprets prose. The caller owns
permission, tests, review and the choice of source/target/message.

## Mode selection

Pin both branch tips before the operation. Consider all commits reachable from
SOURCE but not TARGET (`TARGET..SOURCE`), including merge commits. Inspect only
the first-line subject: a known prefix starts at column zero and is exactly one
of `step:`, `fixup:`, `docs:`, `review:`, `log:` (case-sensitive). Count `step:`
commits; do not infer relationships or require a step for supporting commits.

- All prefixes known and step count <= 1: squash into one new commit.
- Otherwise: a real merge commit with two parents, even if fast-forward is possible.

An empty range refuses. Never choose another mode after failure. No user override
or guessed prefix mapping is needed in this version.

## Preconditions and effects

Before modifying repository state:
- Require a working-tree Git repository, attached HEAD at TARGET, both local tips
  resolving to commits, distinct branches and a nonempty range.
- Require a clean index and tracked worktree and no nonignored untracked files,
  using explicit porcelain status options independent of user display settings.
  Include submodule dirtiness in that status; do not silently ignore it.
- Refuse unfinished merge, rebase, cherry-pick, revert or sequencer operations.
  Resolve state locations through Git so linked worktrees are handled correctly.
- Keep ignored files allowed, but prohibit overwriting them during merge using
  Git's --no-overwrite-ignore guard. Do not delete, stash or force-clean files.
- Recheck pinned tips/HEAD and cleanliness immediately before starting the merge.
  Concurrent external writers are outside scope; callers must hold sole ownership.

Use Git without a shell. Do not let inherited Git repository/index/config-routing
environment overrides redirect the operation outside the cwd repository. Preserve
normal repository configuration and hooks; do not bypass checks or hooks to make
a merge pass. Pass explicit no-autostash. Honor repository rerere settings,
including cached resolution reuse and its index-update policy; do not enable or
disable them. Do not change persistent Git configuration. Invoke a standard two-head merge,
not custom merge-tree/commit-tree plumbing or a temporary worktree framework.

Perform the chosen merge without automatic commit/fast-forward, then commit with
the supplied message only if merge succeeds. Leave conflict resolution to the
caller. On Git error, stop dependent operations and report the failing command,
Git diagnostic and whether state may be partial. No automatic retry, reset, abort
or cleanup. Keep source branch unchanged. A failed commit may leave staged merged
content; report that plainly. Do not force an empty squash commit when there is
no net change. Successful output states mode and resulting commit ID; failures
return nonzero, help returns zero. Verify target/HEAD, parent topology and the
resulting Git status before claiming success. Successful hooks may change the
message or merged content; do not compare these with pre-hook snapshots or reject
them merely for changing. Unexpected branch/topology/status results remain errors
to inspect, not grounds for automatic repair. A nonzero Git merge result still
stops the helper even when rerere has applied a saved resolution; leave that
state for the caller without trying to continue or commit it.

Repository hooks and custom merge drivers remain Git's responsibility; this
helper does not sandbox them or claim to make hostile configuration safe. No
network or production repository is used in tests.

## Verification

Use temporary real Git repositories with local test identity and isolated config;
never merge development branches in this repository as a test. Cover:
- one/zero known steps => squash; multiple steps/unknown prefixes => --no-ff;
  count only source-exclusive commits, keep graph history for real merges;
- both fast-forwardable and diverged clean histories; supplied multiline message,
  normal final newline, source preservation, parent count/IDs and final content;
- dirty tracked/staged/nonignored untracked states refused unchanged;
  ignored noncolliding files preserved and ignored colliding files not overwritten;
- missing/same branches, empty range, wrong/detached HEAD, empty messages,
  unfinished-operation markers including linked-worktree state resolution;
- actual conflicts remain unresolved with no commit/target advance and useful
  diagnostic; commit-hook failure preserves state; no-net-change squash is explicit;
- inherited Git routing overrides cannot affect an outside repository/index;
  explicit behavior overrides autostash/ff-only where necessary; populated rerere
  follows repository settings (including applied resolution with nonzero merge
  status), successful message/content hooks are allowed; help, syntax errors
  and Git unavailable;
- preserve all existing generator/journal tests and configured lint/format checks.

Use bounded failure injection where needed for otherwise unstable failures; assert
state/content and relevant diagnostics, not only return codes. Do not build a
framework for hypothetical Git extensions or retroactively rename history.

References: Git merge manual (no-overwrite-ignore, no-commit, squash/no-ff),
https://git-scm.com/docs/git-merge ; Git commit manual (verbatim cleanup),
https://git-scm.com/docs/git-commit .
