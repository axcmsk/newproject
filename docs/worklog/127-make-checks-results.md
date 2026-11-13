# Make checks implementation evidence

Specification: `docs/worklog/125-make-checks.md` pinned to `b0c33c1f56864d56bce96d437467dc9dd6ea03de`; accepted spec review: `docs/worklog/126-make-spec-review.md` pinned to `3cd214f6bd7e90068c06c6518a1c3cb29b758dae`.

Checked source: working tree based on `3cd214f6bd7e90068c06c6518a1c3cb29b758dae`, including the implementation and released documentation committed with this evidence. GNU Make 3.81, Python 3.9.6, Ruff 0.17.3.

- `make check`: exit 0; format and lint passed; 59 tests passed (23.634s).
- `make format`: exit 0, 8 files already formatted. `make lint`: exit 0, all checks passed. `make test`: exit 0, 59 tests passed (23.192s).
- From `/tmp`, `make -C /Users/andreikondratev/src/newproject check`: exit 0; 59 tests passed (23.081s).
- In a temporary copy of the Makefile, with the real `.venv` linked and all target paths present, `make -C "$taskdir" format` returned 2 on `value=  1` and left the file unchanged. `make -C "$taskdir" reformat` returned 0 and changed it to `value = 1`; a subsequent `make -C "$taskdir" format` returned 0.
- In a separate temporary copy, fake Ruff recorded its arguments and returned 7 for format; fake `python3` recorded its arguments. `PATH="$taskdir/bin:$PATH" make -C "$taskdir" check` returned 2 and recorded only `-m ruff format --check tools newproject.py tests template/heavy/scripts`. `PATH="$taskdir/bin:$PATH" make -k -C "$taskdir" check` returned 2 and additionally recorded `-m ruff check tools newproject.py tests template/heavy/scripts` and `-m unittest discover -s tests -v`. Make reported `Error 7` in both cases.
- `rg -n 'python_check\.py|python-check\.md' --glob '!docs/worklog/**'`: no active references found.

The temporary fixtures did not alter repository sources. Independent static review remains required.
