from pyp5js.templates_renderer import get_target_sketch_template_content


def test_get_target_sketch_template_content():
    events = ['keyPressed', 'mouseDragged']

    expected = """
import {{ sketch_name }} as source_sketch
from pytop5js import *

event_functions = {
    "keyPressed": source_sketch.keyPressed,
    "mouseDragged": source_sketch.mouseDragged,
}

start_p5(source_sketch.setup, source_sketch.draw, event_functions)
"""

    assert expected.strip() == get_target_sketch_template_content(events)
