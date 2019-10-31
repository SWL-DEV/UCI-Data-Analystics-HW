# import all dependencies
import numpy as np

import datetime as dt
from datetime import datetime, timedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )



@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_prcp = []
    for date, prcp in results:
        precipitation_dict = {date:prcp}
        all_prcp.append(precipitation_dict)

    # Return the JSON representation of your dictionary.
    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.station, Station.name, func.count(Measurement.station))\
                                   .join(Station, Measurement.station == Station.station)\
                                   .group_by(Measurement.station)\
                                   .order_by(func.count(Measurement.station)).all()

    session.close()

    all_stations = []
    for station, name, activities in results:
        stations_dict = {}
        stations_dict["station_id"] = station
        stations_dict["station_name"] = name
        stations_dict["activities_count"] = activities
        all_stations.append(stations_dict)

    # Return a JSON list of stations from the dataset.
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query for the dates and temperature observations from a year from the last data point.
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    for date in last_date:
        date = date

    one_year_ago = datetime.strptime(date, '%Y-%m-%d') - dt.timedelta(days=365)

    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date > one_year_ago).all()

    session.close()

    one_year_tobs = []
    for station, date, tobs in results:
        one_year_tobs_dict = {}
        one_year_tobs_dict["station_id"] = station
        one_year_tobs_dict["date"] = date
        one_year_tobs_dict["temperature_observation"] = tobs
        one_year_tobs.append(one_year_tobs_dict)


    # Return a JSON list of Temperature Observations (tobs) for the previous year.
    return jsonify(one_year_tobs)


@app.route("/api/v1.0/<start>")
def calc_temps(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date
    canonicalized = start.replace("/","-")
    canonicalized2 = f"{start[0:4]}-{start[4:6]}-{start[6:8]}"
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()
    
    one_year_temp_calc = []
    for tmin, tavg, tmax in results:
        one_year_temp_calc_dict = {}
        one_year_temp_calc['tmin'] = tmin
        one_year_temp_calc['tavg'] = tavg
        one_year_temp_calc['tmax'] = tmax
        one_year_temp_calc.append(one_year_temp_calc_dict)

        if start == canonicalized or start == canonicalized2:
            return jsonify(one_year_temp_calc)

    return jsonify({"error": "date not found."}), 404


# @app.route("/api/v1.0/<start>/<end>")
# def calc_temps2(start,end)
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     # Calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date
#     start1 = start.replace("/","-")
#     start2 = f"{start[0:4]}-{start[4:6]}-{start[6:8]}"

#     end1 = end.replace("/","-")
#     end2 = f"{end[0:4]}-{end[4:6]}-{end[6:8]}"
    
#     results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

#     session.close()
    
#     one_year_temp_calc = []
#     for tmin, tavg, tmax in results:
#         one_year_temp_calc_dict = {}
#         one_year_temp_calc['tmin'] = tmin
#         one_year_temp_calc['tavg'] = tavg
#         one_year_temp_calc['tmax'] = tmax
#         one_year_temp_calc.append(one_year_temp_calc_dict)

#         if start == (start1 or start2) and end == (end1 or end2):

#             return jsonify(one_year_temp_calc)

#     return jsonify({"error": "date not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)