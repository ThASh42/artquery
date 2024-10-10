.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: lock
lock:
	poetry lock

.PHONY: migrate
migrate:
	poetry run python -m artquery.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m artquery.manage makemigrations

.PHONY: runserver
runserver:
	poetry run python -m artquery.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m artquery.manage createsuperuser

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
