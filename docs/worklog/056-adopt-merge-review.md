# Local merge procedure adoption review

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `87110b550f3e5539735bdafc9814dd738e875bfc`.
- Baseline: `1bf8446d6d3101dbc8523d6150ca5faee49b4ab0`.
- Assignment/evidence: `docs/worklog/055-adopt-merge-procedure.md` at source.
- Scope: root PROJECT-RULES, PROCESS, LEAD, MERGE and merge-specification
  introduction; no helper, template or generator change.
- Findings and conditions: none.
- Next owner/action: LEAD reports adoption after checking the report commit;
  no actual merge or push is authorized by this task.

The root entry points consistently route HUMAN-commanded merges to MERGE and
the existing tools/merge.py. The concrete command matches the fixed-main CLI,
and the helper already exists on baseline main. Its mode selection is delegated
to the script rather than duplicated in agent instructions. The instruction
preserves explicit authorization, source/current-main acceptance, exclusive
ownership, local files including ignored files, affected validation, and failure
handling even when a commit already exists. A refusal cannot be bypassed with a
manual merge.

PROJECT-RULES now permits a helper-selected squash result on main while retaining
the source branch and reviewed commits; it does not authorize rewriting those
commits. The root/template difference is expressly documented, and templates
remain unchanged. Existing roles still own checks and review; adopting the Git
helper does not authorize LEAD to run product checks or accept unreviewed work.

Evidence 055 reports fresh passing 40-test, Ruff lint/format and whitespace checks.
These are supplied LEAD results; REVIEWER ran no executable checks. Review was
static and began at the exact source on main with a clean tree. Only this report
may be committed after HEAD/index/path verification. Return its actual commit
hash separately and release writer ownership to LEAD.
