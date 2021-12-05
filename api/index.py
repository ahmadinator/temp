from flask import Flask
from flask_restful import Resource, Api

app1 = Flask(__name__)
app = Api(app1)

class test(Resource):
    def get(self):
        return "hi"
    
app.add_resource(test, '/api/')
