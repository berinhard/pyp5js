_P5_INSTANCE = None

def createCanvas(*args):
    return _P5_INSTANCE.createCanvas(*args)


def noStroke(*args):
    return _P5_INSTANCE.noStroke(*args)


def fill(*args):
    return _P5_INSTANCE.fill(*args)


def background(*args):
    return _P5_INSTANCE.background(*args)


def cos(*args):
    return _P5_INSTANCE.cos(*args)


def sin(*args):
    return _P5_INSTANCE.sin(*args)


def map(*args):
    return _P5_INSTANCE.map(*args)


def ellipse(*args):
    return _P5_INSTANCE.ellipse(*args)


def frameRate(*args):
    return _P5_INSTANCE.frameRate(*args)


width = None
height = None
PI = None
mouseX = None
mouseY = None
def pre_draw(p5_instance, draw_func):
    """
    We need to run this before the actual draw to insert and update p5 env variables
    """
    global width, height, PI, mouseX, mouseY

    width = p5_instance.width
    height = p5_instance.height
    PI = p5_instance.PI
    mouseX = p5_instance.mouseX
    mouseY = p5_instance.mouseY

    return draw_func()




def global_p5_injection(p5_sketch):
    """
    Injects the p5js's skecth instance as a global variable to setup and draw functions
    """

    def decorator(f):

        def wrapper():
            global _P5_INSTANCE
            _P5_INSTANCE = p5_sketch
            return pre_draw(_P5_INSTANCE, f)
        return wrapper

    return decorator


def start_p5(setup_func, draw_func):
    """
    This is the entrypoint function. It accepts 2 parameters:

    - setup_func: a Python setup callable
    - draw_func: a Python draw callable

    This method gets the p5js's sketch instance and injects them
    """

    def sketch_setup(p5_sketch):
        p5_sketch.setup = global_p5_injection(p5_sketch)(setup_func)
        p5_sketch.draw = global_p5_injection(p5_sketch)(draw_func)

    return __new__ (p5(sketch_setup, 'sketch-holder'))
