# Simplified check guidance: review

Verdict: `ACCEPTED`.

Reviewed checkpoint and initial HEAD:
`1e264cc72e07a1dbcb8cb4e9e7765ee37129d01c`, on `codex/check-helper`.
Baseline: `7de37f5b41172ec2f6aeeb5109908e89e3ed84cd`.
At this final review start, the index was clean and the only working-tree change
was the reviewer's untracked draft from the paused initial review. Only reviewer write:
`docs/worklog/120-simplify-check-guidance-review.md`.

## Scope and conclusions

Static documentation review covers task 119 and matching edits to root/base
PROJECT-RULES, against HUMAN's request for substantially shorter guidance and
latest refinements to retain --reformat but omit the README-documentation sentence.
No blocking findings.

The shared rule now states the requested Python helper convention, conditioned
on availability, mentions --reformat for applying formatting, and prohibits
inventing tools/settings or unconfigured checks. It omits the redundant README
instruction and detailed CLI policy as explicitly requested.
It neither claims the generator installs the helper nor forces an empty project
to create checks prematurely.

The existing precommit paragraph still requires all configured tests, lint and
formatting verification. A missing configured check remains a blocker in the
following rules, so the shorter availability wording does not permit silently
skipping required checks. The successful-formatter substitute and unchanged-input
restriction are preserved in the verification paragraph. Role/check ownership
and review requirements remain unchanged. Both shared edits match between root
and base; the check-commands link still resolves to the retained heading.

Helper, generator, specification and README behavior are unchanged. Removal of
detailed ordering/selection policy is intentional under the latest HUMAN request,
not a change to this repository's accepted CLI contract.

## Evidence and handoff

Task 119 records the actual full helper run on baseline executable sources with
updated templates: overall 0, format-check 0 for ten files, lint 0 and tests 0
with 69 passing tests (26.654s) on the corrected template text. The earlier
28.426s run remains recorded separately. Working-tree whitespace validation passed.
LEAD additionally reported successful staged whitespace validation before the
corrected checkpoint commit, exit code 0, chunk `257ec8`; the reviewer draft was
excluded. No report commit or completed acceptance handoff occurred for the
superseded initial checkpoint.

REVIEWER ran no executable project checks. Adding this report does not alter
checked inputs. Commit only this report with the accepted strict report helper,
verify the direct parent, report-only diff and clean state, then release writer
ownership to LEAD. Return the report commit separately from the accepted source.
Keep all work on `codex/check-helper`, without merge or push.
