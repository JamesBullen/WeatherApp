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
        "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"]
	}
    
    response = openmeteo.weather_api(baseURL, params=params)

    current = response[0].Current()
    current_temperature_2m = round(current.Variables(0).Value())
    current_relative_humidity_2m = current.Variables(1).Value()
    current_weather_code = round(current.Variables(2).Value())
    current_wind_speed_10m = round(current.Variables(3).Value())

    print('Returning weather')
    return [current_temperature_2m, current_weather_code, current_wind_speed_10m, current_relative_humidity_2m]