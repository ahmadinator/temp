from flask import Flask, escape
app = Flask(__name__)

class getProducts(Resource):
    def get(self):
        return "hi"
