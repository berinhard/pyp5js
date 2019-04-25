P5 = None

def createCanvas(*args):
    P5.createCanvas(*args)


def noStroke(*args):
    P5.noStroke(*args)


def fill(*args):
    P5.fill(*args)


def background(*args):
    P5.background(*args)


def cos(*args):
    return P5.cos(*args)


def sin(*args):
    return P5.sin(*args)


def map(*args):
    return P5.map(*args)


def ellipse(*args):
    P5.ellipse(*args)


def frameRate(*args):
    return P5.frameRate(*args)



def global_p5_injection(p5_sketch):
    """
    Injects the p5js's skecth instance as a global variable to setup and draw functions
    """

    def decorator(f):

        def wrapper():
            global P5
            P5 = p5_sketch
            return f()
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
