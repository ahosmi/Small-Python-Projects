import requests

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("City not found. Please check the city name.")

if __name__ == "__main__":
    city_name = input("Enter the name of the city: ")
    api_key = "4b5d3255ad30116691b6630e176bb743"
    weather_data = fetch_weather(city_name, api_key)
    display_weather(weather_data)
