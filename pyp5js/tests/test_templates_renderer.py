from pyp5js import templates_renderer as renderers
from pyp5js.fs import SketchFiles


def test_get_target_sketch_template_content():
    events = ['keyPressed', 'mouseDragged']

    expected = """
import {{ sketch_name }} as source_sketch
from pyp5js import *

event_functions = {
    "keyPressed": source_sketch.keyPressed,
    "mouseDragged": source_sketch.mouseDragged,
}

start_p5(source_sketch.setup, source_sketch.draw, event_functions)
"""

    assert expected.strip() == renderers.get_target_sketch_template_content(events)


def test_get_pytop5js_content():
    vars = ['var_1', 'var_2']
    methods = ['method_1', 'method_2']
    events = ['event_1', 'event_2']

    content = renderers.get_pytop5js_content(vars, methods, events)

    assert 'def start_p5(setup_func, draw_func, event_functions):' in content
    for var in vars:
        assert f'{var} = None' in content
        assert f'{var} = p5_instance.{var}' in content

    for method in methods:
        assert f'def {method}(*args):\n    return _P5_INSTANCE.{method}(*args)' in content

    events_list = '"' + '", "'.join(events) + '", '
    assert f'event_function_names = [{events_list}]' in content


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
