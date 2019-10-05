from pyp5js.pre_compile.update_pytop5js import get_target_sketch_template_content, get_pytop5js_content


def test_get_pytop5js_content():
    vars = ['var_1', 'var_2']
    methods = ['method_1', 'method_2']
    events = ['event_1', 'event_2']

    content = get_pytop5js_content(vars, methods, events)

    assert 'def start_p5(setup_func, draw_func, event_functions):' in content
    for var in vars:
        assert f'{var} = None' in content
        assert f'{var} = p5_instance.{var}' in content

    for method in methods:
        assert f'def {method}(*args):\n    return _P5_INSTANCE.{method}(*args)' in content

    events_list = '"' + '", "'.join(events) + '", '
    assert f'event_function_names = [{events_list}]' in content


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

    assert expected.strip() == get_target_sketch_template_content(events)
