def connect_routes(app, routes):
  for route in routes:
    name = route['name']
    view_func = route['view_func']
    methods = route['methods']
    app.add_url_rule(name, view_func=view_func,
                     methods=methods)