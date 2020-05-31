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
from notes import notes

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(notes)

# Connect login_manager
login_manager = setup_login_manager()
login_manager.init_app(app)


@app.route('/home', endpoint='home')
@login_required
def profile():
  return redirect(url_for('notes.display_all_notes'))