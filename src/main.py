from search import fetchCoordsLoop
from weather import fetchWeather
from report import printReport, getForecast
from flask import Flask, request, jsonify

app = Flask(__name__)

def main():
    coords, address = fetchCoordsLoop()
    weather = fetchWeather(coords)

    printReport(weather, address)

@app.route('/<location>')
def weather(location):
    coords, address = fetchCoordsLoop(location)
    weather = fetchWeather(coords)
    weather[1] = getForecast(weather[1])

    return jsonify(weather, address), 200

if __name__ == '__main__':
    app.run(debug=True)