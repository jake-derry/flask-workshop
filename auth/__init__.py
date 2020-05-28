from flask import Blueprint, redirect, url_for
from flask_login import LoginManager
from util import connect_routes
from auth.routes import routes
from auth.model import User

auth = Blueprint('auth', __name__, url_prefix='/auth')
connect_routes(auth, routes)

def setup_login_manager():
  login_manager = LoginManager()

  @login_manager.user_loader
  def user_loader(email):
    return User.query.filter_by(email=email).first()

  @login_manager.unauthorized_handler
  def unauthorized_callback():
    return redirect(url_for('auth.login'))

  return login_manager