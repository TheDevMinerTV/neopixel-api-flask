#!/usr/bin/python2.7

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = False

LED_COUNT = 150 # Amount of neopixels


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
# Get all neopixels
@app.route('/api/v1/all/get', methods=['GET'])
def neopixels_all_get():
    return jsonify(neopixels)

# Set all neopixels to off
@app.route('/api/v1/all/clear', methods=['PUT'])
def neopixels_all_clear():
    for i in range(len(neopixels)):
        neopixels[i] = {'id': i, 'values': {'r': 0, 'g': 0, 'b': 0}}
    
    for i in range(len(neopixels), LED_COUNT):
        neopixels.append({'id': i, 'values': {'r': 0, 'g': 0, 'b': 0}})
    
    return jsonify(neopixels)

# Set all neopixels to colors according to a array
@app.route('/api/v1/all/set_by_array', methods=['POST'])
def neopixels_all_set_by_array():
    if len(request.json) < LED_COUNT or len(request.json > LED_COUNT):
        abort(400)
    
    for i in range(len(neopixels)):
        neopixels[i] = request.json[i]
    
    for i in range(len(neopixels), LED_COUNT):
        neopixels.append(request.json[i])

    return jsonify(neopixels)


# SINGLE
# Get neopixel by id
@app.route('/api/v1/single/get', methods=['GET'])
def neopixels_single_get():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for neopixel in neopixels:
        if neopixel['id'] == id:
            results.append(neopixel)

    return jsonify(results)

# Set neopixel by id
@app.route('/api/v1/single/set', methods=['PUT', 'POST'])
def neopixels_single_set():
    id = request.json['id']
    if request.method == 'PUT':
        for neopixel in neopixels:
            if neopixel['id'] == id:
                return "Error: ID " + str(id) + " already exists!"
        neopixels.append(request.json)

    elif request.method == 'POST':
        for i, neopixel in enumerate(neopixels):
            if neopixel['id'] == id:
                neopixels[i] = request.json
                print('Neopixel with id ' + str(id) + " got updated with json " + str(request.json))
                print('After update pixel with id ' + str(id) + " has json " + str(neopixels[i]))
                return jsonify(neopixels)
        neopixels.append(request.json)
    
    sort_ids()
    return jsonify(neopixels)


app.run(host='0.0.0.0')
