# Weather App
Flask API which takes any vague, or specific address, and returns data of the current weather there.

## About
Once up and running as a server, it'll pull a location and mile radius from the GET requests file path. The location is passed onto a GeoCode API, which will return the most relevant global coordinates, and a formated address to confirm with the end user. If the address returned to the end user is not accurate, then a more specific location needs to be passed ot the API. These initial results will be stored in a SQLite database, which is then checked for any other stored towns/cities within the given mile radious for there coordinates.

These coordinates are passesd onto another API, which retrieves the weather data from the most relevant sattalite service. If no local areas are found in the database, then 4 sets of coordinates will be passed through in the cardinal directions determined by the given mile radius. These results are formated, and returned with addresses to the original requester.

## Installation
### Dependencies
- Python 3.12.2
- openmeteo-requests API
- requests-cache 1.2.1
- retry-requests 2.0.0
- dotenv 1.0.1
- Flask 3.0.3
- Werkzeug 3.0.3

### Dev Dependencies
- Unit Tests

### Installation
Simply place the folder on the device you wish to run it on.

### Executing program
- `./main.sh` if this does not run, then use `chmod +x main.sh` to make the file executable
- Alternatively `python3 src/main.py` can be used

## Authors
- James Bullen

## Acknowledgements
- David Sadler for improvement suggestions
- Chrisitan Perry for prompt and review
