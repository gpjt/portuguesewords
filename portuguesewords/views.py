from flask import render_template, Response
import json

from portuguesewords import app


with open("/home/portuguesewords/mysite/portuguesewords/words.txt", "r") as f:
    words_str = f.read()

words = []
for id, word_line in enumerate(words_str.split("\n")):
    if word_line == "":
        continue
    freq_str, word = word_line.split("\t")
    freq = int(freq_str)
    words.append({
        "id": id,
        "word": word,
        "details": "Count in corpus: {}".format(freq)
    })



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/words/")
def words_collection():
    return Response(json.dumps(words),  mimetype='application/json')
