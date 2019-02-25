import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

neopixels = [
    {
	'id': 0,
	'values': {
	    'r': 255,
	    'g': 0,
	    'b': 127
	}
    },
    {
        'id': 1,
        'values':  {
            'r': 127,
            'g': 31,
            'b': 63
        }
    },
    {
        'id': 2,
        'values': {
            'r': 255,
            'g': 255,
            'b': 63
        }
    },
    {
        'id': 3,
        'values': {
            'r': 31,
            'g': 127,
            'b': 255
        }
    }
]

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>This api endpoint could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<h1>NEOPIXEL-API</h1><p>This site is a prototype API for nagios-neopixel.</p>"

@app.route('/api/v1/neopixels/all', methods=['GET'])
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

app.run(host='0.0.0.0')
