from flask import render_template, Response
import json

from portuguesewords import app
from portuguesewords.data import words


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/words/")
def words_collection():
    return Response(json.dumps(words),  mimetype='application/json')
