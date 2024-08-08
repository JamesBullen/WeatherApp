import requests

API_KEY = "5b66cfcad32c421484601121a1a6f2dc"

def fetchCoords(input):
    address = input
    URL = f"https://api.geoapify.com/v1/geocode/search?text={address}&limit=1&apiKey={API_KEY}"
    response = requests.get(URL)

    if response.status_code == 200:
        longitude = 0
        latitude = 0

        try:
            longitude = response.json()["features"][0]["geometry"]["coordinates"][0]
            latitude =  response.json()["features"][0]["geometry"]["coordinates"][1]
        except:
            raise Exception('Invalid location')
    else:
        raise Exception(f'Failed to connect with Weather API: {response.status_code}')

    return latitude, longitude