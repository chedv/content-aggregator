.PHONY: create_migration
create_migration:
	pipenv run alembic revision --autogenerate -m "$(message)" --rev-id="$(rev_id)"

.PHONY: migrate
migrate:
	pipenv run alembic upgrade head

.PHONY: revert_migration
revert_migration:
	pipenv run alembic downgrade -1

.PHONY: run_black
run_black:
	pipenv run black --config pyproject.toml src tests migrations

.PHONY: check_black
check_black:
	pipenv run black --check --config pyproject.toml src tests migrations

.PHONY: mypy
mypy:
	pipenv run mypy

.PHONY: api_tests
api_tests:
	pipenv run pytest tests/api_tests
