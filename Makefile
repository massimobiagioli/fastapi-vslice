.PHONY: start-local up down

start-local:
	uvicorn fastapi_vslice.main:app --reload

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans