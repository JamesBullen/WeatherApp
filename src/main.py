from search import fetchCoordsLoop
from weather import fetchWeather
from report import printReport

def main():
    coords, location = fetchCoordsLoop()
    weather = fetchWeather(coords)

    printReport(weather, location)

main()