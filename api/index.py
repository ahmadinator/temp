from flask import Flask

app = Flask(__name__)

@app.route("/api/getproducts")
def productsA():
    return "products"

@app.route("/api/lol")
def lolxd():
    return "lol??"
