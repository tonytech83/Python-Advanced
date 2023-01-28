def forecast(*args):
    weather_data = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }

    hourly_forecast = []

    for location, weather in args:
        weather_data[weather].append(location)

    for weather, locations in weather_data.items():
        for location in sorted(locations):
            hourly_forecast.append(f'{location} - {weather}')

    return '\n'.join(hourly_forecast)


# Test code 1
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
# Test code 2
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
# Test code 3
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
