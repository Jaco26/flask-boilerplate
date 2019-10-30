from app.database.db import db

class RegisteredUser(db.Model):
  username = db.Column(db.String, primary_key=True)
  password = db.Column(db.String, nullable=False)
