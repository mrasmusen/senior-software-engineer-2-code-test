from flask_restplus import (
    Namespace,
    Resource,
    fields,
    reqparse
)

from app.datastore.datastore import datastore

api = Namespace('products', description='Products')

cheapest_products_parser = reqparse.RequestParser()
cheapest_products_parser.add_argument('number', type=int, help='Number of products to return', required=True)

product = api.model('Product',{
    'id': fields.String,
    'name': fields.String,
    'brand': fields.String,
    'retailer': fields.String,
    'price': fields.Float,
    'in_stock': fields.Boolean
 })

product_list = api.model('ProductList', {
    'products': fields.List(fields.Nested(product))
})

@api.route('/<id>')
class Product(Resource):

    @api.doc('Get single product')
    @api.marshal_with(product)
    def get(self, id):
        product = datastore.get_product_by_id(id)
        return product

@api.route('/cheapest')
class CheapestProducts(Resource):
    
    @api.doc('Get list of cheapest products')
    @api.expect(cheapest_products_parser)
    @api.marshal_with(product_list)
    def get(self):

        number = cheapest_products_parser.parse_args()['number']
        
        products = datastore.get_cheapest_products(number)

        return {'products': products}