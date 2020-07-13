from flask_restful import Api
import __init__ as init
from model import Product, products_schema, product_schema
from ProductEndpoints import add_product,get_all_products,get_product,update_product,delete_product

app = init.init()
api = Api(app)

api.add_resource(add_product, '/product')
api.add_resource(get_all_products, '/products')
api.add_resource(get_product, '/product/<id>')
api.add_resource(update_product, '/product/<id>')
api.add_resource(delete_product, '/product/<id>')


if __name__ == '__main__':
    app.run(debug=True)
