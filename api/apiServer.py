from flask import Flask, Response
app = Flask(__name__)

@app.route('/api/')
def catch_all(path):
    return Response("<h1>Flask</h1><p>Hi</p>", mimetype="text/html")
