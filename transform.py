import json
import pandas as pd

with open("raw_data.json", "r") as file:
    data = json.load(file)

rows = []

for city in data:
    rows.append({
        "City": city["name"],
        "Temperature": city["main"]["temp"],
        "Humidity": city["main"]["humidity"],
        "Pressure": city["main"]["pressure"],
        "Weather": city["weather"][0]["main"],
        "Wind Speed": city["wind"]["speed"]
    })

df = pd.DataFrame(rows)

print(df)

df.to_csv("weather_data.csv", index=False)

print("CSV file created successfully!")