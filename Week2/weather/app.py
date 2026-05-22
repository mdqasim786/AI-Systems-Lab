import requests

# API URL
url = "https://api.open-meteo.com/v1/forecast?latitude=33.6&longitude=73.1&current_weather=true"

# Send request
response = requests.get(url)

# Convert JSON to Python dictionary
data = response.json()

# Extract weather data
weather = data["current_weather"]

temperature = weather["temperature"]
windspeed = weather["windspeed"]
time = weather["time"]

# Clean output
print("\nWeather Report")
print("----------------")

print(f"Temperature: {temperature}°C")
print(f"Wind Speed: {windspeed} km/h")
print(f"Time: {time} GST")