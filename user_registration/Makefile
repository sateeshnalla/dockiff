SHELL := /bin/bash
-include .env

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

requirements:
	pip freeze  > requirements.txt
run:
	pipenv run python manage.py runserver
