##############
# Here We create Database (sqlite) and define our Schema
#############
from api import db


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    hist = db.relationship('Example', backref='product', lazy=True)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class Example(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    p_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, name):
        self.name = name


