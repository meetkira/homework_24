import os

from flask import Flask, request, abort, Response

from utils import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Response:
    try:
        cmd_1 = request.args["cmd1"]
        value_1 = request.args["value1"]
        file_name = request.args["file_name"]
    except KeyError:
        abort(400)

    cmd_2 = request.args.get("cmd2")
    value_2 = request.args.get("value2")

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400)

    with open(file_path) as f:
        result = get_query(f, cmd_1, value_1)
        if cmd_2:
            result = get_query(result, cmd_2, value_2)
        content = '\n'.join(result)

    return app.response_class(content, content_type="text/plain")

if __name__ == '__main__':
    app.run()