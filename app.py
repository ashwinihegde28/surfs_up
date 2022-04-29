from email.mime import base
from statistics import mean
from unittest import result


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

import datetime as dt
import numpy as np
import pandas as pd


#The create_engine() function allows us to access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflects the database
Base = automap_base()   

# Python Flask function to reflect the tables 
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to the database
session = Session(engine)




app = Flask(__name__)
@app.route('/')   
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    #convert to one dimentional array using function np.ravel(), with results as our parameter and than into list using list()
    stations = list(np.ravel(results))
    return jsonify(stations=stations) #to return our list as JSON, we need to add stations=stations.

@app.route("/api/v1/tobs")    
def temp_monthly() :
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.date >= prev_year).\
        filter(Measurement.station == 'USC00519281').all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#set start and end parameters to none
# will give null values if start and end date are not mentioned in the route. use /api/v1.0/temp/2017-06-01/2017-06-30 as route
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


