# Python starter

The Makefile, ruff.toml and .coveragerc are starting defaults. Add application
code and tests, then adapt the paths and rules to the actual project. Generation
does not create Python packaging metadata or install dependencies.

Requires Python 3.9+ and GNU Make. From the project root, create the local
environment and install Ruff; coverage is optional:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install ruff==0.17.3
.venv/bin/python -m pip install coverage==7.10.7
```

Make check (also the default) checks formatting, runs lint and discovers
unittest tests. Individual targets are format, lint and test. Reformat applies
formatting only; follow it with make check. The default PYTHON_PATHS is `.`
and TEST_DIR is `tests`; edit the Makefile or override them, for example:

```sh
make check PYTHON_PATHS="src tests" TEST_DIR=tests
make reformat
make test-coverage
```

Test uses python3 from PATH. Ruff and coverage use .venv; choose matching Python
environments and install any application dependencies they need. No Make target
installs tools automatically. From elsewhere, use make -C /path/to/project.

Coverage is optional and excluded from check. Its defaults measure Python code
under the project root, omit tests and .venv, and collect Python subprocesses.
Adapt .coveragerc when changing layout or test paths. Each coverage run clears
measurement data, runs tests once, combines data, prints missing lines, and
writes coverage.json and htmlcov/index.html. Generated data and tool caches are
ignored by Git. For review, provide the measured source version and coverage.json
with per-file totals and missing lines; HTML is supplementary. There is no
coverage threshold. Use a newer Python if required by a tool release.
