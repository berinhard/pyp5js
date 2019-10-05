FROM        python:3.7.4-alpine
MAINTAINER  Álvaro Justen <https://github.com/turicas>

# Configure sharing files/port
VOLUME /sketches
EXPOSE 8000

# Install system dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3 bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Install pyp5js and its dependencies (develop branch)
RUN pip install --no-cache-dir https://github.com/berinhard/pyp5js/archive/develop.zip

# The default command is to run the HTTP server
CMD ["pyp5js", "serve", "--host=0.0.0.0", "--port=8000", "/sketches"]
