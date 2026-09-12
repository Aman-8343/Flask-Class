from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)    #static_folder="assets"

@app.route("/")
def hello_world():
    #print(url_for("static", filename="style2.css"))
    query=request.args.get("q",default="infinix")
    print(query)
    return render_template("index.html",query=query)

#api with json
@app.route("/me")
def me_api():
    data= {
        "username": "aman",
        "theme": "kdfls"
    }
    return jsonify(data),404

@app.route("/aski")
def hello():
    return "<p>Hello, LDR...</p>"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form["username"]
        return f"<p>hello {name}</p>"
    else:
        return render_template("login.html")

# @app.route("/handle-login",methods=["GET","POST"])
# def handle_login():
#     if request.method=="POST":
#         print(request.form)
#         name=request.form["username"]
#         password=request.form["password"]
#         return f"<p>welcome {name}! your pass is {password}</p>"
#         #return "<p>post request</p>"
#     if request.method=="GET":
#         return "<p>get request</p>"
#     return "<p>this is used to handle the form</p>"


@app.route("/jinja")
def embed():
    header="<header>ABC web<header>"
    name="aman"
    friends=["adam","bob","chalie"]

    return render_template("wlcm.html", name=name,friends=friends ,header=header)

@app.route("/reuse")
def templating_inheritannce():
    return render_template("layout.html")

@app.route("/contact")
def templating():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)