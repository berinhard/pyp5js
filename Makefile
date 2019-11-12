DOCKERHUB_USER ?= ${USER}

test:
	@pytest

serve:
	@pyp5js serve .

compile:
	@transcrypt -b -m -n sketch

update_dist:
	@python3 setup.py sdist bdist_wheel

upload_pypi:
	@twine upload dist/*

update_pyp5js:
	@python3 pyp5js/pre_compile/update_pytop5js.py

docker-build:
	docker build -t pyp5js .

docker-tag:
	docker tag pyp5js ${DOCKERHUB_USER}/pyp5js:$(shell git rev-parse HEAD | head -c 8)
	docker tag pyp5js ${DOCKERHUB_USER}/pyp5js:latest

docker-push:
	docker push ${DOCKERHUB_USER}/pyp5js

docker-serve:
	docker run --publish=8000:8000 --volume=$(shell pwd):/sketches --rm pyp5js

docker-sh:
	docker run --publish=8000:8000 --volume=$(shell pwd):/sketches --rm -it pyp5js bash

.PHONY: test serve compile update_dist upload_pypi update_pyp5js docker-build docker-tag docker-push docker-serve docker-sh
