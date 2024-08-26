import openmeteo_requests
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

baseURL = "https://api.open-meteo.com/v1/forecast"

def fetchWeather(coords):
    print('Fetching Weather')

    params = {
        "latitude": coords[0],
        "longitude": coords[1],
        "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
	    "wind_speed_unit": "mph"
	}
    
    response = openmeteo.weather_api(baseURL, params=params)

    temperatures = []
    humidities = []
    weatherCodes = []
    windSpeed = []

    for i in range(len(coords[0])):
        current = response[i].Current()
        temperatures.append(round(current.Variables(0).Value()))
        humidities.append(current.Variables(1).Value())
        weatherCodes.append(round(current.Variables(2).Value()))
        windSpeed.append(round(current.Variables(3).Value()))

    print('Returning weather')
    return [weatherCodes, temperatures, windSpeed, humidities]