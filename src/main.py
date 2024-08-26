from search import fetchCoords
from weather import fetchWeather
from flask import Flask, request, jsonify

app = Flask(__name__)

# API function
@app.route('/<location>/<distance>', methods=['GET'])
def weather(location, distance):
    addresses, coords = fetchCoords(location, int(distance))
    weather = fetchWeather(coords)

    response = jsonify(addresses, weather)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')