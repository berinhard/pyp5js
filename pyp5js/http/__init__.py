import glob
import mimetypes
import os
from pathlib import Path
from textwrap import dedent

import gunicorn.app.base

from pyp5js.config import SKETCHBOOK_DIR
from pyp5js.compiler import compile_sketch_js
from pyp5js.fs import SketchFiles

from pyp5js.http.web_app import app as pyp5js_web_app


def make_sketches_list(path):
    """Retrieve all sketches from a path an return a HTML page with links"""

    template = dedent(
        """
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>pyp5js server</title>
        </head>
        <body>
          Available sketches:
          <ul>
        {{PLACEHOLDER}}
          </ul>
        </body>
        </html>
    """
    ).strip()

    # Get all sub-directories which has a Python file inside, except "pyp5js"
    sketches = set(
        str(Path(os.path.dirname(filepath)).relative_to(path))
        for filepath in glob.glob(str(path / "*/*.py"))
    )
    if "pyp5js" in sketches:
        sketches.remove("pyp5js")

    return template.replace(
        "{{PLACEHOLDER}}",
        "\n".join(
            f'    <li> <a href="{sketch}">{sketch}</a> </li>' for sketch in sorted(sketches)
        ),
    )


def get_response_data(fobj):
    """Prepare HTTP response headers and body based on a fobj

    Note: not safe for large files (all the contents will be loaded in memory)
    """

    response_body = fobj.read()
    response_headers = [
        ("Content-Type", mimetypes.guess_type(fobj.name)[0]),
        ("Content-Length", str(len(response_body))),
    ]
    return response_headers, response_body


def sketch_files_app():
    """Handle WSGI requests to serve sketches (compiles + serve static files)"""

    base_path = SKETCHBOOK_DIR.resolve()  # must be a pathlib.Path instance
    base_path_str = str(base_path)

    def handler_app(environ, start_response):
        request_path = environ["PATH_INFO"]

        if request_path[0] == "/":
            # Remove slash from the beginning of the string so we can easily
            # operate this string as a sub-path from our base path
            # (`base_path / request_path` will work without overwritting
            # `base_path`).
            request_path = request_path[1:]

        if request_path == "":
            # Home page - list all available sketches on `base_path`.
            start_response("200 OK", [("Content-Type", "text/html")])
            return [make_sketches_list(base_path).encode("utf-8")]

        full_path = (base_path / request_path).resolve()
        if not str(full_path).startswith(base_path_str):
            # User tried something not allowed (as "/root/something" or "../xxx")
            start_response("403 FORBIDDEN", [("Content-Type", "text/plain")])
            return [b"Get out"]

        elif not full_path.exists():
            # Ouch, file/path not found (the endpoint for favicons, usually)
            start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
            return [b"File not found =/"]

        else:
            # Found an existing path (sketch) or a file

            if full_path.is_dir():
                # Probably inside a sketch directory, let's compile it
                # XXX: the sketch Python file should be the same as it's parent
                # directory name. Example: /home/user/mysketches/s1/s1.py
                sketch_files = SketchFiles(full_path.absolute().name)
                if not sketch_files.sketch_exists:
                    start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
                    return [b"Sketch not found =/"]
                compile_sketch_js(sketch_files)

                # TODO: should not compile sketch if file is not changed
                full_path = full_path / "index.html"

            with open(full_path, mode="rb") as fobj:
                response_headers, response_body = get_response_data(fobj)
                start_response("200 OK", response_headers)
                return [response_body]

    return handler_app


class SketchesWebApplication(gunicorn.app.base.BaseApplication):
    """Standalone gunicorn application

    Got from: <https://github.com/benoitc/gunicorn/blob/master/examples/standalone_app.py>
    """

    def __init__(self, options=None):
        self.options = options or {}
        self.application = sketch_files_app()
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
