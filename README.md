# flask-workshop
A starter project for a Project Phoenix Flask workshop.

## Installation

If you have Flask installed, skip to the next section unless you don't know
about `pipenv`.

Before using Flask, we need to get some things set up like downloading Flask. If
you have used `pip` before but have not tried out `pipenv`, I encourage you to
try it out. `pipenv` creates a Pipfile that lists out dependencies automatically
as you create them, so you don't have to worry about creating a `requirements.txt`
file. So install `pipenv` ironically with `pip`.

```
python3 -m pip install --user pipenv
```

Now, use `pipenv` like how you use `pip`.

```
pipenv install Flask
```

A `Pipfile` and a `Pipfile.lock` will be created that outlines the dependencies
for what you just installed including the correct version of Python.

Now, just activate the environment.

```
pipenv shell
``` 

or you can just run each
command you want to run with `pipenv run`.

[More about `pipenv`](https://docs.python-guide.org/dev/virtualenvs/)

## Hello, World!

The best thing about Flask is that it is SUPER easy to get started, so straight
from the Flask documentation, here is the Hello, World! application in Flask.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

Put this code in a file named `app.py` and run `flask run` in the directory that
the `app.py` file is. Now, you can see your application on your local host.
[See your application](http://127.0.0.1:5000/)!

