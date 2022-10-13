.PHONY: up down start-local

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans

start-local:
	uvicorn fastapi_vslice.main:app --reload