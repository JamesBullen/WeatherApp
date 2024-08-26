import requests
import math
import sqlite3
import os
from dotenv import load_dotenv

# Gets API keys from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
GOOGLE_KEY = os.getenv('GOOGLE_KEY')

# Fetches global coordinates of a given and nearby locations
def fetchCoords(location, distance):
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_KEY}')

    if response.json()['status'] != 'OK':
        return False

    # Extracts required data from API respnse
    results = response.json()['results'][0]
    address = results['formatted_address']
    lat = results['geometry']['location']['lat'] # 90 to -90 | (pi / 180) * 6371km | newLat = lat + (distance / 6371km) * (180 / pi)
    lng = results['geometry']['location']['lng'] # 180 to -180 | (p1 / 180) * 6371km * cos(lat * pi / 180) | newLng = lng + (distance / 6371km) * (180 / pi) / cos(newLat * pi / 180)

    # Looks for postal town address component
    tempList = []
    for component in results['address_components']:
        if ('postal_town' in component['types']):
            tempList.append(component['long_name'])
        if ('administrative_area_level_2' in component['types']):
            tempList.append(component['long_name'])
    
    # Adds to SQLite table if required address components found
    if len(tempList) == 2:
        addToTable(tempList, lat, lng)

    # Checks database for nearby locations, and returns results if any found
    nearbyLocations = checkTable(lat, lng, distance)
    if nearbyLocations != []:
        return (address, lat, lng), nearbyLocations
    
    # If no nearby areas are stored in the database, will display the weather from 4 cardinal within given distance
    return cardinalLocations(address, distance, lat, lng)

# Checks if distance bewteen two global coords are within range
def checkTable(lat, lng, distance):
    # Creates connection to database, and a cursor to interact with it
    connection = sqlite3.connect('pastSearches.db')
    cursor = connection.cursor()

    latDisPlus = lat + ((distance / 2) * 0.01449275362318840579710144927536)
    latDisMin = lat - ((distance / 2) * 0.01449275362318840579710144927536)
    lngDisPlus = lng + ((distance / 2) * 0.01831501831501831501831501831502)
    lngDisMin = lng - ((distance / 2) * 0.01831501831501831501831501831502)

    try:
        query = 'SELECT * FROM tblTowns WHERE (lat BETWEEN ? AND ?) AND (lng BETWEEN ? AND ?) AND (lat != ?) AND (lng != ?)'
        params = (latDisMin, latDisPlus, lngDisMin, lngDisPlus, lat, lng)
        cursor.execute(query, params)
        results = cursor.fetchall()
    except:
        print('error')

    # Closes connection to database
    connection.close()
    
    return results

def cardinalLocations(address, distance, lat, lng):
    newDistance = math.sqrt(distance**2 / 2)
    nwLat, nwLng = newCoords(lat, lng, newDistance, -newDistance)
    neLat, neLng = newCoords(lat, lng, newDistance, newDistance)
    swLat, swLng = newCoords(lat, lng, -newDistance, -newDistance)
    seLat, seLng = newCoords(lat, lng, -newDistance, newDistance)

    # Returned data is order sensetive
    return [address, 'North West', 'North East', 'South West', 'South East'], [[lat, nwLat, neLat, swLat, seLat], [lng, nwLng, neLng, swLng, seLng]]

# Gives new global coords in given distance and direction
earthRadiusMiles = 3958.756
def newCoords(lat, lng, dy, dx):
    newLat = lat + (dy / earthRadiusMiles) * (180 / math.pi)
    newLng = lng + (dx / earthRadiusMiles) * (180 / math.pi) / math.cos(newLat * math.pi / 180)

    return newLat, newLng

def addToTable(input, lat, lng):
    # Creates connection to database, and a cursor to interact with it
    connection = sqlite3.connect('pastSearches.db')
    cursor = connection.cursor()

    # Creates a Towns table if one doesn't exist already
    cursor.execute('CREATE TABLE IF NOT EXISTS tblTowns(town TEXT NOT NULL UNIQUE, lat INT NOT NULL, lng INT NOT NULL);')

    # Inserts the values into the table
    try:
        query = 'INSERT INTO tblTowns(town, lat, lng) VALUES(?, ?, ?)'
        params = (f'{input[0]}, {input[1]}', lat, lng)
        cursor.execute(query, params)
    except:
        print('insert error')

    # Commits changes to table, and then closes the connection
    connection.commit()
    connection.close()

print(fetchCoords('watford', 10))