.PHONY: check format lint test reformat

check: format lint test

format:
	.venv/bin/python -m ruff format --check tools newproject.py tests template/heavy/scripts

lint:
	.venv/bin/python -m ruff check tools newproject.py tests template/heavy/scripts

test:
	python3 -m unittest discover -s tests -v

reformat:
	.venv/bin/python -m ruff format tools newproject.py tests template/heavy/scripts
