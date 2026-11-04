# Script implementation evidence

- Baseline: `ae40b4c2641e0c8ed4ed9b55872f81ab19166303`.
- Approved specification: `docs/specs/newproject.md`, frozen at `/private/tmp/newproject-script-spec-v1`; review `docs/worklog/007-script-spec-review.md`, ACCEPTED.
- Snapshot before decisive tests: `/private/tmp/newproject-implementation-v1` (SHA-256):
  - `newproject.py`: `62fa656357ceb870fff3bc7a7a9cfe2f2c5f53718ff7ffc5f18592c5b29849ab`
  - `.gitignore`: `6feaded4e28ea86e001a6751b4e3d960e8b7c31b9616ff9936b79297086e809b`
  - `tests/test_newproject.py`: `33792f50246e8b4d6cc263158d4e77edc5a78c48fd39a397f4019af23031521f`
  - `README.md`: `e8f13fd9994dfdbc87478c371cfeae138ecff266c9bf0a980802557222b6faab`
  - `docs/workflow/PROJECT-RULES.md`: `d1589a994e33cf1d54fb9e2a91d1b54ded2700eaeba54bdc18c56dd580dcbd19`
- Working paths matched these SHA-256 hashes after testing. Python 3.9.6; Git 2.54.0.
- Decisive command: `python3 -m unittest discover -s tests -v`. Result: eight test methods passed, 2.121 seconds, `OK`. Tests use temporary fixtures, the real CLI and Git, and injected init/copy failures. No actual sibling project was created.
- `git diff --check` returned zero. This does not inspect untracked files.
- During development the initial suite failed to import due to a syntax error in the test fixture (`git.chmod 0o755`); corrected to `git.chmod(0o755)` before the frozen snapshot. An exploratory run then passed all eight methods. No test failures occurred on the frozen version.
- Limitations: this is one Python/Git/OS combination; hostile concurrent filesystem replacement is outside the specification. The copy-failure case uses an in-process injection to create a destination collision, while the other cases exercise the subprocess CLI.

## Round 2

Review `009-script-review.md` requested changes. Traversal errors now abort preflight; new repositories initialize with a temporary empty Git template; Git system configuration is disabled for script-invoked Git. Fixture environments strip inherited `GIT_*`, set HOME and XDG_CONFIG_HOME to temporary paths, and disable system configuration. The CLI strips inherited `GIT_*` and sets `GIT_CONFIG_NOSYSTEM=1`; the fixture-supplied HOME and XDG paths carry through. The regression deliberately supplies redirected Git variables and checks sentinel repository and configuration bytes remain unchanged. Existing-target refusal and repeat checks compare file bytes, directories and symlink targets. A real Git template with staged index and remote configuration tests initialization isolation. An injected child traversal failure asserts diagnostics and unchanged existing target.

Frozen before decisive checks: `/private/tmp/newproject-implementation-v2`, SHA-256:

- `newproject.py`: `ae2decacfca8e005d24fc0f6004d083cfb66d1af2bec2f17cf3b0726d91f7c3c`
- `.gitignore`: `6feaded4e28ea86e001a6751b4e3d960e8b7c31b9616ff9936b79297086e809b`
- `tests/test_newproject.py`: `26390f08051900601884d837a2e8e5f9a203dae56a6e79c7c734f10cf788fac6`
- `README.md`: `e3b190c23273c335c55994e19487c1e12c145e4b9cd1686c8187485b66fb21f2`
- `docs/workflow/PROJECT-RULES.md`: `d1589a994e33cf1d54fb9e2a91d1b54ded2700eaeba54bdc18c56dd580dcbd19`

Decisive command, with intentionally contaminated inherited settings:

```sh
GIT_DIR=/nonexistent/external-repo GIT_WORK_TREE=/nonexistent/external-worktree GIT_INDEX_FILE=/nonexistent/external-index GIT_CONFIG_GLOBAL=/nonexistent/external-config GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=init.templateDir GIT_CONFIG_VALUE_0=/nonexistent/external-template XDG_CONFIG_HOME=/nonexistent/external-xdg python3 -m unittest discover -s tests -v
```

Result: 11 test methods passed in 2.606 seconds, `OK`. Python 3.9.6 and Git 2.54.0. An exploratory run before freezing also passed the 11 methods. The round 1 snapshot and results above remain preserved. Limitations remain as in round 1; traversal and copy errors use deterministic in-process injection, while Git-template and environment tests exercise the real CLI and real Git.
