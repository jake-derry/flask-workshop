from notes.forms import *
from notes.model import Note
from datetime import datetime
from app import db
from flask.helpers import url_for
from flask import redirect
from flask.templating import render_template
from flask_login import login_required, current_user

@login_required
def display_all_notes():
  notes = Note.query.filter_by(user_id=current_user.id)
  return render_template('all_notes.html', notes=notes)

@login_required
def add_note():
  form = AddNoteForm()
  if form.validate_on_submit():
    note = Note(title=form.title.data, content=form.content.data, 
                date=datetime.today(), user_id=current_user.id)
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('notes.display_all_notes'))
  return render_template('note.html', form=form)