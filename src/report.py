# All possible weather codes the API can return
weatherCode = {0:'Clear Skies', 1:'Mainly Clear', 2:'Partly Cloudy', 3:'Overcast', 45:'Fog', 48:'Depositing Rime Fog',51:'Light Drizzle', 53:'Moderate Drizzle',
               56:'Freezing Light Drizzle', 57:'Freezing Heavy Drizzle', 61:'Light Rain', 63:'Heavy Rain', 65:'Heavy Rain', 66:'Freazing Light Rain', 67:'Freezing Heavy Rain',
               71:'Light Snowfall', 73:'Moderadte Snowfall', 75:'Heavy Snowfall', 77:'Snow Grains', 80:'Light Showers', 81:'Moderate Showers', 82:'Heavy Showers',
               85:'Light Snow Showers', 86:'Heavy Snow Showers', 95:'Thunderstorm', 96:'Thunderstorm with Slight Hail', 99:'Thunderstorm with Heavy Hail'}

# Prints to console data recieved from API in a user friendly manner
def printReport(weather, location):
    forecast = getForecast(weather[1])

    # Determines how long border needs to print
    length = lambda x: 20 if x < 11 else x + 11
    border = f"#{'=' * length(len(forecast))}#"

    # Prints report itself
    print('>>')
    print(f'Your weather report for {location}:')
    print(border)
    print(f'  Temperature: {weather[0]}°C')
    print(f'  Weather: {forecast}')
    print(f'  Wind Speed: {weather[2]} mph')
    print(f'  Humidity: {weather[3]}%')
    print(border)

def getForecast(weather):
    return weatherCode[weather]