from search import fetchCoordsLoop
from weather import fetchWeather
from report import printReport, getForecast
from flask import Flask, request, jsonify

app = Flask(__name__)

# Only used to check the weather from an interal command
def main():
    coords, address = fetchCoordsLoop()
    weather = fetchWeather(coords)

    printReport(weather, address)

# API function
@app.route('/<location>')
def weather(location):
    coords, address = fetchCoordsLoop(location)
    weather = fetchWeather(coords)
    weather[1] = getForecast(weather[1])

    response = jsonify(weather, address)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')