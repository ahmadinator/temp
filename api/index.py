from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class getProducts(Resource):
    def get(self):
        return "hi"

api.add_resource(getProducts, '/api/getproducts')
