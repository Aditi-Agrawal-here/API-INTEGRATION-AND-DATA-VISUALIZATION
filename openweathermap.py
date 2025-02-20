import urllib.request
import json
import pandas as pd

API_KEY = "9774e995a51c0dd3ea11e78ca8515fe3"
CITIES = ["Mumbai", "Pune", "Tokyo", "London"]

weather_data = []

for CITY in CITIES:
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        with urllib.request.urlopen(BASE_URL) as response:
            data = response.read().decode()
            weather = json.loads(data)

        
        description = weather['weather'][0]['description'].capitalize()
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        
        weather_data.append([CITY, temp, humidity, wind_speed, description])

    except Exception as e:
        print(f"Error fetching weather data for {CITY}:", e)

df = pd.DataFrame(weather_data, columns=["City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Condition"])

df.to_csv("weather_data.csv", index=False)

print(" Weather data saved to 'weather_data.csv'!")
