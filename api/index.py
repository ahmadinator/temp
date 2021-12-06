from flask import Flask

app = Flask(__name__)

@app.route("/api/")
def hi():
    return "hi"

@app.route("/api/getproducts")
def products():
    return "products"
