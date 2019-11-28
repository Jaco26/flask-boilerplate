from flask import Response, json

class ApiResponse:
  def __init__(self):
    self.data = None
    self.message = ''
    self.status = 200

  def to_flask_response(self):
    return Response(
      json.dumps({
        'data': self.data,
        'message': self.message
      }),
      status=self.status,
      mimetype='application/json'
    )