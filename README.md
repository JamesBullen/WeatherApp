# Weather App
Django API which takes any vague or specific address, and a mile radius. Then returns data of the current weather, and the surrounding area within the given radius.

## About
Once it recieves a GET requests, it'll pull a location and mile radius from the url path. The location is passed onto a GeoCode API, which will return the most relevant global coordinates, and a formated address to confirm with the end user. If the address returned to the end user is not accurate, then a more specific location needs to be passed ot the API. These initial results will be stored in a SQLite database, which is then checked for any other stored towns/cities within the given mile radious for there coordinates.

These coordinates are passesd onto another API, which retrieves the weather data from the most relevant sattalite service. If no local areas are found in the database, then 4 sets of coordinates will be passed through in the cardinal directions determined by the given mile radius. These results are formated, and returned with addresses to the original requester.

## Installation
### Dependencies
- Python 3.12.2
- openmeteo-requests API
- requests-cache 1.2.1
- retry-requests 2.0.0
- dotenv 1.0.1
- django 5.2
- gunicorn 22
- whitenoise[brotli] 3
- djangorestframework
- django-cors-headers

### Dev Dependencies
- Unit Tests

## Authors
- James Bullen

## Acknowledgements
- David Sadler for improvement suggestions
- Chrisitan Perry for prompt and review
