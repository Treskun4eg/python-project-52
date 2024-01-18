MANAGE := poetry run python manage.py

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

setup:
	cp -n .env.example .env || true
	make install
	make migrate

PORT ?= 8000
start:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

check:
	poetry check

lint:
	poetry run flake8 .

.PHONY: test
test:
	@poetry run pytest