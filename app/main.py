from flask import Flask, render_template
from .database import db
from .blueprints import auth_bp
from .util import ExtendedJSONEncoder, ErrorHandler, jwt

def create_app(config=None):
  app = Flask(__name__)
  app.json_encoder = ExtendedJSONEncoder

  if config:
    app.config.from_object(config)
    if config.ENABLE_CORS:
      from flask_cors import CORS
      CORS(app)

  error_handler = ErrorHandler()

  db.init_app(app)
  jwt.init_app(app)
  error_handler.init_app(app)

  app.register_blueprint(auth_bp, url_prefix='/api/auth')

  @app.route('/')
  def index():
    return render_template('index.html')
  
  return app