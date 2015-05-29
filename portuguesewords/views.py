from flask import render_template, request, Response
import json

from portuguesewords import app, db
from portuguesewords.models import Word


@app.route("/")
def index():
    return render_template("index.html")


def dictify_word(word):
    return {
        "id": word.id,
        "word": word.word,
        "english": word.english,
        "count": word.count
    }


@app.route("/words/", methods=["GET"])
def words_collection():
    words = Word.query.all()
    return Response(
        json.dumps([dictify_word(word) for word in words]),
        mimetype='application/json'
    )


@app.route("/words/<int:word_id>", methods=["POST"])
def words_element(word_id):
    new_data = request.get_json()

    word = Word.query.filter_by(id=word_id).first()
    word.word = new_data["word"]
    word.english = new_data["english"]
    word.count = new_data["count"]
    db.session.commit()

    return Response(
        json.dumps(dictify_word(word)),
        mimetype='application/json'
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
