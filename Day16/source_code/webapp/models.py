from . import db


class Client(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(64))
    password = db.Column(db.String(64))
