import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

url = "http://api.openweathermap.org/data/2.5/onecall"

API_KEY = os.environ.get('API_KEY')
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
    'exclude': "hourly,current,minutely",
    'appid': API_KEY
}

response = requests.get(url, parameters)
response.raise_for_status()
data = response.json()

#print(data)

daily = data["daily"]
tomorrow = daily[1]

weather = tomorrow["weather"][0]['main']
max = tomorrow["temp"]['max']
min = tomorrow["temp"]['min']
feels_like = tomorrow["feels_like"]['day']
print(f"weather {weather} max {max} min {min} feels{feels_like}")

sms_text = f"Tomorrow weather will have {weather} with max temp {max} and min temp {min}" \
    f" and feels like will be {feels_like} C"\
    f" Bonishhhhhhhhhhh :)"

# msg = "Bring an Umbrella, chances of rain in next 12 hours"
# weather_slice = data["hourly"][:12]
#
# print(weather_slice)
print(sms_text)
#
#
# if will_rain:
#     print('It will rain in next 12 hours')
message = client.messages \
    .create(
    body=sms_text,
    to=os.environ.get('dest'),
    from_='+18643839494'
    )

