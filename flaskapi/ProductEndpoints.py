from flask_restful import Resource
from flask import request, jsonify
from extensions import db
from model import Product, products_schema, product_schema


class add_product(Resource):

    def post(self):
        self.name = request.json['name']
        self.description = request.json['description']
        self.price = request.json['price']
        self.qty = request.json['qty']
        self.new_product = Product(self.name, self.description, self.price, self.qty)
        db.session.add(self.new_product)
        db.session.commit()
        return product_schema.jsonify(self.new_product)


class get_all_products(Resource):

    def get(self):
        self.all_products = Product.query.all()
        result = products_schema.dump(self.all_products)
        return jsonify(result)


class get_product(Resource):

    def get(self, id):
        product = Product.query.get(id)
        result = product_schema.dump(product)
        return jsonify(result)


class update_product(Resource):

    def put(self, id):
        update_product = Product.query.get(id)
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        update_product.name = name
        update_product.description = description
        update_product.price = price
        update_product.qty = qty

        db.session.commit()

        return product_schema.jsonify(update_product)


class delete_product(Resource):

    def delete(self, id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"deleted": "product"})


class home(Resource):
    def get(self):
        return jsonify({"HI": "Welcome"})


# api.add_resource(add_product, '/product')
# api.add_resource(get_all_products, '/products')
# api.add_resource(get_product, '/product/<id>')
# api.add_resource(update_product, '/product/<id>')
# api.add_resource(delete_product, '/product/<id>')
