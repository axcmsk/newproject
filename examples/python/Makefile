.PHONY: check format lint test test-coverage reformat

PYTHON_PATHS ?= .
TEST_DIR ?= tests

check: format lint test

format:
	.venv/bin/python -m ruff format --check $(PYTHON_PATHS)

lint:
	.venv/bin/python -m ruff check $(PYTHON_PATHS)

test:
	python3 -m unittest discover -s $(TEST_DIR) -v

test-coverage:
	.venv/bin/coverage erase
	COVERAGE_FILE="$(CURDIR)/.coverage" COVERAGE_RCFILE="$(CURDIR)/.coveragerc" .venv/bin/coverage run -m unittest discover -s $(TEST_DIR) -v
	.venv/bin/coverage combine
	.venv/bin/coverage report
	.venv/bin/coverage html
	.venv/bin/coverage json

reformat:
	.venv/bin/python -m ruff format $(PYTHON_PATHS)
