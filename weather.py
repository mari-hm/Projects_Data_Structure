import requests

api_key = "e8002eb7ac6144538ce114637230707"  
city = input("Enter city name: ")

base_url = "http://api.weatherapi.com/v1/current.json"
params = {"key": api_key, "q": city}
response = requests.get(base_url, params=params)
data = response.json()

if "error" in data:
    print(f"Error: {data['error']['message']}")
else:
    location = data["location"]["name"]
    weather_info = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]

    print(f"Weather in {location}:")
    print(f"Description: {weather_info}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
