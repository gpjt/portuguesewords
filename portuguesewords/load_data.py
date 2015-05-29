from portuguesewords import db
from portuguesewords.data import words
from portuguesewords.models import Word

print("Deleting old data")
Word.query.delete()

for word in words:
    print("Adding {}".format(word["word"]))
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