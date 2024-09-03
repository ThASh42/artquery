.PHONY: install
install:
	poetry install

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

.PHONY: update
update: install migrate ;

.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: cpsettingsdev
cpsettingsdev:
	cp core/artquery/settings/templates/settings.dev.py ./local/settings.dev.py