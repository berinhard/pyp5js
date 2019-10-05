serve:
	@pyp5js serve

compile:
	@transcrypt -b -m -n sketch

update_dist:
	@python3 setup.py sdist bdist_wheel

upload_pypi:
	@twine upload dist/*

update_pyp5js:
	@python3 pyp5js/utils/update_pytop5js.py
