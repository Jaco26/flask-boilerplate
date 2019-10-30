from uuid import uuid4
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy, Model
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
import sqlalchemy as sa

  
class BaseModel(Model):
  id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
  date_created = sa.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  date_updated = sa.Column(TIMESTAMP(timezone=True), onupdate=datetime.utcnow)

  def cols_dict(self):
    return { c.name: getattr(self, c.name) for c in self.__table__.columns }


db = SQLAlchemy(model_class=BaseModel)


def init_app(app):
  db.init_app(app)
  Migrate(app, db)

