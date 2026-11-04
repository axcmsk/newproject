# Lint implementation evidence

Assignment: `017-lint-task.md`, baseline `6b5fd6d7fbb40acf0f89d245bdd8f7cfd2d6968e`. LEAD confirmed README unchanged and frozen before decisive checks. Frozen copies are in `/private/tmp/newproject-lint-snapshot-018/`; exact Git blob IDs before and after checks:

```text
293876835b8e6f4839572fa4f241d9dc32cac083 newproject.py
2fbc1d7db75dfad615a84ba6838ed83f7f3e07d5 tests/test_newproject.py
a2a7e7877c2c1e818cdd075113ae21e0fa8691b2 ruff.toml
247b0fe431cd6a81ce2f6a58dd7a3e6f8f872b90 README.md
```

Ruff selects E, W, F, I, N, B, UP, S and C90 with Python 3.9 and complexity 10. E501 is excluded because the formatter may retain long lines. Inline S603 and S607 suppressions identify the no-shell Git/controlled test subprocess calls and intended PATH lookup. No other exclusions were added.

Compared with baseline, `validate_target` calls the extracted `validate_existing_repo` at the same point and returns true only after the same ordered Git checks; the checks, arguments, refusal messages and exception flow remain unchanged. `main` remains the caller and catches the renamed internal exception. `capture_output=True` sets both pipes as before; Git still uses its resolved path and argument list, while tests use the same executables and arguments. Import order changed only. Assertions and fixtures are unchanged. The existing suite covers successful new/empty/existing targets and refusals including malformed, bare, staged and referenced repositories, as well as injected traversal, initialization and copy failures. No helper-specific tests were added. No behavior change identified. These checks do not establish comprehensive security or correctness.

Versions: Python 3.9.6, Git 2.54.0, Ruff 0.17.3. All commands below exited 0, executed in repository root after freezing source/config and README. Raw output:

```text
$ python3 -m unittest discover -s tests -v
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
Ran 11 tests in 2.767s

OK
$ /private/tmp/newproject-ruff-venv/bin/ruff check newproject.py tests/test_newproject.py
All checks passed!
$ /private/tmp/newproject-ruff-venv/bin/ruff format --check newproject.py tests/test_newproject.py
2 files already formatted
$ git diff --check
(no output)
$ git hash-object newproject.py tests/test_newproject.py ruff.toml README.md
293876835b8e6f4839572fa4f241d9dc32cac083
2fbc1d7db75dfad615a84ba6838ed83f7f3e07d5
a2a7e7877c2c1e818cdd075113ae21e0fa8691b2
247b0fe431cd6a81ce2f6a58dd7a3e6f8f872b90
```

## Second source version

LEAD requested explanatory comments for each selected group and the deliberately unselected policies. Only comments and layout in `ruff.toml` changed; its effective settings and the Python source, tests and README remain unchanged. The first snapshot and results above are retained as round 1. Round 2 frozen copies are in `/private/tmp/newproject-lint-snapshot-018-v2/`. The unchanged source means the round 1 full suite applies; the lint, format and whitespace checks were rerun on round 2. All exited 0:

```text
$ /private/tmp/newproject-ruff-venv/bin/ruff check newproject.py tests/test_newproject.py
All checks passed!
$ /private/tmp/newproject-ruff-venv/bin/ruff format --check newproject.py tests/test_newproject.py
2 files already formatted
$ git diff --check
(no output)
$ git hash-object newproject.py tests/test_newproject.py ruff.toml README.md
293876835b8e6f4839572fa4f241d9dc32cac083
2fbc1d7db75dfad615a84ba6838ed83f7f3e07d5
afdf11150e40e3acadd76f5859ecf8cb96ea41c5
247b0fe431cd6a81ce2f6a58dd7a3e6f8f872b90
```
