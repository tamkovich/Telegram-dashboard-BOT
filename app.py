from flask import Flask, request, json

from logic_application.database import push_database
from settings import *
import messageHandler

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route(config['app']['tg']['posturi'], methods=["POST"])
def telegram():
    data = json.loads(request.data)
    if data.get("message"):
        push_database(data["message"])
        messageHandler.create_answer(
            data["message"], config['app']['tg']['token']
        )
        return "ok"
    return "nothing"


app.run(config['app']['host'], config['app']['port'])
