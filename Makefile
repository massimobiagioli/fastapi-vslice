.PHONY: up down start-local test

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans

start-local:
	uvicorn fastapi_vslice.main:app --reload

test:
	poetry run pytest -vv