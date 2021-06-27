import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_cors import CORS
import json
import operator






uspc_class_all_file = open ('uspc_class_all.json', "r")
uspc_class_all_json = json.loads(uspc_class_all_file.read())

uspc_class_daysandrate_all_file = open ('uspc_class_daysandrate_all.json', "r")
uspc_class_daysandrate_all_json = json.loads(uspc_class_daysandrate_all_file.read())

uspc_attorney_success_withnames_all_file = open ('uspc_attorney_success_withnames_all.json', "r")
uspc_attorney_success_withnames_all_json = json.loads(uspc_attorney_success_withnames_all_file.read())

#################################################

# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>" # br line break
        f"/api/v1.0/uspc_class_all<br/>"
        f"/api/v1.0/uspc_class_daysandrate<br/>"
        f"/api/v1.0/uspc_class_daysandrate_all<br/>"
        f"/api/v1.0/uspc_attorney_success_withnames<br/>"
        f"/api/v1.0/uspc_attorney_success_withnames_all"
    )

@app.route("/api/v1.0/uspc_class_all")
def uspc_class_all(uspc_class=None):
    print(uspc_class_all_json)
    return jsonify(uspc_class_all_json)



@app.route("/api/v1.0/uspc_class_daysandrate/<uspc_class>")
def uspc_class_daysandrate(uspc_class=None):
    for row in uspc_class_daysandrate_all_json:
        if row[0] == str(uspc_class):
            return jsonify(row)
    return jsonify([]) 

@app.route("/api/v1.0/uspc_class_daysandrate_all")
def uspc_class_daysandrate_all(uspc_class=None):
    print(uspc_class_daysandrate_all_json)
    return jsonify(uspc_class_daysandrate_all_json) 

@app.route("/api/v1.0/uspc_attorney_success_withnames/<uspc_class>")
def uspc_attorney_success_withnames(uspc_class=None):
    attorneys = []
    for row in uspc_attorney_success_withnames_all_json:
        if row[0] == str(uspc_class):
            # print(row)
            attorneys.append(row)
    attorneys = sorted(attorneys, key=operator.itemgetter(3))
    top = attorneys[-100:len(attorneys)]
    top.reverse()
    print(top)
    return jsonify(top) 

@app.route("/api/v1.0/uspc_attorney_success_withnames_all")
def uspc_attorney_success_withnames_all(uspc_class=None):
    return jsonify(uspc_attorney_success_withnames_all_json) # This is a dictionary


if __name__ == '__main__':
    app.run()