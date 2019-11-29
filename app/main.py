from flask import Flask, render_template, request, abort
from .database import db
from .blueprints import auth_bp
from .util import ApiErrorHandler, ApiResponse, jwt, extended, commands

def create_app(config=None):
  app = extended.ApiFlask(__name__)
  app.json_encoder = extended.ApiJSONEncoder

  if config:
    app.config.from_object(config)
    if config.ENABLE_CORS:
      from flask_cors import CORS
      CORS(app)

  error_handler = ApiErrorHandler()

  db.init_app(app)
  jwt.init_app(app)
  error_handler.init_app(app)

  app.cli.add_command(commands.seed_db_command)

  @app.after_request
  def after_req(res):
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    res.headers['Server'] = 'My Butt'
    res.headers['X-DNS-Prefetch-Control'] = 'off' # https://helmetjs.github.io/docs/dns-prefetch-control/
    res.headers['X-Frame-Options'] = 'deny' # https://helmetjs.github.io/docs/frameguard/
    res.headers['X-Content-Type-Options'] = 'nosniff' # https://helmetjs.github.io/docs/dont-sniff-mimetype/
    return res

  app.register_blueprint(auth_bp, url_prefix='/api/auth')

  @app.route('/')
  def index():
    return render_template('index.html')

  return app