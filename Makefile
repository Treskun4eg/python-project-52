MANAGE := poetry run python manage.py

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

setup:
	cp -n .env || true
	make install
	make migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: check
check:
	poetry check

lint:
	poetry run flake8 task_manager

.PHONY: test
test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

.PHONY: makemessages
makemessages:
	poetry run django-admin makemessages -l ru

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

run-dev:
	poetry run python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application