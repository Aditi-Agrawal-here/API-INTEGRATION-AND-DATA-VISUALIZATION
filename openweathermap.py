import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "9774e995a51c0dd3ea11e78ca8515fe3"
CITIES = ["Mumbai", "Pune", "Delhi", "Jaipur"]

weather_data = []

for CITY in CITIES:
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        with urllib.request.urlopen(BASE_URL) as response:
            data = response.read().decode()
            weather = json.loads(data)

        # Extract relevant weather data
        description = weather['weather'][0]['description'].capitalize()
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        # Append data to the list
        weather_data.append([CITY, temp, humidity, wind_speed, description])

    except Exception as e:
        print(f"Error fetching weather data for {CITY}:", e)

# Convert data into a Pandas DataFrame
df = pd.DataFrame(weather_data, columns=["City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Condition"])

# Save data to CSV
df.to_csv("weather_data.csv", index=False)
print("Weather data saved to 'weather_data.csv'!")

# 📊 Visualization using Seaborn
sns.set_style("whitegrid")

# Temperature Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm")
plt.title("Temperature in Different Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()

# Humidity Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="City", y="Humidity (%)", data=df, palette="Blues")
plt.title("Humidity in Different Cities")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.show()

# Wind Speed Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="City", y="Wind Speed (m/s)", data=df, palette="Greens")
plt.title("Wind Speed in Different Cities")
plt.xlabel("City")
plt.ylabel("Wind Speed (m/s)")
plt.show()
