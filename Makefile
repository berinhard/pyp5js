test:
	@pytest

update_dist:
	@python3 setup.py sdist bdist_wheel

upload_pypi:
	@twine upload dist/*

update_pyp5js:
	@python3 pyp5js/pre_compile/update_pytop5js.py

