from flask import Blueprint, Flask, abort, jsonify, make_response, request, abort
from flask import current_app
from datetime import date, datetime, timedelta
from functools import wraps
import os
import jwt
import logging

from db import *
from GraphParser import *
from suggestion import *

session = Session()
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

graph = Blueprint("graph", __name__)
"""
api graph
"""
@graph.route("/api/v1/graph/suggestion", methods=["POST", "GET"])
def get_recommedation():
    try:
        data_received = request.get_json()["search"]
        data = "some text"
        responce = suggestion(data_received)
        return jsonify({"result": responce}) 
    except Exception as e:
        current_app.logger.warning(f"Exeption {e} ocured")
        # abort(Response(e, 500))
