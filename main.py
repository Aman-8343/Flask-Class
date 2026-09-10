from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Pal , A man this side...</p>"

@app.route("/aski")
def hello():
    return "<p>Hello, LDR...</p>"

app.run(debug=True)