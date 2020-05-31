from config import db

class Note(db.Model):
  __tablename__ = 'note'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  title = db.Column(db.String(200))
  content = db.Column(db.Text)
  date = db.Column(db.DateTime)