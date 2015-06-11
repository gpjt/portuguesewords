from portuguesewords import db


class Word(db.Model):

    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(32))
    english = db.Column(db.String(256))
    count = db.Column(db.Integer)
    notes = db.Column(db.String(4096))