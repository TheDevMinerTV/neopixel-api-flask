#!/usr/bin/python2.7

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

neopixels = [
]

def sort_ids():
    for passnum in range(len(neopixels)-1,0,-1):
        for i in range(passnum):
            if neopixels[i]>neopixels[i+1]:
                temp = neopixels[i]
                neopixels[i] = neopixels[i+1]
                neopixels[i+1] = temp

@app.errorhandler(404)
def four_o_four(e):
    return "<h1>404</h1><p>This api endpoint could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<h1>NEOPIXEL-API</h1><p>This site is a API for neopixels.</p>"

# ALL
@app.route('/api/v1/neopixels/all/get', methods=['GET'])
def neopixels_all_get():
    return jsonify(neopixels)

# SINGLE
@app.route('/api/v1/neopixels/single/get_by_id', methods=['GET'])
def neopixels_single_get_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for neopixel in neopixels:
        if neopixel['id'] == id:
            results.append(neopixel)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/neopixels/single/create_by_id', methods=['PUT'])
def neopixels_single_set_by_id():
    id = request.json['id']
    for neopixel in neopixels:
        if neopixel['id'] == id:
            return "Error: ID " + str(id) + " already exists!"  
    
    neopixels.append(request.json)
    sort_ids()
    return jsonify(neopixels)


app.run(host='0.0.0.0')
