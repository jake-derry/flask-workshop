from util import connect_routes
from notes.routes import routes
from flask import Blueprint

notes = Blueprint('notes', __name__, url_prefix='/notes')
connect_routes(notes, routes)