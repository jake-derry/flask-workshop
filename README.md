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
from the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/), here is the Hello, World! application in Flask.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
```

Put this code in a file named `app.py` and run `flask run` in the directory that
the `app.py` file is. Now, you can see your application on your local host.
[See your application](http://127.0.0.1:5000/hello)!

### How does this work?

First, you created the web application. Then, you created a function that
returns 'Hello, World!'. You gave that function the '/hello' route, so when
you go to 'http://127.0.0.1:5000/hello', the application runs the `hello_world`
function. Boom! You see 'Hello, World!'

## The Flask architecture

Now that we have Flask working, with only 5 lines of code, it's time to create
something that's actually interesting.

Flask is a web framework that doesn't have many hard requirements. For example,
you can organize your file system however you'd like, but here is a file
structure that encourages modularity.

The file system looks something like this:

```
app.py                # links the application together
config.py             # stores application configurations
manage.py             # manages the application using Flask-Manager
app/                  # a package for a specific app within your larger app
├ __init__.py         # initializes the app package
├ controller.py       # stores the controllers of the application 
├ model.py            # models the application
├ forms.py            # stores application forms using Flask-WTF
├ static/             # a folder for static files (CSS, JS, HTML)
└ templates/          # a folder for dynamic Jinja HTML templates
```

Why this file structure:

1. Scalable to multiple sub-applications in your web application. For example,
if you are building a job site, you will want a sub-application for searching
employers and another for job applicants.

2. Uses the [MVC design pattern](https://www.geeksforgeeks.org/mvc-design-pattern/).
The MVC design pattern breaks an application into a model, view, and controller.
The Model stores the information about the application and performs business
logic. The View determines how the Model will be displayed. The Controller
connects the model and view to initate changes to the model and display of the
view. In this file structure, each of these parts are stored in separate files.
In fact, Jinja templates also function as part of the view that separates the
data from how it is displayed.

3. Allows management and configuration. The `config.py` file stores possible
configurations that can be used. The `manage.py` file allows easy database and
application management. For example, some of the management that Python provides
support for includes initializing a database: `python manage.py db init`.

## Building a simple application

To start with Flask, let's create a simple application that will make use of
some interesting Flask extensions like:
- Flask-WTF (forms)
- Flask-Migrate (database migration)
- Flask-Assets (asset management)
- SQLAlchemy (easy database management)
- Flask-Login (login management)
- Flask-Admin (administration)

We are going to build a simple Flask application that stores users notes. Here
are some important features we want to offer:
- User data is consistent even when the web application is restarted
- User's notes are safe with authentication
- Admins can help users if they have trouble with login

Our application will be broken into two sub-applications: authentication (auth)
and the actual notes application (notes).

### Adding user authentication

Before we can expand the notes application, we need to be able to authenticate
users, so each user's notes will be private to them.