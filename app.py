from flask_bootstrap import Bootstrap5
from flask import Flask, request
from flask import render_template
import requests
from flask import jsonify
import json
import binaryTree

app = Flask(__name__)

bootstrap = Bootstrap5(app)
#API_KEY = "greycat78"
API_KEY = "CXJAbHFmcAzhlzKmCkVSSdhODynSAJTi"
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

@app.route('/air_quality', methods=['GET', 'POST'])
def get_air_quality():
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
    tree = binaryTree.BinaryTree()
    
    if request.method == 'POST':
        print(request.form.get("state"))
    
    headers = {
    "token": API_KEY  # NOAA requires token in the headers
    }
    params = {
        "datasetid": "GSOY",  # ✅ Global Summary of the Year
        "stationid": "GHCND:USW00024233",
        "startdate": "2014-01-01",
        "enddate": "2023-12-31",
        "limit": 1000,  # Adjust as needed
        "datatypeid": "TAVG,TMAX,TMIN,PRCP"  # ✅ Average Temp & Precipitation
    }

    response = requests.get(url, headers=headers, params=params)

    # Process response
    if response.status_code == 200:
        climate_data = response.json()
        year = None
        temp = None
        tmax = None
        tmin = None
        prcpt = None
        for i in climate_data['results']:
            if year != i['date'][:4]:
                year = i['date'][:4]
            if i['datatype'] == 'TAVG':
                temp = i['value']
            elif i['datatype'] == 'PRCP':
                prcpt = i['value']
            elif i['datatype'] == 'TMAX':
                tmax = i['value']
            elif i['datatype'] == 'TMIN':
                tmin = i['value']
            if temp and prcpt:
                tree.insert(int(year), temp, tmax, tmin, prcpt)
                temp = None
                tmax = None
                tmin = None
                prcpt = None
        arr = []
        tree.setArray(tree.get_root(), arr)
        return render_template("graph.html", arr=arr)
        
    else:
        print(f"Error {response.status_code}: {response.text}")

    
