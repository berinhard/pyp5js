import subprocess
import shutil
import shlex
from cprint import cprint
from unipath import Path


PYP5_DIR = Path(__file__).parent


def compile_sketch_js(sketch, target_name):
    sketch_dir = sketch.parent

    command = ' '.join([str(c) for c in [
        'transcrypt', '-xp', PYP5_DIR, '-b', '-m', '-n', sketch
    ]])

    cprint.info(f"Converting Python to P5.js...\nRunning command:\n\t {command}")

    proc = subprocess.Popen(shlex.split(command))
    proc.wait()

    __target = sketch_dir.child('__target__')
    if not __target.exists():
        cprint.err(f"Error with transcrypt: the {__target} directory wasn't created.", interrupt=True)

    target_dir = sketch_dir.child(target_name)
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.move(__target, target_dir)
