Development
-----------

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
