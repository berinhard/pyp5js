@echo off

IF /I "%1"=="test" GOTO test
IF /I "%1"=="update_dist" GOTO update_dist
IF /I "%1"=="upload_pypi" GOTO upload_pypi
IF /I "%1"=="run_demo" GOTO run_demo
GOTO error

:test
	set PYTHONWARNINGS=ignore::flask.DeprecationWarning && pytest
	GOTO :EOF

:update_dist
	@python3 setup.py sdist bdist_wheel
	GOTO :EOF

:upload_pypi
	@twine upload dist/*
	GOTO :EOF

:run_demo
	PUSHD docs/pyodide
	python -m http.server
	POPD
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
