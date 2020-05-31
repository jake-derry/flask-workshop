from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea

class AddNoteForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', widget=TextArea())
  submit = SubmitField('Register')