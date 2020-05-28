from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Setup database
db = SQLAlchemy()

def config_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'Hpqd/TyqgtpWT3xE'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  return app