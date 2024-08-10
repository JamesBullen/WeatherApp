import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

# Loops function until a valid location is passed through
def fetchCoordsLoop():
    while True:
        results = fetchCoords()
        if results != False:
            break
    return results


# Fetches global coordinates of a given location
def fetchCoords():
    location = input('Enter a location you would like to check: ')

    URL = f"https://api.geoapify.com/v1/geocode/search?text={location}&limit=1&apiKey={API_KEY}"
    response = requests.get(URL)

    # Smart arse may to see if status code is between 200 and 299
    # Checks if successfully connected to API
    if response.status_code // 100 != 2:
        raise Exception(f'Failed to connect with Weather API: {response.status_code}')
    
    # Checks if given location is valid by if 'features' is not empty, which contain the needed global coords
    shortResponse = response.json()['features'][0]
    if shortResponse:
        longitude = shortResponse["geometry"]["coordinates"][0]
        latitude =  shortResponse["geometry"]["coordinates"][1]
        address = f'{shortResponse['properties']['address_line1']}, {shortResponse['properties']['address_line2']}'

        # Returns
        return [latitude, longitude], address

    #Returns but false
    print('Not a valid location')
    return False