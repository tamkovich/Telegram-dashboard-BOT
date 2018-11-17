from flask import Flask, request, json

from logic_application.database import push_database, update_user_step
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
#        if data["message"]["chat"]["id"] == 661793395:
#            return "nothing"
        step = push_database(data["message"])
        step = messageHandler.create_answer(
            data["message"], config['app']['tg']['token'], step
        )
        update_user_step(
            step=step,
            user_id=str(data["message"]["chat"]["id"])
        )
        return "ok"
    return "nothing"


app.run(config['app']['host'], config['app']['port'])
