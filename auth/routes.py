from auth.controllers import *

routes = [
  {
    'name' : 'login',
    'view_func' : login,
    'methods' : ['GET', 'POST']
  },
  {
    'name' : 'signup',
    'view_func' : signup,
    'methods' : ['GET', 'POST']
  },
  {
    'name' : 'logout',
    'view_func' : logout,
    'methods' : ['GET', 'POST']
  }
]