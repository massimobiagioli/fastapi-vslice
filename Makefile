.PHONY: up down start-local test coverage

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans

start-local:
	uvicorn fastapi_vslice.main:app --reload

load-fixtures:
	poetry run load_fixtures

test:
	poetry run pytest -vv

coverage: test
	poetry run pytest --cov=fastapi_vslice

coverage-features: test
	poetry run pytest --cov=fastapi_vslice/features