from flask import Flask
from app.util import ApiResponse

class ApiFlask(Flask):
  def make_response(self, rv):
    if isinstance(rv, ApiResponse):
      return rv.to_flask_response()
    return Flask.make_response(self, rv)