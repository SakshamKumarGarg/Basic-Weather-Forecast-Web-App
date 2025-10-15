import requests
import matplotlib.pyplot as plt

# --- Helpers ---
def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    resp = requests.get(url, params={"name": city})
    data = resp.json()
    if "results" not in data or len(data["results"]) == 0:
        return None, None, None, None
    loc = data["results"][0]
    return loc["latitude"], loc["longitude"], loc["name"], loc["country"]

def get_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,weathercode",
        "timezone": "auto"
    }
    return requests.get(url, params=params).json()["daily"]

# Map weather codes → human text
WEATHER_CODE = {
    0: "☀️ Clear", 1: "🌤 Mainly clear", 2: "⛅ Partly cloudy", 3: "☁️ Overcast",
    45: "🌫 Fog", 48: "🌫 Depositing rime fog", 51: "🌦 Light drizzle", 61: "🌧 Light rain",
    71: "🌨 Light snow", 80: "🌦 Showers", 95: "⛈ Thunderstorm"
}

def display_dashboard(daily, city):
    dates = daily["time"]
    tmax, tmin = daily["temperature_2m_max"], daily["temperature_2m_min"]
    rain = daily["precipitation_sum"]
    wind = daily["windspeed_10m_max"]
    codes = daily["weathercode"]

    print(f"\n📊 7-Day Forecast for {city}")
    for d, t1, t2, r, w, c in zip(dates, tmax, tmin, rain, wind, codes):
        desc = WEATHER_CODE.get(c, "🌈 N/A")
        print(f"{d}: {desc}, Max {t1}°C, Min {t2}°C, Rain {r} mm, Wind {w} km/h")

    # Plot
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax1.plot(dates, tmax, marker='o', label="Max Temp (°C)")
    ax1.plot(dates, tmin, marker='o', label="Min Temp (°C)")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Temperature (°C)")
    ax1.tick_params(axis='x', rotation=45)
    ax1.legend(loc="upper left")

    # Rain on second axis
    ax2 = ax1.twinx()
    ax2.bar(dates, rain, alpha=0.3, color='blue', label="Rain (mm)")
    ax2.set_ylabel("Rain (mm)")
    ax2.legend(loc="upper right")

    plt.title(f"🌦 7-Day Weather Dashboard – {city}")
    # plt.tight_layout()
    plt.show()

# --- Main ---
city = input("Enter city name: ")
lat, lon, name, country = get_coordinates(city)

if lat is None:
    print("❌ City not found.")
else:
    print(f"✅ {name}, {country} (Lat {lat}, Lon {lon})")
    forecast = get_forecast(lat, lon)
    display_dashboard(forecast, f"{name}, {country}")
