from flask_login import UserMixin, LoginManager
from config import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))
  authenticated = db.Column(db.Boolean, default=False)

  def authenticate(self):
    self.authenticated = True
    return

  def is_active(self):
    """True, as all users are active."""
    return True

  def get_id(self):
    """Return the email address to satisfy Flask-Login's requirements."""
    return self.email

  def is_authenticated(self):
    """Return True if the user is authenticated."""
    return True

  def is_anonymous(self):
    """False, as anonymous users aren't supported."""
    return False

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)