# Adopt the local merge procedure

HUMAN requests integrating the existing helper into this repository's process;
new-project generation and template integration are deferred. Baseline:
1bf8446d6d3101dbc8523d6150ca5faee49b4ab0 on main.

Documentation short route: LEAD edits root PROJECT-RULES, PROCESS, LEAD, MERGE
and the merge specification introduction. Link the procedure at the merge handoff,
use the concrete tools/merge.py command, and reconcile the history-preservation
rule with helper-selected squash while preserving the source branch. Keep mode
selection out of agent instructions. Retain HUMAN authorization, acceptance,
check ownership and failure recovery. No script, template or generator changes;
no actual merge or push is requested. This root/template difference is explicit.

LEAD runs README checks and commits these documents and this evidence. REVIEWER
(Astra/high) statically reviews the committed scope and writes/commits only
056-adopt-merge-review.md, then returns ownership to LEAD. New process authority
is not relied on before acceptance.

## Checks

On the baseline plus these documentation-only edits, LEAD ran:

- `python3 -m unittest discover -s tests -v`: 40 tests passed in 14.600s.
- `.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts`: passed.
- `.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts`: passed, 6 files already formatted.
- `git diff --check`: passed; local links and the CLI were inspected.

Executable, configuration, template and test inputs are unchanged. No actual
branch merge, push or generator change was performed.
