import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

url = "http://api.openweathermap.org/data/2.5/onecall"

API_KEY = '5faa2643696ecd41624cd956047a1e0b'
MY_LAT = '42.775140'
MY_LONG = '-81.185980'

##SMS settings
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
client = Client(account_sid, auth_token)

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'units': 'metric',
    'exclude': "daily,current,minutely",
    'appid': API_KEY
}

response = requests.get(url, parameters)
response.raise_for_status()
data = response.json()

# print(data)
#
# counter = 0
# while counter < 12:

#
#         counter = counter + 1

msg = "Bring an Umbrella, chances of rain in next 12 hours"
weather_slice = data["hourly"][:12]

will_rain = False
for x in weather_slice:
    hour_data = x["weather"]
    weather_id = hour_data[0]['id']

    if int(weather_id) > 700:
        will_rain = True

if will_rain:
    print('It will rain in next 12 hours')
    message = client.messages \
    .create(
    body=msg,
    to='+14165206267',
    from_='+18643839494'
    )

