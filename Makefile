lint:
	flake8

lintstats:
	flake8 --statistics --count -qq

lintfix:
	autopep8 --aggressive -i -r --max-line-length=100 fusebox

.PHONY: docker-build
docker-build:
	docker build -t titomiguelcosta/fusebox -f Dockerfile .

.PHONY: docker-run
docker-run:
	docker-compose up

.PHONY: push
docker-push:
	docker push titomiguelcosta/pocket:latest

.PHONY: deploy
deploy:
	php dep deploy dev
