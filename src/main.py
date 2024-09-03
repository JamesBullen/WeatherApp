from search import fetchCoords
from weather import fetchWeather
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# API function
@app.route('/<location>/<distance>', methods=['GET'])
@cross_origin()
def weather(location, distance):
    addresses, coords = fetchCoords(location, int(distance))
    weather = fetchWeather(coords)

    response = jsonify(addresses, weather)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))