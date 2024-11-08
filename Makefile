include .env
export

POETRY := python3.10 -m poetry

VENV_PATH = .venv

ifeq ("$(wildcard $(VENV_PATH))", "")
	PYTHON=$(shell which python3)
else
	PYTHON=$(VENV_PATH)/bin/python3
endif

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' ${MAKEFILE_LIST} | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

install: ## install poetry packages
	poetry install

init: install ## init poetry
	poetry run pre-commit install

requirements.txt: ## generate requirements.txt
	$(POETRY) export -f requirements.txt --output requirements.txt

run:
	$(PYTHON) -m src

build: ## build service
	docker compose -f docker-compose.yml build

run_app: ## run application
	scripts/run_app.sh
