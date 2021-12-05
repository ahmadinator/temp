from flask import Flask, escape
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import sqlite3
import json
import os

app = Flask(__name__)
CORS(app)
api = Api(app)

class getProducts(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('max', type=int, help='Max products to fetch')
        args = parser.parse_args()
        with open(os.getcwd() + '\\api\\db\\products.json') as json_file:
            products = json.load(json_file)
            if not args['max'] is None:
                items = []
                for i in range(args['max']):
                    iS = str(i)
                    if iS in products:
                        items.append(products[iS])
                return items
            else:
                return products

api.add_resource(getProducts, '/api/getproducts')

if __name__ == '__main__':
    app.run(debug=True, port=4000)