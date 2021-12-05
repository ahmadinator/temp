from flask import Flask, escape
from flask_restful import Resource, Api, reqparse

app1 = Flask(__name__)
app = Api(app1)

class getProducts(Resource):
    def get(self):
        return "hi"
app.add_resource(getProducts, '/api/')
