import os
from flask import Flask, request
from messages import make_response
import config

def my_mul(*args):
    if args:
        return args[0] * my_mul(* args[1:])
    return 1

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    payload = {
                "message": "welcome to the multiplication microservice",
                "status": "success"
            }
    return make_response(payload, 200)


@app.route("/mul", methods=["POST"])
def mul():
    list = request.get_json()['list']
    result = my_mul(*list)
    payload = {
               "result": result
            }
    return make_response(payload, 200)



if __name__ == "__main__":
    app.run(debug=config.DEBUG_MODE, host="0.0.0.0", port=config.MUL_PORT)