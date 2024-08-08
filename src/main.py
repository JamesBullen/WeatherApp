from search import fetchCoords
from weather import fetchWeather
from report import printReport

def main():
    location = str(input('Enter a location to check the weather for >> '))
    coords = fetchCoords(location)
    weather = fetchWeather(coords)

    printReport(weather, location)

main()