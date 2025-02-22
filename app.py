import datetime
from flask_bootstrap import Bootstrap5
from flask import Flask
from flask import render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.datetime.now()
    )

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
