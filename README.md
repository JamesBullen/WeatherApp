# Weather App
Flask API which takes any vague, or specific address, and returns data of the current weather there.

## About
Once up and running as a server, it'll pull a location from any GET requests file path. Then it'll pass it on to a GeoCode API which will return the most relevant global coordinates. If they are not accurate, then a more specific location needs to be passed ot the API. These coordinates are passesd onto another satellite weather API, with the parameters of which specific weather data we want for that location.

These results are formated, and returned to the original requester. A full address is also returened to help the end user confirm if the weather is for their intended location. Due to multiple areas having the same/similair names.

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
