def printReport(weather, location):
    print(f'Your weather report for {location}')
    print('>> >>')
    print(f'Temperature: {round(weather[0])}°C')
    print(f'Weather: {fetchCondition(weather[1])}')
    print(f'Wind Speed: {round(weather[2])} mph')
    print(f'Humidity: {round(weather[3])}%')
    print('>> >>')

def fetchCondition(weather):
    match weather:
        case 0:
            return 'Clear Skies'
        case 1:
            return 'Mainly Clear'
        case 2:
            return 'Partly Cloudy'
        case 3:
            return 'Overcast'
        case 45:
            return 'Fog'
        case 48:
            return 'Depositing Rime Fog'
        case 51:
            return 'Light Drizzle'
        case 53:
            return 'Moderate Drizzle'
        case 55:
            return 'Heavy Drizzle'
        case 56:
            return 'Freezing Light Drizzle'
        case 57:
            return 'Freezing Heavy Drizzle'
        case 61:
            return 'Light Rain'
        case 63:
            return 'Moderate Rain'
        case 65:
            return 'Heavy Rain'
        case 66:
            return 'Freazing Light Rain'
        case 67:
            return 'Freezing Heavy Rain'
        case 71:
            return 'Light Snowfall'
        case 73:
            return 'Moderadte Snowfall'
        case 75:
            return 'Heavy Snowfall'
        case 77:
            return 'Snow Grains'
        case 80:
            return 'Light Showers'
        case 81:
            return 'Moderate Showers'
        case 82:
            return 'Heavy Showers'
        case 85:
            return 'Light Snow Showers'
        case 86:
            return 'Heavy Snow Showers'
        case 95:
            return 'Thunderstorm'
        case 96:
            return 'Thunderstorm with Slight Hail'
        case 99:
            return 'Thunderstorm with Heavy Hail'
        case _:
            return 'Unknown'