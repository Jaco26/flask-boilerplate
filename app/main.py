from flask import Flask
from .database.db import db
from .util import ExtendedJSONEncoder, ErrorHandler, jwt

def create_app(config=None):
  app = Flask(__name__)
  app.json_encoder = ExtendedJSONEncoder

  if config:
    app.config.from_object(config)

  error_handler = ErrorHandler()

  db.init_app(app)
  jwt.init_app(app)
  error_handler.init_app(app)

  @app.route('/')
  def index():
    return '<h1>Welcome to the boilerplate!</h1>'
  
  return app