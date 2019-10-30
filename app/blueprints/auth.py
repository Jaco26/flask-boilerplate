from flask import Blueprint, jsonify
from passlib.hash import pbkdf2_sha256
from app.util.validate import should_look_like
from app.database.models import RegisteredUser

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
  body = should_look_like({
    'username': str,
    'password': str,
  })

  if not RegisteredUser.query.get(body['username']):

    pw_hash = pbkdf2_sha256.hash(body['password'])

    new_user = RegisteredUser(username=body['username'], password=pw_hash)
    



@auth_bp.route('/login', methods=['POST'])
def login():
  body = should_look_like({
    'username': str,
    'password': str,
  })
  print(body['username'], body['password'])
  return jsonify('yes!')
