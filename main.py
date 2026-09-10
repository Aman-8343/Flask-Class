from flask import Flask, render_template, url_for

app = Flask(__name__,static_folder="assets")

@app.route("/")
def hello_world():
    print(url_for("static", filename="style2.css"))
    return render_template("index.html")

@app.route("/aski")
def hello():
    return "<p>Hello, LDR...</p>"


if __name__=="__main__":
    app.run(debug=True)