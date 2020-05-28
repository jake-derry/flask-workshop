# Functions that connect the model and view using a form (which connects to the
# model) and a template (which connects the model to the view). These controllers
# are added to the route in the `routes.py` file.

from flask.templating import render_template
from flask_login import current_user, login_user
from auth.forms import LoginForm
from auth.forms import RegistrationForm
from flask.helpers import flash, url_for
from flask import redirect
from auth.model import User
from app import db

def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      print('Login failed')
      return redirect(url_for('auth.login'))
    user.authenticate()
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('home'))
  return render_template('login.html', form=form)

def signup():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(name=form.name.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('home'))
  return render_template('signup.html', title='Register', form=form)

def logout():
  return 'logout'
