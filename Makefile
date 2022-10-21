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
ifdef filter
	poetry run pytest $(filter) -vv
else
	poetry run pytest -vv
endif

coverage: test
	poetry run pytest --cov-report term-missing --cov=fastapi_vslice

coverage-features: test
	poetry run pytest --cov-report term-missing --cov=fastapi_vslice/features