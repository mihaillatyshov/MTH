from flask import Blueprint, Flask, abort, jsonify, make_response, request, abort, current_app
from flask_cors import CORS
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
CORS(graph)
"""
api graph
"""
@graph.route("/test", methods=["POST", "GET"])
def index():
    print(request.get_json()["search"])
    return "success"

@graph.route("/api/v1/graph/suggestion", methods=["POST", "GET"])
def get_recommedation():
    try:
        data_received = request.get_json()["search"]
        print(data_received)
        responce = suggestion(data_received)
        return jsonify({"result": responce}) 
    except Exception as e:
        current_app.logger.warning(f"Exeption {e} ocured")
        # abort(Response(e, 500))


@graph.route("/get_node/<int:id>", methods=["GET"])
def get_node(id):
    return jsonify({"node" : {"id" : id, "name" : GP.GetNodes()[id]}})


@graph.route("/get_nodes/<string:sids>", methods=["GET"])
def get_nodes(sids):
	ids = sids.split(",")
	Nodes = []
	for id in ids:
		if id == '':
			continue
		Nodes.append({"id" : int(id), "name" : GP.GetNodes()[int(id)]})

	return jsonify({"nodes" : Nodes})


@graph.route("/get_nodes_count", methods=["GET"])
def get_nodes_count():
    return jsonify({"nodesCount" : len(GP.GetNodes())})


@graph.route("/api/v1/graph/get_prev_next/<int:id>", methods=["GET"])
def get_comments(id):
	Prev = []
	Next = []
	edges = GP.GetPrevNext(id)
	for pedge in edges["Prev"]:
		Prev.append({"id" : pedge["id"], "name" : GP.GetNodes()[int(pedge["id"])], "desc" : pedge["desc"]})
	for nedge in edges["Next"]:
		Next.append({"id" : nedge["id"], "name" : GP.GetNodes()[int(nedge["id"])], "desc" : nedge["desc"]})

	return jsonify({"nodes" : {"Prev" : Prev, "Now" : {"id" : id, "name" : GP.GetNodes()[int(edges["Now"])]}, "Next" : Next}})
	