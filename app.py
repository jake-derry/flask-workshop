from flask import redirect, url_for
from flask_login import login_required, LoginManager, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import db, config_app

from auth import setup_login_manager

app = config_app()

# Connect Flask-Migrate
migrate = Migrate(app, db)

# Import blueprints
from auth import auth

# Register blueprints
app.register_blueprint(auth)

# Connect login_manager
login_manager = setup_login_manager()
login_manager.init_app(app)


@app.route('/home', endpoint='home')
@login_required
def profile():
  user = current_user
  return 'You found your profile!'