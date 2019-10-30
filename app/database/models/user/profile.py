from app.database.db import db

class UserProfile(db.Model):

  username = db.relationship('RegisteredUser', lazy='joined')
  