from flask import Flask
from flask_cors import CORS
from api_auth import auth
from api_graph import graph


app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(graph)
CORS(app)


if __name__ == "__main__":
    app.run(port = 3444, debug = True)


# from flask import Flask, jsonify, make_response, request, abort
# from GraphParser import GraphParser
# from flask_login import LoginManager, login_user, login_required, current_user, login_fresh
# from flask_login.utils import logout_user
# from werkzeug.security import check_password_hash, generate_password_hash
# import datetime
# from RedisLogin import RedisLogin

# from authentication import User

# RL = RedisLogin()
# GP = GraphParser("./res/Polytech_total.xgml")

# app = Flask(__name__)
# app.secret_key = "my super duper puper secret key!"


# login_manager = LoginManager(app)
# @login_manager.user_loader
# def load_user(user_id):
# 	return User().FromDB(user_id, RL)
	

# @app.route("/get_node/<int:id>", methods=["GET"])
# def get_node(id):
#     return jsonify({"node" : {"id" : id, "name" : GP.GetNodes()[id]}})


# @app.route("/get_nodes/<string:sids>", methods=["GET"])
# def get_nodes(sids):
# 	ids = sids.split(",")
# 	Nodes = []
# 	for id in ids:
# 		if id == '':
# 			continue
# 		Nodes.append({"id" : int(id), "name" : GP.GetNodes()[int(id)]})

# 	return jsonify({"nodes" : Nodes})


# @app.route("/get_nodes_count", methods=["GET"])
# def get_nodes_count():
#     return jsonify({"nodesCount" : len(GP.GetNodes())})


# @app.route("/get_prev_next/<int:id>", methods=["GET"])
# def get_comments(id):
# 	Prev = []
# 	Next = []
# 	edges = GP.GetPrevNext(id)
# 	for pedge in edges["Prev"]:
# 		Prev.append({"id" : pedge["id"], "name" : GP.GetNodes()[int(pedge["id"])], "desc" : pedge["desc"]})
# 	for nedge in edges["Next"]:
# 		Next.append({"id" : nedge["id"], "name" : GP.GetNodes()[int(nedge["id"])], "desc" : nedge["desc"]})

# 	return jsonify({"nodes" : {"Prev" : Prev, "Now" : {"id" : id, "name" : GP.GetNodes()[int(edges["Now"])]}, "Next" : Next}})
	

# @app.route("/login", methods=["POST"])
# def login():
# 	if not request.json:
# 		abort(400)
	
# 	email 		= request.json.get("email")
# 	password	= request.json.get("password")
	
# 	if email and password:
# 		user = User().FromDB(email, RL)
# 		if user.IsExists():
# 			if check_password_hash(user.GetPassword(), password):
# 				cookieDuration = datetime.timedelta(seconds = 10)
# 				login_user(user, remember=True, duration=cookieDuration)
# 				return jsonify({ "isAuth" : True })

# 	return make_response(jsonify({ "message" : "Wrong email or password!" }), 422)


# @app.route("/islogin", methods=["GET"])
# def islogin():
# 	return jsonify({ "isAuth" : current_user.get_id() != None })


# @app.route("/profileinfo", methods=["GET"])
# def porfileInfo():
# 	curr_id = current_user.get_id()
# 	if curr_id != None:
# 		user = User().FromDB(curr_id, RL)
# 		if user.IsExists():
# 			return jsonify({ 
# 				"isAuth" : True, 
# 				"email" : user.GetEmail(), 
# 				"nickname" : user.GetNickname(), 
# 				"name" : user.GetName(), 
# 				"registration_date" : user.GetRegDate(),
# 				"confirmed" : user.GetConfirmed()  
# 			})

# 	return jsonify({ "isAuth" : False })


# @app.route("/logout", methods=["POST"])
# @login_required
# def logout():
# 	logout_user()
# 	return jsonify({ "res" : "User Logout!" })


# @app.route("/register", methods=["POST"])
# def register():
# 	if not request.json:
# 		abort(400)

# 	email = 	request.json.get("email")
# 	password1 = request.json.get("password1")
# 	password2 = request.json.get("password2")
# 	nickname = 	request.json.get("nickname", "")
# 	name = 		request.json.get("name", "")

# 	if not (email or password1 or password2):
# 		print("test1")
# 		return (make_response(jsonify({ "message" : "Please, fill all fields" }), 422))
# 	elif password1 != password2:
# 		print("test2")
# 		return (make_response(jsonify({ "message" : "Passwords are not equal" }), 422))
# 	else:
# 		hashPwd = generate_password_hash(password1)
# 		print(str(datetime.datetime.now().date()))
# 		RL.AddUser(email, {
# 			"password"			: hashPwd,
# 			"nickname"			: nickname,
# 			"name"				: name, 
# 			"registration_date" : str(datetime.datetime.now().date()),
# 			"confirmed" 		: 0 
# 		})

# 	return make_response(jsonify({ "message" : "User Registered!" }), 201)


# if __name__ == "__main__":
#     app.run(port = 3444, debug = True)