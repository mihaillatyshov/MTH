from flask import Blueprint, Flask, jsonify, make_response, request, abort
from flask import current_app
from datetime import date, datetime, timedelta
from functools import wraps
import os
import jwt
import logging

from db import *

SECRET_KEY = "helloworld"
if not os.path.isdir("./log"):
    os.mkdir("./log")
logging.basicConfig(filename=f'./log/{date.today()}.log', level=logging.DEBUG)


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

auth = Blueprint("auth", __name__)


"""
auth api
"""
@auth.route("/api/v1/auth/login", methods=["POST", "GET"])
def login():
    try:
        data = request.get_json(force=True)
        user = session.query(User) \
            .filter(User.username == data["username"]).first()
        if user:
            token = jwt.encode({"username": data["username"], 
            "exp": datetime.utcnow() + timedelta(days = 730)}, 
            SECRET_KEY)
            current_app.logger.info("%s logged in successfully", user.username)
            return jsonify({"token": token})
    except Exception as e:
        current_app.logger.info(f"Error {e} occured")
        abort(500)


@auth.route("/api/v1/auth/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json(force=True)
        session.add(User(data["last_name"], data["first_name"],
        data["username"], data["email"], data["password"], 1))
        session.commit()
        session.close()
        return jsonify(200, "OK")
    except Exception as e:
        return jsonify(500, f"Error occured in {e}")


@auth.route("/api/v1/auth/test", methods=["GET"])
@token_required
def index(current_user):
    try:
        token = request.headers["Authorization"]
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])["username"]
        # print(data)
        return jsonify(200, "OK")
    except Exception as e:
        return jsonify(500, f"Error occured in {e}")

@auth.route("/api/v1/auth/islogin", methods=["GET"])
def is_login():
    return jsonify({ "isAuth" : False })