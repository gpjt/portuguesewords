import json
from flask import Flask, render_template, Response

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/words/")
def words_collection():
    data = [
        {
            "id": "1",
            "portuguese": "palavra 1",
            "details": "The details for the first word",
        },
        {
            "id": "2",
            "portuguese": "palavra 2",
            "details": "The details for the second word",
        },
        {
            "id": "3",
            "portuguese": "palavra 3",
            "details": "The details for the third word",
        }
    ]
    return Response(json.dumps(data),  mimetype='application/json')