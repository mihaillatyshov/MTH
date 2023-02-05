from flask import Blueprint, Flask, jsonify, make_response, request, abort
from flask import current_app
from datetime import date, datetime, timedelta
from functools import wraps
import os
import jwt
import logging
from security import SECRET_KEY, token_required
from db import *

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")
"""
auth api
"""
@auth.route("/login", methods=["POST", "GET"])
def login():
    try:
        if not request.json:
            abort(400)
        data = request.json
        user = session.query(User) \
            .filter(User.username == data["username"]).first()
        if user:
            token = jwt.encode({"username": data["username"], 
            "exp": datetime.utcnow() + timedelta(days = 730)}, 
            SECRET_KEY)
            current_app.logger.info("%s logged in successfully", user.username)
            return {"token": token}
    except Exception as e:
        return {"message": "error"}, 500
        

@auth.route("/register", methods=["POST"])
def register_user():
    try:
        if not request.json:
            abort(400)
        data = request.json
        session.add(User(
            last_name=data["last_name"], 
            first_name=data["first_name"],
            username=data["username"], 
            email=data["email"], 
            password=data["password"]
            ))
        session.commit()
        session.close()
        return {"message": "ok"}
    except Exception as e:
        return {"message": "error"}, 500


@auth.route("/test", methods=["GET"])
@token_required
def index(current_user):
    try:
        token = request.headers["Authorization"]
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])["username"]
        return jsonify(200, "OK")
    except Exception as e:
        return {"message": "error"}, 500


@auth.route("/islogin", methods=["GET"])
def is_login():
    return { "isAuth" : False }