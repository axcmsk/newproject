# Project creation

## Approved user intent

Provide `python3 newproject.py NAME` to create a sibling of this repository,
copy only `template/` contents, and initialize Git on `main` without a commit.
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
- On success the target contains the template tree and its own Git repository,
  on an unborn `main` branch, without staged entries, commits or remotes added by
  this program. Preserve pre-existing Git configuration. Changing the unborn branch
  name to main is intended. Never delete existing user files or Git history.
- Validate arguments, source tree, target state and Git availability before target
  mutation. Template must exist, be a nonempty directory, and contain only regular
  files/directories; reject symlinks, special entries and any `.git` entry.
  Copy hidden template files too. Do not copy repository history, worklogs, script,
  caches or personal sibling `common` files unless actually part of the template.
- Use standard-library Python only, with a documented minimum version. Invoke Git
  without a shell and isolate Git operations from inherited GIT_* overrides that
  could redirect repository/index/config operations. Do not change global Git config.
- Repeated invocation after success fails clearly without changing existing content.
  Return zero only on success, nonzero on refusal/failure, with useful diagnostics
  including target path and any partial state left after mutation. No automatic
  recursive rollback or deletion of pre-existing directories. Failures before
  mutation leave the target unchanged. Concurrent hostile filesystem replacement
  is outside scope, but do not overwrite files that appear during copying.
- No initial commit, push, publication, dependency install or interactive prompt.

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
