import requests

API_KEY = "5b66cfcad32c421484601121a1a6f2dc"

def fetchCoords(location= None):
    if location == None:
        location = input('Enter a location to check the weather for >> ')

    URL = f"https://api.geoapify.com/v1/geocode/search?text={location}&limit=1&apiKey={API_KEY}"
    response = requests.get(URL)

    if response.status_code == 200:
        longitude = 0
        latitude = 0

        try:
            longitude = response.json()["features"][0]["geometry"]["coordinates"][0]
            latitude =  response.json()["features"][0]["geometry"]["coordinates"][1]
        except:
            print('Invalid location')
            return fetchCoords()
            
    else:
        raise Exception(f'Failed to connect with Weather API: {response.status_code}')

    return [latitude, longitude], location

print(fetchCoords()[0][0])