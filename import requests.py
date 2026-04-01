import requests

# Lahore coordinates
url = "https://api.open-meteo.com/v1/forecast?latitude=31.5497&longitude=74.3436&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current_weather = data.get("current_weather", {})
    temperature = current_weather.get("temperature")
    print("Current Temperature:", temperature, "°C")
else:
    print("Error:", response.status_code)
