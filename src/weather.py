import openmeteo_requests
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

baseURL = "https://api.open-meteo.com/v1/forecast"

def fetchWeather(coords):
    params = {
    "latitude": coords[0],
	"longitude": coords[1],
	"hourly": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
	"forecast_days": 1
	}
    
    responses = openmeteo.weather_api(baseURL, params=params)
    response = responses[0]

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
    hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()
    hourly_wind_speed_10m = hourly.Variables(3).ValuesAsNumpy()

    return hourly_temperature_2m[-1], hourly_weather_code[-1], hourly_wind_speed_10m[-1], hourly_relative_humidity_2m[-1]