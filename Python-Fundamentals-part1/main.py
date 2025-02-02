# EXAMPLES NOT FOR USE
# --------------------

import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load environment variables from .env file

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def main():
    api_key = os.getenv('API_KEY')  # Get API key from environment variable
    city = input("Enter city name: ")
    weather = get_weather(city, api_key)
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    main()

# EXAMPLES NOT FOR USE
# --------------------
