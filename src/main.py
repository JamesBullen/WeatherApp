from search import fetchCoords
from weather import fetchWeather
from report import printReport

def main():
    coords, location = fetchCoords()
    weather = fetchWeather(coords)

    printReport(weather, location)

main()