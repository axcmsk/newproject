# Merge helper correction review

- Verdict: `CHANGES_REQUESTED`.
- Reviewed source and review-start HEAD:
  `598b812e31187f8ad459d5f449a05cfa85bb7d80`.
- Final contract: `docs/specs/merge.md` and task 039 at
  `07c6ec185055ba656a5286a275514f3768a25888`, accepted in
  `docs/worklog/044-merge-git-policy-review.md` at `836abe0`.
- Prior implementation review: `docs/worklog/042-merge-review.md` at `bc3327e`.
- Evidence: `docs/worklog/041-merge-implementation.md` at reviewed source.
- Scope: affected implementation/tests, prior findings and the approved policy
  amendment. No merge, push or adoption of the draft is authorized.
- Conditions allowing closure without re-review: none.
- Next owner/action: DISPATCHER routes the bounded R5 fixture correction to
  DEVELOPER and returns the checked correction for affected review.

## Prior findings

R1 is closed: the operation-scoped ff setting permits diverged squash despite
persistent ff-only configuration; the added real-Git case checks parent, message,
both sides' content, source preservation and unchanged configuration.

R2 is closed in the product code: diff status 0, 1 and error are distinguished,
and errors stop before commit with diagnostic and partial-state reporting. Its
new evidence fixture needs the correction below.

R3 is superseded by HUMAN's accepted policy. Successful message/content hooks
are permitted, with real-hook cases asserting success and committed changes.
No unwanted pre/post semantic comparison was introduced.

R4's product/evidence gap is addressed: the added submodule case exercises dirty
submodule refusal and preserved branch/content state. The populated rerere case
demonstrates saved resolution reuse with the repository's autoupdate setting,
a nonzero merge result, unchanged target and retained MERGE_HEAD. The helper now
honors rerere configuration and stops without retrying or committing that result.

## R5 — Restore and isolate the in-process diff-error fixture

Location: `tests/test_merge.py:329-347`, test_diff_error_stops_commit.

The test mocks os.getcwd to return its temporary repository before saving
old = Path.cwd(). The saved value is consequently the fixture path, not the real
starting directory. Its finally block changes back to that same temporary path;
TemporaryDirectory cleanup then leaves the test process in a deleted directory.
This can break later tests or tools that use the current directory and makes the
suite order-dependent.

Unlike helper() subprocess cases, this in-process call also inherits the runner's
real environment instead of self.env. Git can therefore read the user's HOME/XDG
configuration and global hooks rather than the isolated fixture configuration
required by the contract.

Closure: remove the unnecessary cwd mock, save the actual starting directory
before changing it, restore it reliably before fixture deletion, and apply the
fixture environment during the in-process helper call. Retain the injected diff
error and assertions proving no commit and preserved staged content. Rerun the
affected test and configured checks; no product behavior change is required.

## Evidence and boundary

The report supplies 40 passing tests and passing expanded Ruff lint/format results
on the committed inputs. REVIEWER ran no checks or project code. The new defect
is established by static control-flow inspection; it was not reproduced here.
Checks remain host-specific, and this verdict does not reopen accepted policy.

Review began at the exact source with a clean tree. Only this report may be staged
and committed after HEAD/index/path verification. Return its commit separately
and release ownership; the report commit preserves this failed verdict.
