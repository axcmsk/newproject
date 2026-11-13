.PHONY: check format lint test test-coverage reformat

check: format lint test

format:
	.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts

lint:
	.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts

test:
	python3 -m unittest discover -s tests -v

test-coverage:
	.venv/bin/coverage erase
	COVERAGE_FILE="$(CURDIR)/.coverage" COVERAGE_RCFILE="$(CURDIR)/.coveragerc" .venv/bin/coverage run -m unittest discover -s tests -v
	.venv/bin/coverage combine
	.venv/bin/coverage report
	.venv/bin/coverage html
	.venv/bin/coverage json

reformat:
	.venv/bin/python -m ruff format tools newproject.py tests template/heavy/scripts
