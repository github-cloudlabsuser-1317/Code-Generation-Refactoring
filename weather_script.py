import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("Failed to retrieve weather data. Please check the city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)