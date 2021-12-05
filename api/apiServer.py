from flask import Flask, escape, Response
from flask_restful import Resource, Api, reqparse

app1 = Flask(__name__)
app = Api(app)

class getProducts(Resource):
    def get(self):
        return "<h1>Hi</h1>"

app.add_resource(getProducts, '/api/getproducts')
