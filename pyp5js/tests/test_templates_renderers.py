from pyp5js import templates_renderers as renderers
from pyp5js.fs import SketchFiles


def test_get_sketch_index_content():
    sketch_files = SketchFiles('dir', 'foo')

    expected_template = renderers.templates.get_template(sketch_files.from_lib.index_html.name)
    expected_content = expected_template.render({
        'sketch_name': sketch_files.sketch_name,
        "p5_js_url": sketch_files.STATIC_NAME + "/p5.js",
        "sketch_js_url": sketch_files.TARGET_NAME + "/target_sketch.js",
    })

    assert expected_content == renderers.get_sketch_index_content(sketch_files)


def test_get_target_sketch_content():
    sketch_files = SketchFiles('dir', 'foo')

    expected_template = renderers.templates.get_template(sketch_files.from_lib.target_sketch_template.name)
    expected_content = expected_template.render({
        'sketch_name': sketch_files.sketch_name,
    })
    content = renderers.get_target_sketch_content(sketch_files)

    assert expected_content == content
    assert "import foo as source_sketch" in content
