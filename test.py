#!/usr/bin/python2.7

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

neopixels = [
]

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>This api endpoint could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<h1>NEOPIXEL-API</h1><p>This site is a API for neopixels.</p>"

@app.route('/api/v1/neopixels/get_all', methods=['GET'])
def neopixels_all():
    return jsonify(neopixels)

@app.route('/api/v1/neopixels/get_by_id', methods=['GET'])
def api_id():
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

@app.route('/api/v1/neopixels/set_all', methods=['GET'])
def neopixels_all():
    return jsonify(neopixels)


app.run(host='0.0.0.0')
