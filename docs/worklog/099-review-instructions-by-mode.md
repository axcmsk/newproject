# Review instructions by workflow mode

HUMAN approved keeping strict report-only instructions in common REVIEW-COMMIT
and the heavy invocation with fixed STATE/journal paths in HEAVY. Baseline:
1e463d57882559e0845402542076d628a641a4cb. Branch:
codex/review-instructions-by-mode. No script or generator behavior changes.

Documentation short route. LEAD owns root/base docs/workflow/REVIEW-COMMIT.md,
template/heavy/docs/workflow/HEAVY.md and this record. Remove the generic
operational-path procedure from normal, keep root/base identical, and put the
fixed docs/workflow/STATE.md and docs/workflow/work-log.jsonl command in HEAVY.
Keep explicit permission, pinned-input exclusions, STATE block/journal checks,
tracked/unstaged prerequisites, writer handoff and separate operational closeout.
Omit each option when its path is not authorized or is pinned; other paths are
buffered rather than substituted. Do not broaden write authority or duplicate
common success/failure instructions. The helper's generic contract is unchanged.

LEAD runs README checks, commits, then REVIEWER Astra/high independently reviews
the exact checkpoint and saved evidence. Only reviewer write:
docs/worklog/100-review-instructions-by-mode-review.md. Commit report using the
accepted strict helper; verify report-only child and release ownership. LEAD
integrates accepted changes through merge.py, preserving branch; no push.

LEAD checked baseline executable inputs with updated templates:
`python3 -m unittest discover -s tests -v` passed 59 tests (24.162s);
`.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`
passed; `.venv/bin/python -m ruff format --check tools newproject.py tests
template/heavy/scripts` passed (8 files); `git diff --check` passed. `cmp`
confirmed identical root/base guides. No workflow/template references remain to
the removed operational-changes anchor (rg returned no matches). Final staged
diff check is required in the sequential commit command and reported with its hash.
