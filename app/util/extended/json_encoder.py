from datetime import tzinfo, date, timedelta
from flask.json import JSONEncoder
from uuid import UUID
from app.database.db import db


class SimpleUTC(tzinfo):
  def tzname(self, **kwargs):
    return 'UTC'

  def utcoffset(self, dt):
    return timedelta(0)


class ApiJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.replace(tzinfo=SimpleUTC()).isoformat()
    elif isinstance(obj, timedelta):
      return str(obj)
    elif isinstance(obj, UUID):
      return str(obj)
    elif isinstance(obj, db.Model):
      return obj.cols_dict()
    return json.JSONEncoder.default(obj)