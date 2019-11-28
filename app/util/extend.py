from flask import Flask, Response, json
from werkzeug.exceptions import default_exceptions, HTTPException
from datetime import date, tzinfo, timedelta
from uuid import UUID
from app.database.db import db


# class ApiResponse:
#   def __init__(self):
#     self.data = None
#     self.message = ''
#     self.status = 200

#   def to_response(self):
#     return Response(
#       json.dumps({
#         'data': self.data,
#         'message': self.message
#       })
#       status=self.status,
#       mimetype='application/json'
#     )



# class SimpleUTC(tzinfo):
#   def tzname(self, **kwargs):
#     return 'UTC'

#   def utcoffset(self, dt):
#     return timedelta(0)



# class CustomJSONEncoder(json.JSONEncoder):
#   def default(self, obj):
#     if isinstance(obj, date):
#       return obj.replace(tzinfo=SimpleUTC()).isoformat()
#     elif isinstance(obj, timedelta):
#       return str(obj)
#     elif isinstance(obj, UUID):
#       return str(obj)
#     elif isinstance(obj, db.Model):
#       return obj.cols_dict()
#     return json.JSONEncoder.default(obj)



# class CustomErrorHandler:
#   def error_to_api_reponse(self, error):
#     res = ApiResponse()
#     if isinstance(error, HTTPException):
#       res.status = error.code
#       res.message = str(error)
#     else:
#       res.status = 500
#       res.message = str(error)
#     return res
  
#   def init_app(self, app):
#     for code in default_exceptions.keys():
#       app.register_error_handler(code, self.error_to_api_reponse)
    


  
# class ApiFlask(Flask):
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)

#     self.json_encoder = CustomJSONEncoder

#     error_handler = CustomErrorHandler()

#     for code in default_exceptions.keys():
#       self.register_error_handler(code, error_handler.error_to_api_reponse)
    
#     db.init_app(self)
    


#   def make_response(self, rv):
#     if isinstance(rv, ApiResponse):
#       return rv.to_response()
#     return Flask.make_response(self, rv)