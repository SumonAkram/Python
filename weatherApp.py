import requests

def get_weather_forecast(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "b7f049816662b873bcbd79ab42ec215f"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        city_name = input("Enter city name: ")
        weather_data = get_weather_forecast(city_name, api_key)
        
        # Check if 'name' key exists in weather data
        if 'name' in weather_data:
            # Display weather forecast
            print("Weather Forecast:")
            print(f"City: {weather_data['name']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Description: {weather_data['weather'][0]['description']}")
            break  # Exit the loop if the city is found
        else:
            print("City not found. Please enter a valid city name.")  # Print message for invalid city
            attempts += 1
    
    # If all attempts are used up without finding a valid city
    if attempts == max_attempts:
        print("You've reached the maximum number of incorrect attempts. Please try again later!")
        exit()  # Automatically exit the program after displaying the final message

if __name__ == "__main__":
    main()
