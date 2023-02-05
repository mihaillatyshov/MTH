from functools import wraps
from flask import request, jsonify
import jwt
from db import *
from utils import *

SECRET_KEY = get_app_data()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        head = request.headers
        token = head["Authorization"]
        if not token:
            return jsonify({"message":"token is missing"}), 403
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = session.query(User).filter(User.username == data["username"]).first()
        except:
            return jsonify({"message":"token is invalid"}), 402
        return f(current_user, *args, **kwargs)

    return decorated
