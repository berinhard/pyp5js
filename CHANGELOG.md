Development
-----------

0.7.2
-----
- Remove existing sketch after clearing/running it again [PR #199](https://github.com/berinhard/pyp5js/pull/199)
- Add share button to demo editor [PR #205](https://github.com/berinhard/pyp5js/pull/205)
- Fixed bug of adding new lines when saving Sketch in Windowns [PR #209](https://github.com/berinhard/pyp5js/pull/209)
- Upgrade pyp5js dependencies versions [PR #220](https://github.com/berinhard/pyp5js/pull/220)
- Run CI for Python 3.10 version [PR #219](https://github.com/berinhard/pyp5js/pull/219)

0.7.1
-----
- Create sketch using p5.js from CDN [PR #191](https://github.com/berinhard/pyp5js/pull/191)
- Add `keyIsDown` event to Transcrypt mode - [PR #187](https://github.com/berinhard/pyp5js/pull/187)
- Fix bug with multiple events calls - PR #187 too
- Serve JS files if `--local` flag [PR #195](https://github.com/berinhard/pyp5js/pull/195)
- Force `utf-8` as the lib's default encoding [PR #193](https://github.com/berinhard/pyp5js/pull/193)
- Fix preload function bug in both modes - [PR #196](https://github.com/berinhard/pyp5js/pull/196)

0.7.0
-----
- Remove `from pyp5js import *` requirement under transcrypt [PR #183](https://github.com/berinhard/pyp5js/pull/183/)
- Make local code editor collapsible [PR #184](https://github.com/berinhard/pyp5js/pull/184/)
- Add `mouseWheel` event to Pyodide's demo [PR #185](https://github.com/berinhard/pyp5js/pull/185/)

0.6.0
-----
- Add transcrypt interpreter choice to web editor - [PR #175](https://github.com/berinhard/pyp5js/pull/175)
- Upgrade Transcrypt to 3.9.0
- Upgrade Pyodide to v0.18.1 - [PR #181](https://github.com/berinhard/pyp5js/pull/181)
- Enable to use custom templates files to generate and compile index.html - [PR #177](https://github.com/berinhard/pyp5js/pull/177)
- Add docs on Pyodide examples - [PR #178](https://github.com/berinhard/pyp5js/pull/178)

0.5.2
-----
- Pyodide mode bugfix for missing `P3D` global definition
- Processing-like PVector class under transcrypt mode
- Processing-like PVector class under pyodide mode

0.5.1
-----
- Minor fix in view sketch HTML

0.5.0
-----
- Support to Pyodide as the Python interpreter

0.4.5
-----
- Support to get/set pixels with Transcrypt interpreter
- `pyp5js` can run on top of Gitpod.io

0.4.4
-----
- Fix to allow directories name with spaces - PR #127

0.4.3
-----
- Fix conflict with p5.js `clear` method and Python
- Upgrade `p5.js` version to `1.0.0`
- Use local file for Ace editor

0.4.2
-----
- Keep Python functions with name conflict with p5.js working as expected
- `createCanvas` now returns `p5.Renderer`
- Fix `transcrypt` error on Windows
- Add support to `loadImage`

0.4.1
-----
- Fix bug of null `_P5_INSTANCE`


0.4.0
-----
- Display sketch with code
- Add ACE editor to edit the sketch code
- Add aliases to Processing.py functions & constants (`size`, `pushMatrix`, `popMatrix`, `pushStyle`, `pushStyle`, `P3D`)

0.3.5
-----
- Fix issue with assets

0.3.4
-----
- Update sketch's template
- Add unit tests to the Flask API
- Base style for the web client

0.3.3
-----
- Validate sketch name
- Add base templates for the web app
- Add iframe with example 000 to the index

0.3.2
-----
- Ensure the sketchbook dir always exists

0.3.1
-----
- Fix build without web application assets

0.3.0
-----
- Create `pyp5js serve` command
- Add `SKETCHBOOK_DIR` to configure the sketchbook's directory
- Local web app to compile sketches on the fly and to create sketches

0.2.0
-----
- Rename pyp5.js module from pytop5js to pyp5js
- Enable keyword argument
- Enable checking for existence in dictionary keys
- Commands now printing index files as URI

0.1.1
-----
- Fix install issue

0.1.0
-----
- Simplification of pytop5js usage
- Support p5.dom.js library
- Fixes on monitor observer

0.0.7
-----
- Fix bug with monitor not running transcrypt more than once

0.0.6
-----
- Add flag on new commmand to monitor sketch after creating it
- Fix bug when running the monitor command from the sketch's directory
- Update width and height values on createCanvas

0.0.5
-----
- Add all p5's missing global variables

0.0.4.1
-------
- Support event functions such as `keyPressed`

0.0.4
-----
- Support p5.js pop function
- Add `monitor` command to the CLI
- Allow to run `pyp5js` commands specifying a directory
- First try on organizing the docs

0.0.3
-----
- Add WEBGL variables

0.0.2
-----
- Support more of P5's variable


0.0.1
-----
- First release
