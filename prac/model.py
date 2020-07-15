##############
# Here We create Database (sqlite) and define our Schema
#############


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)

# ma = Marshmallow(app)


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    history = db.relationship('Example', backref= 'history', lazy=True)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# class Example(db.Model):
#



# class ProductSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'name', 'description', 'price', 'qty')
#
# product_schema = ProductSchema()
# products_schema = ProductSchema(many=True)