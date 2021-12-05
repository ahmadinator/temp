from flask import Flask, escape, Response
from flask_restful import Resource, Api, reqparse

app1 = Flask(__name__)
app = Api(app)

class getProducts(Resource):
    def get(self):
        return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

app.add_resource(getProducts, '/api/getproducts')
