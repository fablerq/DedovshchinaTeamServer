import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    Response,
    send_file
)

app = Flask(__name__)
app.config.from_object("project.config.Config")

@app.route("/calc")
def calc():
    return jsonify(hello="world")

@app.route("/calc/csv", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["FILES_FOLDER"], filename))
    return send_from_directory(app.config["FILES_FOLDER"], filename)

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