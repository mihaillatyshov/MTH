from flask import Flask
from flask_cors import CORS
from api_auth import auth
from api_graph import graph
from datetime import date
import os
import logging


if not os.path.isdir("./log"):
    os.mkdir("./log")
logging.basicConfig(filename=f'./log/{date.today()}.log', level=logging.DEBUG)


app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(graph)
CORS(app)


if __name__ == "__main__":
    app.run(port = 3444, debug = True)

