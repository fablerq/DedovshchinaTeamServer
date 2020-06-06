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

@app.route("/calc/<line>", methods=["POST"])
def calc(line):
    result_line = line[::-1]
    return jsonify(line=result_line), 200

@app.route("/files/<filename>")
def get_file(filename):
    return send_from_directory(app.config["FILES_FOLDER"], filename)

@app.route("/calc/csv", methods=["POST"])
def upload_file():
    if request.files.get('file', None) is None:
        return jsonify(message="Could not get file field from request"), 500
    file = request.files["file"]
    if file.filename == '':
        return jsonify(message="Could not get file nme from request"), 500
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["FILES_FOLDER"], filename))
    return jsonify(url=f"{server_host}/files/{filename}"), 200

# json = {
#     "id": 1,
#     "initial": "str",
#     "level": "str",
#     "country": "str",
#     "region": "str",
#     "city": "city",
#     "place": "place",
#     "area_type": "str",
#     "area": "str",
#     "street_type": "str",
#     "house": "str",
#     "building": "str",
#     "flat": "str",
#     "office": "str"
# },

