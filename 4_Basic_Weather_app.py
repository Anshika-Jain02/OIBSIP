import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
    else:
        print("Error:", data["message"])

def main():
    api_key = "c5fdd157c717b881cc3353991a149f24"  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
