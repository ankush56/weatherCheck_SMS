import requests

url = "http://api.openweathermap.org/data/2.5/forecast"

# http://api.openweathermap.org/data/2.5/forecast?lat=42.775140&lon=-81.185980&units=metric&appid=5faa2643696ecd41624cd956047a1e0b

API_KEY = '5faa2643696ecd41624cd956047a1e0b'
MY_LAT = '42.775140'
MY_LONG = '-81.185980'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'units': 'metric',
    'appid': API_KEY
}

response = requests.get(url, parameters)
data = response.json()

counter = 0
for x in data["list"]:
    weather_list = x["weather"]
    for y in weather_list:
        if 'rain' in y['description']:
            print("It will rain")
