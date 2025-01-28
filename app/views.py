from rest_framework.response import Response
from rest_framework.decorators import api_view
from search import fetchCoords
from weather import fetchWeather

# Create your views here.
@api_view(['GET'])
def temp(request, location, distance):
    print(location)
    addresses, coords = fetchCoords(location, int(distance))
    print(addresses, coords)
    weather = fetchWeather(coords)

    response = (addresses, weather)

    return Response(response)