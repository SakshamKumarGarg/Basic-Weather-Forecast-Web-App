import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 28.61,        # Delhi
    "longitude": 77.23,
    "current_weather": True
}
response = requests.get(url, params=params)
data = response.json()
current = data["current_weather"]
print("🌦️  Current Weather:")
print(f"Temperature: {current['temperature']}°C")
print(f"Windspeed: {current['windspeed']} km/h")

