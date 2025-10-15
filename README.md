# 🌤 Weather Forecast Dashboard

A simple and interactive **weather forecast web app** built with **Python**, **Streamlit**, and **Open-Meteo APIs**.  
It provides a **7-day forecast** — including temperature, wind speed, and rainfall — for any city in the world 🌍.

---

## 📸 Demo Preview

Type a city → click **Get Forecast** → view:
- ✅ City details (country, coordinates)
- 🌤 Weather descriptions (Clear, Rain, Cloudy, etc.)
- 📊 Interactive temperature & rainfall chart

---

## 🧠 Concept Overview

This project demonstrates how to **use APIs in Python** to build a real-world data application.  
You’ll learn how to:
- Send HTTP **GET requests**
- Handle **JSON responses**
- Chain **multiple APIs** (Geocoding + Forecast)
- Display data using **Streamlit**
- Visualize results with **Matplotlib**

---

## 🗂 Project Structure
weather-dashboard/
│
├── weather_dashboard.py # Main Streamlit app
├── requirements.txt # Dependencies
└── README.md # Documentation

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SakshamKumarGarg/Simple-Weather-Forecast-Web-App.git
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the app
```bash
streamlit run weather_dashboard.py
```
💻 How It Works
1. City to Coordinates 🌍

The app uses Open-Meteo Geocoding API to convert the user’s city input into latitude and longitude.

2. Fetch Weather Forecast 🌦

Then it uses Open-Meteo Forecast API to retrieve 7-day weather data for that location.

3. Parse and Visualize 📊

The JSON response is parsed to extract:

Max/Min Temperature

Precipitation

Wind Speed

Weather Codes (mapped to emojis like ☀️, 🌧, 🌫)

Finally, the app displays:

Clean textual forecast

Temperature & Rainfall chart








