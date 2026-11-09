# Python check specification and template convention

HUMAN requests renaming the specification and adding the check-command rule to
the template. Baseline be9149af8d45f279d1630594f1354dd157bc7cd0 on codex/check-helper;
standing no-merge/no-push instruction remains. Documentation short route.

LEAD owns docs/specs/check.md -> docs/specs/python-check.md, README.md,
root/base docs/workflow/PROJECT-RULES.md and this record. Update active links,
preserving historical pinned worklog paths. Add matching shared policy for
repository-local check commands once checks are configured; Python name and
full/selected/reformat interface follow the accepted helper. No invented checks,
tool dependencies or Python-only assumptions for other languages. Keep check
ownership and required full-check coverage; allow successful opt-in formatting
to satisfy formatting verification on unchanged inputs. README documents wrapper
commands and direct tool installation. The generator still installs only its
existing two helpers: no copying this repository-specific script or its spec.

LEAD performs configured documentation checks, commits, then REVIEWER Astra/high
statically reviews the exact checkpoint and evidence. Only reviewer write:
docs/worklog/118-python-check-template-rule-review.md. Review root/base consistency,
empty-project applicability, link validity, no false claim of installed helper,
and unchanged role authority. Commit report via accepted helper, verify report-only
child/clean state and release LEAD. No code/tests/generator changes or new agents
required for implementation; preserve reviewed history and leave work in branch.

LEAD ran `python3 tools/python_check.py` on unchanged executable sources with
updated templates: overall exit 0, format check 0 (10 files), lint 0, tests 0
(69 passed, 27.099s). `git diff --check` passed. Active README/spec/workflow/template
search found no old specs/check.md references; historical worklogs are untouched.
The shared Check commands section is identical in root/base. Final staged diff
check runs before the checkpoint commit and is reported with its exact hash.
