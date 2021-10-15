from flask import Flask, jsonify, make_response, request, abort
from parser import GraphParser

GP = GraphParser("./res/Polytech_total.xgml")
print(GP.GetNodes()[0])
print(GP.GetEdges()[0])
print(GP.GetPrevNext(42))

app = Flask(__name__)

@app.route("/get_node/<int:id>", methods=["GET"])
def get_node(id):
    return jsonify({"node" : {"id" : id, "name" : GP.GetNodes()[id]}})

@app.route("/get_nodes/<string:sids>", methods=["GET"])
def get_nodes(sids):
	ids = sids.split(",")
	Nodes = []
	for id in ids:
		if id == '':
			continue
		Nodes.append({"id" : int(id), "name" : GP.GetNodes()[int(id)]})

	return jsonify({"nodes" : Nodes})


@app.route("/get_nodes_count", methods=["GET"])
def get_nodes_count():
    return jsonify({"nodesCount" : len(GP.GetNodes())})

@app.route("/get_prev_next/<int:id>", methods=["GET"])
def get_comments(id):
	Prev = []
	Next = []
	edges = GP.GetPrevNext(id)
	for pedge in edges["Prev"]:
		Prev.append({"id" : pedge["id"], "name" : GP.GetNodes()[int(pedge["id"])], "desc" : pedge["desc"]})
	for nedge in edges["Next"]:
		Next.append({"id" : nedge["id"], "name" : GP.GetNodes()[int(nedge["id"])], "desc" : nedge["desc"]})

	return jsonify({"nodes" : {"Prev" : Prev, "Now" : {"id" : id, "name" : GP.GetNodes()[int(edges["Now"])]}, "Next" : Next}})
	

if __name__ == "__main__":
    app.run(port = 3444, debug = True)