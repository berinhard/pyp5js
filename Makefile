test:
	export PYTHONWARNINGS=ignore::flask.DeprecationWarning; pytest

update_dist:
	@python3 setup.py sdist bdist_wheel

upload_pypi:
	@twine upload dist/*
