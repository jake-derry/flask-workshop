from notes.controllers import *

routes = [
  {
    'name' : 'add',
    'view_func' : add_note,
    'methods' : ['GET', 'POST']
  },
  {
    'name' : 'all',
    'view_func' : display_all_notes,
    'methods' : ['GET']
  },
  {
    'name' : '<int:note_id>',
    'view_func' : delete_note,
    'methods' : ['POST']
  }
]