.PHONY: start-local up down

start-local:
	uvicorn main:app --reload

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans