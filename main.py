import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("api_key")
Account_SID = os.getenv("Account_SID")
Auth_Token = os.getenv("Auth_Token")
sender = os.getenv("send")
receiver = os.getenv("rec")



weather_params = {
    "lat": 22.067459,
    "lon": 88.137177,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()


# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(Account_SID,Auth_Token)
    message = client.messages.create(
        to = receiver,
        from_= sender,
        body="sms_internal_alerts",

    )
    print(message.sid)


    