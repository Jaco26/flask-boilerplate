from flask_sqlalchemy import SQLAlchemy, Model
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declared_attr

class DictModel(Model):
  def cols_dict(self):
    return { c.name: getattr(self, c.name) for c in self.__table__.columns }


db = SQLAlchemy(model_class=DictModel)


def init_app(app):
  db.init_app(app)
  Migrate(app, db)

