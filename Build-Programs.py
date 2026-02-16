def greet_hello():
    print("Hello!!")
    print("Hello again!")

greet_hello()

def check_weather():
    temperature =25
    if temperature>30:
        print("Its hot")
    else:
        print("Nice weather!")

check_weather()

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("Amit", "Sharma")




import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)