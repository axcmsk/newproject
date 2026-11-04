# Ruff formatting implementation evidence

Assignment: `/private/tmp/newproject-format-assignment/014-format-task.md` (also `docs/worklog/014-format-task.md`); SHA-256 `c73e2a773753c042417270e735f71a93f934a3919d106f2b1c8ca52e87534a61`. Baseline commit: `e30d588570c3ddae8dee556cdf8ab5b872b1494b`.

Ruff 0.17.3 formatted `newproject.py` and `tests/test_newproject.py`. LEAD's README and configuration changes were preserved. Before the decisive checks, the four inputs and assignment were copied to `/private/tmp/newproject-format-final/`. `cmp` confirmed README, ruff.toml, and the repository assignment match the LEAD assignment snapshot. Frozen input identities:

| Path | SHA-256 | Git blob ID |
| --- | --- | --- |
| `newproject.py` | `08c31334c6a9822c973885627c457684559db2cf0f2af387dd0bdce6cd9a2e7d` | `f636288282b57cdd1b11f3eac1d3125313d48b33` |
| `tests/test_newproject.py` | `dfd8562e7df976fae382ffff93e41d0f6725c7c0368af1e77e5414364c47e0df` | `425fde6b82c5746928a159f39696f4ccef7f0cde` |
| `README.md` | `e62293ea44ba1f286020d70b33a747e87a3c0d02776b8232efa662582f1f6401` | `247b0fe431cd6a81ce2f6a58dd7a3e6f8f872b90` |
| `ruff.toml` | `a096764ddca45b95b2543ac8cdbad4149d02e317ab452afd7e3feeda514d0c74` | `3379fdc3528432d01ab361d9ff3fdaa3e235ce81` |

Environment: Python 3.9.6, Git 2.54.0, Ruff 0.17.3 in `/private/tmp/newproject-ruff-venv`. All checks below ran at repository root and exited 0.

`python3 -m unittest discover -s tests -v`:

```text
test_ambient_git_template_is_ignored (test_newproject.CreationTests) ... ok
test_contaminated_environment_stays_in_fixture (test_newproject.CreationTests) ... ok
test_copy_failure_reports_partial_state_and_preserves_file (test_newproject.CreationTests) ... ok
test_git_environment_isolation_and_missing_git (test_newproject.CreationTests) ... ok
test_init_failure_partial_state (test_newproject.CreationTests) ... ok
test_invalid_git_states (test_newproject.CreationTests) ... ok
test_names_and_parent_git (test_newproject.CreationTests) ... ok
test_new_empty_and_existing_repositories (test_newproject.CreationTests) ... ok
test_target_refusals (test_newproject.CreationTests) ... ok
test_template_refusals (test_newproject.CreationTests) ... ok
test_traversal_failure_before_mutation (test_newproject.CreationTests) ... ok

----------------------------------------------------------------------
Ran 11 tests in 2.833s

OK
```

`/private/tmp/newproject-ruff-venv/bin/ruff check newproject.py tests/test_newproject.py`:

```text
All checks passed!
```

`/private/tmp/newproject-ruff-venv/bin/ruff format --check newproject.py tests/test_newproject.py`:

```text
2 files already formatted
```

`git diff --check`: no output.

AST comparison command:

```sh
python3 - <<'PY'
import ast
import pathlib
import subprocess

for path in ('newproject.py', 'tests/test_newproject.py'):
    baseline = subprocess.check_output(['git', 'show', 'e30d588570c3ddae8dee556cdf8ab5b872b1494b:' + path], text=True)
    current = pathlib.Path(path).read_text()
    assert ast.dump(ast.parse(baseline), include_attributes=False) == ast.dump(ast.parse(current), include_attributes=False), path
    print(path + ': AST equal to baseline (locations ignored)')
PY
```

```text
newproject.py: AST equal to baseline (locations ignored)
tests/test_newproject.py: AST equal to baseline (locations ignored)
```

AST equality establishes unchanged parsed code and assertions, ignoring source locations; it does not itself establish behavior under every environment. Independent static review remains pending.
