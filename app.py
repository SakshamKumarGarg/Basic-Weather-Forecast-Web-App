import requests
import matplotlib.pyplot as plt

def get_coordinates(city):
    """Convert city name to latitude & longitude"""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city}
    response = requests.get(geo_url, params=params)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        location = data["results"][0]
        return location["latitude"], location["longitude"], location["name"], location["country"]
    else:
        return None, None, None, None

def get_forecast(lat, lon):
    """Fetch daily forecast for given coordinates"""
    forecast_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto"
    }
    response = requests.get(forecast_url, params=params)
    data = response.json()
    return data["daily"]

def display_forecast(daily, city_name):
    """Print and plot the forecast"""
    dates = daily["time"]
    temp_max = daily["temperature_2m_max"]
    temp_min = daily["temperature_2m_min"]

    print(f"\n🌤️ 7-Day Forecast for {city_name}:")
    for date, tmax, tmin in zip(dates, temp_max, temp_min):
        print(f"{date}: Max {tmax}°C, Min {tmin}°C")

    # Plotting
    plt.figure(figsize=(10,5))
    plt.plot(dates, temp_max, marker='o', label="Max Temp")
    plt.plot(dates, temp_min, marker='o', label="Min Temp")
    plt.title(f"7-Day Temperature Forecast for {city_name}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

# ===== Main Program =====
city = input("Enter city name: ")
lat, lon, name, country = get_coordinates(city)

if lat is None:
    print("❌ City not found. Please try again.")
else:
    print(f"✅ Found {name}, {country} → Lat: {lat}, Lon: {lon}")
    daily_forecast = get_forecast(lat, lon)
    display_forecast(daily_forecast, name)
