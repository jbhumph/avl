from flask_bootstrap import Bootstrap5
from flask import Flask
from flask import render_template
import requests
from flask import jsonify

app = Flask(__name__)

bootstrap = Bootstrap5(app)
API_KEY = "greycat78"
EMAIL = "jbhumph@gmail.com"

@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/graph/")
def graph():
    return render_template("graph.html")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route('/air_quality', methods=['GET'])
def get_air_quality():
    url = "https://aqs.epa.gov/data/api/annualData/byState"
    params = {
        "email": EMAIL,
        "key": API_KEY,
        "param": "45201",
        "bdate": "19950515",
        "edate": "19950515",
        "state": "37"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")
        return jsonify({"error": "Invalid JSON response"}), 500
    except requests.exceptions.RequestException as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500
