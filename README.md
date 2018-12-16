### pyp5js

This project is still a proof of concept based in [Axel Tanner's "Transcrypt & p5js" blogpost](https://4nomore.net/2018/transcrypt_p5js/). The idea is to encapsulate his generators' strategy in a Python Command Line interface.

My main goal is to make this idealistc Python code to be able to generate its respective JS code:

```python
def setup():
    createCanvas(200, 200)
    background(160)
    print(foo)


def draw():
    fill('blue')
    background(200)
    r = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, r, r)
```

If you want to test what I've done so far, you can edit the `sketch.py` file to try pyp5js out. To do that, you'll have to run:

1. `$ pip3 install -r requirements.txt`
2. `$ make serve` - this will start a simple HTTP server to serve the JS files created by [Transcrypt](http://www.transcrypt.org/). This can be left runnning in background.
3. `$ make compile` - this will compile your Python code to JS files using [Transcrypt](http://www.transcrypt.org/)

When the code is compiled, you can see the result by accessing `http://localhost:8000/`
