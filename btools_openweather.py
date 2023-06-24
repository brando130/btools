##################################################################
# B-TOOLS-OPENWEATHER v0.24
#
# OpenWeather:
# current_weather(city (string)) - returns a JSON object with current weather
#
##################################################################

import requests
import os

def current_weather(city):

    API_KEY = os.environ["OPENWEATHER_API_KEY"]
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)
    data = response.json()

    return data