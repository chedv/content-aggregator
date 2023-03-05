.PHONY: create_migration
create_migration:
	alembic revision --autogenerate -m "$(message)" --rev-id="$(rev_id)"

.PHONY: migrate
migrate:
	alembic upgrade head

.PHONY: revert_migration
revert_migration:
	alembic downgrade -1
