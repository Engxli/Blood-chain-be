pre-commit: format lint test

format:
	poetry run isort .
	poetry run black .
lint:
	poetry run mypy .
	poetry run pylint **/*.py
test:
	poetry run pytest
