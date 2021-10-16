test:
	export PYTHONWARNINGS=ignore::flask.DeprecationWarning; pytest

update_dist:
	@python3 setup.py sdist bdist_wheel

upload_pypi:
	@twine upload dist/*

# helper command for the maintainer to refresh the docs files
refresh_transcrypt_docs:
	cd docs/examples/transcrypt; for x in `ls -d */`; do SKETCHBOOK_DIR="/home/bernardo/envs/pyp5js/docs/examples/transcrypt/" pyp5js compile $$x --refresh --template "/home/bernardo/envs/pyp5js/docs/examples/transcrypt/index.html.template"; done;

refresh_pyodide_docs:
	cd docs/examples/pyodide; for x in `ls -d */`; do SKETCHBOOK_DIR="/home/bernardo/envs/pyp5js/docs/examples/pyodide" pyp5js compile $$x --refresh --template "/home/bernardo/envs/pyp5js/docs/examples/pyodide/index.html.template"; done;

refresh_demo:
	SKETCHBOOK_DIR="/home/bernardo/envs/pyp5js/docs/" pyp5js compile pyodide --refresh --template "/home/bernardo/envs/pyp5js/docs/pyodide/index.html.template";
