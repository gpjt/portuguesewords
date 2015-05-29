import os

from portuguesewords import db
from portuguesewords.models import Word

print("Loading data from file")

with open(os.path.join(os.path.dirname(__file__), "words.txt"), "r") as f:
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
        "english": "",
        "count": freq
    })

print("Loaded data")


print("Deleting old data from DB")
Word.query.delete()
print("Deleted")

print("Inserting data into DB")
for word in words:
    print("Inserting {}".format(word["word"]))
    word_model = Word(
        word=word["word"],
        english=word["english"],
        count=word["count"]
    )
    db.session.add(word_model)

print("Committing")
db.session.commit()

print("{} words added.".format(Word.query.count()))

print("Done")