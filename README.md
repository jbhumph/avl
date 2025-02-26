# State Temperature Graph
Climate data comparison web-app utilizing an AVL tree for CS 240

## Author
John Humphrey

## Contents
- [Author](#author)
- [Overview](#overview)
- [Instructions](#instructions)
- [About](#about)
- [AVL Tree](#avl-tree)
- [Dependencies](#dependencies)
- [Screenshots](#screenshots)


## Overview
US State Temperature Graph is a web application that allows one to select a state and then visualize annual temperature data over a 10 year period against a national average. This uses a REST API call to NOAA's climate data, specifically their Global Summary of the Year Report.

This initiated as way to implement an AVL tree and then expanded into this project. I wanted to use an AVL tree at the heart of the program while using a diverse tech stack to obtain variable data to run through it and then later traverse. This program uses Python / Flask / Bootstrap and is deployed from Heroku.


## Instructions
The application has been deployed and should be available at the following address:

https://avg-temp-a27676261ea1.herokuapp.com/

Because I am using Heroku's Eco plan for hosting, the site may take an extra few seconds to load when first visiting.

The application may also be run locally. Feel free to clone the project file and open it up in your IDE. You'll need create a new Python virtual environment and in that terminal run:

```
pip install -r requirements.txt
```

This will install all dependencies for the project. At that you will just need to run:

```
python -m flask run
```

This should compile and run the program at the stated local address.


## About
The focal point of this project is the app.py file. This represents the backend of the program. We initialize Flask and Bootstrap. We then define our routes to all sites - most of which are logically quite simple. At this point we can access all of our html documents which are cascaded with Jinja, template.html being the foundation for nthe site's markdown. The site integrated Bootstrap for nearly all of it's styling and much of that can be seen here. 

The bulk of the logic comes with the application itself. We send a GET request to the NOAA server with our parameters in the body and token in the header. 

```
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
```

Upon succesful receipt of the data, we proceed to parse it and add it to the AVL tree. More info on the AVL tree in the following section. Once the tree has been created we create an array with the data and pass it into the graph page via Jinja.

Within graph.html we create a new canvas which will utilize the Chart.js library. There is then a script block on the page where we parse out the data into smaller arrays for average, max average, low average temperature arrays. This data is then fed into the logic for the graph. We then proceed to parse out the primary array into a table using Jinja's limited iterative functions.


## AVL Tree



## Dependencies


## Screenshots

