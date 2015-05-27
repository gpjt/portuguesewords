from flask import render_template, Response
import json

from portuguesewords import app
from portuguesewords.data import words


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/words/", methods=["GET"])
def words_collection():
    return Response(json.dumps(words),  mimetype='application/json')


@app.route("/words/<int:word_id>", methods=["POST"])
def words_element(word_id):
    return Response(json.dumps(words[word_id]),  mimetype='application/json')
