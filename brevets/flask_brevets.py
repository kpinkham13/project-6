"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import os
import logging
import requests

###
# Globals
###
app = flask.Flask(__name__)
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)

###
# API Callers
###

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api"

def brevet_insert(start_time, length, checkpoints):
    _id = requests.post(f"{API_URL}/brevets", json={"start_time": start_time, "length": length, "checkpoints": checkpoints}).json()
    return _id

def brevet_find():
    lists = requests.get(f"{API_URL}/brevets").json()
    data = lists[-1]
    return data["start_time"], data["length"], data["checkpoints"]

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    print("Something")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    dist = request.args.get('dist', type=int)
    start_time = request.args.get('start', type=str)
    start_time = arrow.get(start_time, "YYYY-MM-DDTHH:mm") 
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, dist, start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, dist, start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/insert", methods=["POST"])
def insert():
    try:
        input_json = request.json
        start_time = input_json["start_time"]
        brevet_dist = input_json["brevet_dist"]
        checkpoints = input_json["checkpoints"]
        
        brevet_id = brevet_insert(start_time, brevet_dist, checkpoints)
         
        return flask.jsonify(result={},
                        message="Inserted!",
                        status=1,
                        mongo_id=brevet_id)

    except:
        return flask.jsonify(result={},
                        message="Oh no! Server error!",
                        status=0,
                        mongo_id='None')

@app.route("/fetch")
def fetch():
    try:
        start_time, length, checkpoints = brevet_find()
        return flask.jsonify(
                result={"start_time": start_time, "brevet_dist": length, "checkpoints": checkpoints},
                status=1,
                message="Successfully fetched the brevet list!")
    except:
        return flask.jsonify(
                result={},
                status=0,
                message="Something went wrong, couldn't fetch any lists!")

#############


if __name__ == "__main__":
    print("Opening for global access on port {}".format(port_num))
    app.run(port=port_num, host="0.0.0.0")
