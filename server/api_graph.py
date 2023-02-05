from flask import Blueprint, Flask, abort, jsonify, make_response, request, abort, current_app, request
from flask_cors import CORS
from datetime import date, datetime, timedelta
from functools import wraps
import os
import jwt

from security import *
from db import *
from GraphParser import *
from suggestion import *

session = Session()

graph = Blueprint("graph", __name__, url_prefix="/api/v1/graph")
CORS(graph)
"""
api graph
"""
@graph.route("/suggestion", methods=["POST", "GET"])
def get_recommedation():
    try:
        if not request.json:
            abort(400)
        data_received = request.json["search"]
        print(data_received)
        responce = suggestion(data_received)
        return {"result": responce} 
    except Exception as e:
        current_app.logger.warning(f"Exeption {e} ocured")
        # abort(Response(e, 500))


@graph.route("/get_node/<int:id>", methods=["GET"])
def get_node(id):
    return {"node" : {"id" : id, "name" : GP.GetNodes()[id]}}


@graph.route("/get_nodes/<string:sids>", methods=["GET"])
def get_nodes(sids):
	ids = sids.split(",")
	Nodes = []
	for id in ids:
		if id == '':
			continue
		Nodes.append({"id" : int(id), "name" : GP.GetNodes()[int(id)]})

	return {"nodes" : Nodes}


@graph.route("/get_nodes_count", methods=["GET"])
def get_nodes_count():
    return {"nodesCount" : len(GP.GetNodes())}


@graph.route("/get_prev_next/<int:id>", methods=["GET"])
def get_comments(id):
	Prev = []
	Next = []
	edges = GP.GetPrevNext(id)
	for pedge in edges["Prev"]:
		Prev.append({"id" : pedge["id"], "name" : GP.GetNodes()[int(pedge["id"])], "desc" : pedge["desc"]})
	for nedge in edges["Next"]:
		Next.append({"id" : nedge["id"], "name" : GP.GetNodes()[int(nedge["id"])], "desc" : nedge["desc"]})

	return {"nodes" : {"Prev" : Prev, "Now" : {"id" : id, "name" : GP.GetNodes()[int(edges["Now"])]}, "Next" : Next}}
	