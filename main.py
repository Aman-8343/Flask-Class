from flask import Flask, render_template, url_for, request

app = Flask(__name__)    #static_folder="assets"

@app.route("/")
def hello_world():
    #print(url_for("static", filename="style2.css"))
    return render_template("index.html")

@app.route("/aski")
def hello():
    return "<p>Hello, LDR...</p>"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/handle-login",methods=["GET","POST"])
def handle_login():
    if request.method=="POST":
        print(request.form)
        name=request.form["username"]
        password=request.form["password"]
        return f"<p>welcome {name}! your pass is {password}</p>"
        #return "<p>post request</p>"
    if request.method=="GET":
        return "<p>get request</p>"
    return "<p>this is used to handle the form</p>"


if __name__=="__main__":
    app.run(debug=True)