from app.database.db import db

class RegisteredUser(db.Model):
  username = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String, nullable=False)
