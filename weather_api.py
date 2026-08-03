# weather_api.py
# This program gets the current weather for a city using OpenWeatherMap

import requests

# Put your own API key here (get one for free at openweathermap.org)
api_key = "API key placholder"
city = "London"

# Build the URL for the API request
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

# Make the request
response = requests.get(url)

# Check if the request worked
if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print("City:", city)
    print("Temperature:", temperature, "C")
    print("Conditions:", description)
else:
    print("Something went wrong. Status code:", response.status_code)