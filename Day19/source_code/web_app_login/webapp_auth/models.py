
from . import db
from flask_login import UserMixin

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    addresses = db.relationship('Address', back_populates='client')

    def __repr__(self):
        return f'<Client(first_name={self.first_name}, last_name={self.last_name})>'
    

class Address(db.Model):
    __tablename__ = 'adresses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('Client', back_populates='addresses')

    def __repr__(self):
        return f'<Address(name={self.name}, address={self.address}, client_id={self.client_id})>'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(64))
