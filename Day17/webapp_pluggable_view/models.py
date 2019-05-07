from . import db


class Client(db.Model):
    __tablename__ = 'clients'

    idx = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    address = db.relationship('Address', back_populates='client')

    def __repr__(self):
        return f'<Client(first_name={self.first_name}, last_name={self.last_name})>'


class Address(db.Model):
    __tablename__ = 'addresses'

    idx = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(40))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.idx'))
    client = db.relationship('Client', back_populates='address')

    def __repr__(self):
        return f'<Address(address={self.address}, client_id={self.client_id})>'
