serve:
		@python3 -m http.server

compile:
		@transcrypt -b -m -n sketch

update_dist:
		@python3 setup.py sdist bdist_wheel

upload_pypi:
		@twine upload dist/*
