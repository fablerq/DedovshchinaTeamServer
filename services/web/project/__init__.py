import os

from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    Response,
)

app = Flask(__name__)
CORS(app)
app.config.from_object("project.config.Config")

server_host = "http://213.219.213.136"

@app.route("/calc")
def calc():
    line = request.args.get('data', None)
    if line is None:
        return jsonify(message="Could not get file field from request"), 400
    result_line = line[::-1]
    return jsonify(line=result_line), 200

@app.route("/files/<filename>")
def get_file(filename):
    return send_from_directory(app.config["FILES_FOLDER"], filename)

@app.route("/calc/csv", methods=["POST"])
def upload_file():
    if request.files.get('file', None) is None:
        return jsonify(message="Could not get file field from request"), 400

    file = request.files["file"]

    if file.filename == '':
        return jsonify(message="Could not get file name from request"), 400

    filename = secure_filename(file.filename)

    with open(f"{app.config['FILES_FOLDER']}/{filename}", "bw") as f:
        chunk_size = 4096
        while True:
            chunk = file.stream.read(chunk_size)
            if len(chunk) == 0:
                return jsonify(url=f"{server_host}/files/{filename}"), 200
            f.write(chunk)