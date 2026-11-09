# Python check specification and template convention: review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`6b49399308b85f3a40c251922e191edb2b37855a`, on `codex/check-helper`.
Baseline: `be9149af8d45f279d1630594f1354dd157bc7cd0`.
The index and working tree were clean at review start. Only reviewer write:
`docs/worklog/118-python-check-template-rule-review.md`.

## Scope and conclusions

Static documentation short-route review covers task 117, the specification rename
to `docs/specs/python-check.md`, README's updated link, and root/base PROJECT-RULES
changes against HUMAN's requested rename and template convention. No blocking
findings.

The renamed specification preserves the accepted helper behavior and clarifies
the distinction between this repository's script and a shared template convention.
README points to the existing renamed document. Static search found no stale
`specs/check.md` or relative `check.md` links in current README, specifications,
workflow or template documents. Historical pinned worklog paths remain untouched.

The shared Check commands section is identical in root and base. It applies
after a project establishes its checks, prohibits inventing checks/settings and
rejects unavailable selections. Thus an empty generated project is not required
to pretend checks or tools are already configured. Python gets the agreed helper
name; other languages are not forced to use Python, this repository's Ruff setup,
unittest command or target paths.

The convention preserves sequential format/lint/tests ordering, common formatter/
lint targets, selected-step failure handling, compatible reformat selection and
required full-check coverage. Successful opt-in formatting supplies formatting
verification without repeating it on unchanged inputs. The common precommit rule
links to this configured procedure while retaining required checks, saved evidence
and unchanged-input reuse. Role/execution ownership remains unchanged.

The generator and executable sources are unchanged. Its existing helper list
still contains only merge.py and review_commit.py; no Python check script or
specification is copied. The new text defines how projects expose their own
configured checks and makes no false claim that the helper is installed.

## Evidence and limitations

Task 117 records the actual full `python3 tools/python_check.py` run with overall
exit 0, format-check exit 0 for ten files, lint exit 0 and unittest exit 0 with
69 passing tests (27.099s), on unchanged executable inputs and updated templates.
Working-tree whitespace validation passed. LEAD additionally reported successful
staged whitespace validation immediately before the checkpoint in a sequential
command, exit code 0, chunk `055b3d`.

REVIEWER inspected the documents and saved evidence statically and ran no project
checks. Adding this report does not alter checked inputs. Actual project-specific
tool choices and wrapper implementation remain future configuration work in each
generated project, under its normal development/review process.

## Handoff

Commit only this report using the accepted strict report helper with the recorded
HEAD, verify the report-only direct child and clean repository state, then release
writer ownership to LEAD. Return the report commit separately from the accepted
checkpoint. This documentation stage requires no implementation handoff. Keep
the work on `codex/check-helper`; no merge or push is authorized.
