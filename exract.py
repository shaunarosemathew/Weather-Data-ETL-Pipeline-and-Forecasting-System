import requests
import json

API_KEY = "ce3329b3279160fbbd93138dd7f09b29"

cities = ["Chennai", "Mumbai", "Bangalore", "Hyderabad"]

weather_data = []

for city in cities:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data.append(data)
        print(f"Data collected for {city}")
    else:
        print(f"Failed for {city}")
        print(response.text)

with open("raw_data.json", "w") as file:
    json.dump(weather_data, file, indent=4)

print("Weather data saved successfully!")