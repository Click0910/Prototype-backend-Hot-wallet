from utils.db import db
from sqlalchemy.orm import relationship


class PKey(db.Model):
    __tablename__ = "priv_key"
    id = db.Column(db.Integer, primary_key=True)
    p_key = db.Column(db.String(500))
    address = relationship("Address", backref="priv_key")

    def __init__(self, p_key):
        self.p_key = p_key


class Address(db.Model):

    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    crypto_type = db.Column(db.String(5))
    address = db.Column(db.String(100))
    address_id = db.Column(db.Integer, db.ForeignKey("priv_key.id"))

    def __init__(self, crypto_type, address, address_id):
        self.crypto_type = crypto_type
        self.address = address
        self.address_id = address_id


