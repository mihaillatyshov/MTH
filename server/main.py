from flask import Flask, jsonify, make_response, request, abort
from parser import GraphParser

GP = GraphParser("./res/Polytech_total.xgml")
print(GP.GetNodes()[0])
print(GP.GetEdges()[0])
print(GP.GetPrevNext(42))

app = Flask(__name__)

@app.route("/get_node/<int:id>", methods=["GET"])
def get_node(id):
    return jsonify({"node" : {"id" : id, "desc" : GP.GetNodes()[id]}})

@app.route("/get_nodes/<string:sids>", methods=["GET"])
def get_nodes(sids):
	ids = sids.split(",")
	Nodes = []
	for id in ids:
		if id == '':
			continue
		Nodes.append({"id" : int(id), "desc" : GP.GetNodes()[int(id)]})

	return jsonify({"nodes" : Nodes})


@app.route("/get_nodes_count", methods=["GET"])
def get_nodes_count():
    return jsonify({"nodesCount" : len(GP.GetNodes())})

@app.route("/get_prev_next/<int:id>", methods=["GET"])
def get_comments(id):
	Prev = []
	Next = []
	ids = GP.GetPrevNext(id)
	for pid in ids["Prev"]:
		Prev.append({"id" : pid, "desc" : GP.GetNodes()[int(pid)]})
	for nid in ids["Next"]:
		Next.append({"id" : nid, "desc" : GP.GetNodes()[int(nid)]})

	return jsonify({"nodes" : {"Prev" : Prev, "Now" : {"id" : id, "desc" : GP.GetNodes()[int(ids["Now"])]}, "Next" : Next}})
	

if __name__ == "__main__":
    app.run(port = 3444, debug = True)