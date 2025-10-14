import requests
import matplotlib.pyplot as plt


# Step 1: Ask user for a city
city = input("Enter city name: ")

# Step 2: Call the geocoding API
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city}
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

# Step 3: Extract latitude & longitude
if "results" in geo_data and len(geo_data["results"]) > 0:
    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    print(f"Found {location['name']}, {location['country']} → Lat: {latitude}, Lon: {longitude}")
else:
    print("City not found")

# Step 4: Call the weather API
weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}
weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

daily = weather_data["daily"]
dates = daily["time"]
temp_max = daily["temperature_2m_max"]
temp_min = daily["temperature_2m_min"]

# Step 5: Show current weather
# current = weather_data["current_weather"]
# print(f"\n🌦️ Current Weather in {location['name']}:")
# print(f"Temperature: {current['temperature']}°C")
# print(f"Windspeed: {current['windspeed']} km/h")

print(f"\n🌤️ 7-Day Forecast for {city}:")
for date, tmax, tmin in zip(dates, temp_max, temp_min):
    print(f"{date}: Max {tmax}°C, Min {tmin}°C")


# Step 4: Plot the forecast
plt.figure(figsize=(10,5))
plt.plot(dates, temp_max, marker='o', label="Max Temp")
plt.plot(dates, temp_min, marker='o', label="Min Temp")
plt.title(f"7-Day Temperature Forecast for {city}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
