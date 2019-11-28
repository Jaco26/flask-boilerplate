from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions
from app.util.api_response import ApiResponse


class ApiErrorHandler:
  def to_api_response(self, error):
    res = ApiResponse()
    res.status = error.code if isinstance(error, HTTPException) else 500
    res.message = str(error)
    return res

  def init_app(self, app):
    for code in default_exceptions.keys():
      app.register_error_handler(code, self.to_api_response)