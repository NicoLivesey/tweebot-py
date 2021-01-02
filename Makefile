SLUG := tweebot
DOCKER_IMAGE_LOCAL := "${SLUG}-local"
DOCKER_IMAGE_PROD := ${SLUG}

ENV_FILE := ".env"

clean: ## remove all build, test, coverage and Python artifacts
	@rm -fr build/ dist/ .eggs/ public/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

	@rm -fr .coverage cov-report .pytest_cache


test:  ## run tests and coverage quickly with the default Python
	pytest


install-dev-socle: ## install the package for developement
	make clean
	pip install -r requirements/requirements_socle.txt


install-dev-collector: ## install the package for developement
	make clean
	pip install -r requirements/requirements_collector.txt


install-dev: ## install the package for developement
	make install-dev-socle
	make install-dev-collector


install: ## install the package to the active Python's site-packages
	make clean
	pip install -r requirements/requirements_runtime.txt
	pip install -r requirements/requirements_tests.txt


init: ## setup the dev enviroment
	make install-dev
	make test
	make help


docker-build:  ## [DEV  ] build docker image without downloading the model
	@echo "Building image ${DOCKER_IMAGE_LOCAL}"
	docker build -t ${DOCKER_IMAGE_LOCAL} .


docker-exec: ## [DEV  ] run cmd inside dev docker
	docker run --rm \
	--name ${DOCKER_IMAGE_LOCAL} \ 
	--env-file= ${ENV_FILE} \
	--it ${DOCKER_IMAGE_LOCAL}