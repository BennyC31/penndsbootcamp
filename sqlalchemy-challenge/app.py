import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
        f"start and end format='YYYY-MM-DD' (Ex: '2018-02-04' or '2017-08-22/2018-02-04' )"
    )


@app.route("/api/v1.0/precipitation")
def percipitation():
    # Convert the query results to a dictionary using date as the key and prcp as the value.
    # Return the JSON representation of your dictionary.
    # Create our session (link) from Python to the DB
    session = Session(engine)
    percp_data = session.execute("select m.date,m.prcp from measurement m where date > (select date((SELECT m1.date \
                from measurement m1 order by m1.date DESC limit 1),'-1 year','-1 day'))").fetchall()  # .fetchmany(5)
    session.close()
    percp_dict = {}
    percp_dict = {k: v for (k, v) in percp_data}
    return jsonify(percp_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset.
    session = Session(engine)
    results = session.query(station.id, station.station, station.name).all()
    session.close()

    all_stations = []
    for id, stat, name in results:
        station_dict = {}
        station_dict['id'] = id
        station_dict['station'] = stat
        station_dict['name'] = name
        all_stations.append(station_dict)
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the previous year of data.
    # Return a JSON list of temperature observations (TOBS) for the previous year.
    session = Session(engine)
    results = session.query(measurement.station, measurement.date, measurement.tobs).filter(
        measurement.station == 'USC00519281').all()
    session.close()
    all_tobs = []
    for station, date, tobs in results:
        tobs_dict = {}
        tobs_dict['station'] = station
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    print(start)
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.
    session = Session(engine)
    results = None
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(
        measurement.tobs)).filter(measurement.date >= start).order_by(measurement.date.desc()).all()
    session.close()
    print(results)
    all_stat = []
    for stats in results:
        stats_dict = {}
        stats_dict['Min'] = results[0][0]
        stats_dict['Avg'] = results[0][1]
        stats_dict['Max'] = results[0][2]
        all_stat.append(stats_dict)
    return jsonify(all_stat)


@ app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).
    session = Session(engine)
    results = None
    results = session.query(func.min(measurement.tobs),
                            func.avg(measurement.tobs),
                            func.max(measurement.tobs)).filter(measurement.date >= start,
                                                               measurement.date <= end).order_by(measurement.date.desc()).all()
    session.close()
    print(results)
    all_stat = []
    for stats in results:
        stats_dict = {}
        stats_dict['Min'] = results[0][0]
        stats_dict['Avg'] = results[0][1]
        stats_dict['Max'] = results[0][2]
        all_stat.append(stats_dict)
    return jsonify(all_stat)


if __name__ == '__main__':
    app.run(debug=True)
