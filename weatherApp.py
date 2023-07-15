class Weather:
    def __init__(self, city, temperature, description):
        self.city = city
        self.temperature = temperature
        self.description = description

class WeatherApp:
    def display_weather(self, weather):
        print(f"City: {weather.city}")
        print(f"Temperature: {weather.temperature}°C")
        print(f"Description: {weather.description}")

weather_app = WeatherApp()

current_weather = Weather("New York", 25.5, "Sunny")
weather_app.display_weather(current_weather)

another_weather = Weather("London", 18.2, "Cloudy")
weather_app.display_weather(another_weather)
