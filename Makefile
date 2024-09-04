.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: makemigrations
makemigrations:
	poetry run python -m core.manage makemigrations

.PHONY: runserver
runserver:
	poetry run python -m core.manage runserver

.PHONY: createsuperuser
createsuperuser:
	poetry run python -m core.manage createsuperuser

.PHONY: flake8
flake8:
	poetry run flake8

cpsettingsdev:
	cp core/artquery/settings/templates/settings.dev.py ./local/settings.dev.py

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: update
update: install migrate install-pre-commit;
