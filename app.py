from flask_bootstrap import Bootstrap5
from flask import Flask, request
from flask import render_template
import requests
from flask import jsonify
import binaryTree

app = Flask(__name__)

bootstrap = Bootstrap5(app)
API_KEY = "CXJAbHFmcAzhlzKmCkVSSdhODynSAJTi"
EMAIL = "jbhumph@gmail.com"

@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/graph/", methods=['GET', 'POST'])
def graph():
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
    tree = binaryTree.BinaryTree()
    state_name = "Washington"
    selected_state = "GHCND:USW00024233"

    # NOAA station IDs for major US cities
    noaa_stations = {
        "GHCND:USW00013876": "Alabama",  # Birmingham Intl Airport
        "GHCND:USW00026451": "Alaska",  # Anchorage
        "GHCND:USW00023183": "Arizona",  # Phoenix
        "GHCND:USW00013963": "Arkansas",  # Little Rock
        "GHCND:USW00023174": "California",  # Los Angeles
        "GHCND:USW00023234": "Colorado",  # Denver
        "GHCND:USW00014739": "Connecticut",  # Hartford
        "GHCND:USW00013781": "Delaware",  # Wilmington
        "GHCND:USW00012839": "Florida",  # Miami
        "GHCND:USW00013874": "Georgia",  # Atlanta
        "GHCND:USW00022521": "Hawaii",  # Honolulu
        "GHCND:USW00024131": "Idaho",  # Boise
        "GHCND:USW00094846": "Illinois",  # Chicago
        "GHCND:USW00093819": "Indiana",  # Indianapolis
        "GHCND:USW00014933": "Iowa",  # Des Moines
        "GHCND:USW00003928": "Kansas",  # Wichita
        "GHCND:USW00093820": "Kentucky",  # Louisville
        "GHCND:USW00012916": "Louisiana",  # New Orleans
        "GHCND:USW00014764": "Maine",  # Portland
        "GHCND:USW00093721": "Maryland",  # Baltimore
        "GHCND:USW00014739": "Massachusetts",  # Boston
        "GHCND:USW00094847": "Michigan",  # Detroit
        "GHCND:USW00014922": "Minnesota",  # Minneapolis
        "GHCND:USW00013927": "Mississippi",  # Jackson
        "GHCND:USW00013994": "Missouri",  # St. Louis
        "GHCND:USW00024153": "Montana",  # Billings
        "GHCND:USW00014942": "Nebraska",  # Omaha
        "GHCND:USW00023169": "Nevada",  # Las Vegas
        "GHCND:USW00014710": "New Hampshire",  # Concord
        "GHCND:USW00014734": "New Jersey",  # Newark
        "GHCND:USW00023050": "New Mexico",  # Albuquerque
        "GHCND:USW00094728": "New York",  # New York City
        "GHCND:USW00013722": "North Carolina",  # Charlotte
        "GHCND:USW00024011": "North Dakota",  # Fargo
        "GHCND:USW00014821": "Ohio",  # Columbus
        "GHCND:USW00013967": "Oklahoma",  # Oklahoma City
        "GHCND:USW00024229": "Oregon",  # Portland
        "GHCND:USW00014737": "Pennsylvania",  # Philadelphia
        "GHCND:USW00014765": "Rhode Island",  # Providence (nearest major)
        "GHCND:USW00013883": "South Carolina",  # Columbia
        "GHCND:USW00014944": "South Dakota",  # Sioux Falls
        "GHCND:USW00013897": "Tennessee",  # Nashville
        "GHCND:USW00013958": "Texas",  # Dallas
        "GHCND:USW00024127": "Utah",  # Salt Lake City
        "GHCND:USW00014742": "Vermont",  # Burlington
        "GHCND:USW00013743": "Virginia",  # Richmond
        "GHCND:USW00024233": "Washington",  # Seattle
        "GHCND:USW00003860": "West Virginia",  # Charleston
        "GHCND:USW00014839": "Wisconsin",  # Madison
        "GHCND:USW00024018": "Wyoming"  # Cheyenne
    }

    # Get selected state from menu
    if request.method == 'POST':
        selected_state = request.form.get("state")
    
    headers = {
    "token": API_KEY
    }
    params = {
        "datasetid": "GSOY",
        "stationid": selected_state,
        "startdate": "2014-01-01",
        "enddate": "2023-12-31",
        "limit": 1000,
        "datatypeid": "TAVG,TMAX,TMIN,PRCP" 
    }

    # Make request
    response = requests.get(url, headers=headers, params=params)

    # Process response
    if response.status_code == 200:
        climate_data = response.json()
        state_name = noaa_stations[selected_state]
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
        return render_template("graph.html", arr=arr, selected_state=selected_state, state_name=state_name)
    else:
        print(f"Error {response.status_code}: {response.text}")

    


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

