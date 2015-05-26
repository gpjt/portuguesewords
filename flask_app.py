import json
from flask import Flask, render_template, Response

app = Flask(__name__)


with open("/home/portuguesewords/mysite/words.txt", "r") as f:
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