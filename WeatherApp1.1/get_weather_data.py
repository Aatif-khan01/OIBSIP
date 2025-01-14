import requests

API_key = 'd6c01232093e4678d500e6fd2b339778'

print("Welcome to WeatherApp 1.1! Created by Aatif Muneeb Khan")

def get_units():
    units = input(
        "Enter units (metric for Celsius, imperial for Fahrenheit, default is Kelvin): ").strip().lower()
    valid_units = ["metric", "imperial", "kelvin", ""]
    if units not in valid_units:
        print("Invalid units. Defaulting to Kelvin.")
        return ""  # Default to Kelvin if the input is invalid
    return units

def display_weather(city_name, data, units):
    unit_labels = {
        "metric": "°C",
        "imperial": "°F",
        "kelvin": "K",
    }
    unit_label = unit_labels.get(units, "K")  # Default to Kelvin if units are empty

    print(f"\nWeather in {city_name}:")
    print(f"Weather is: {data['weather'][0]['description']}")
    print(f"Current Temperature: {data['main']['temp']} {unit_label}")
    print(f"Current Temperature Feels Like: {data['main']['feels_like']} {unit_label}")
    print(f"Humidity: {data['main']['humidity']}%")

def get_weather():
    try:#The try block wraps the entire while loop. This ensures that if a KeyboardInterrupt is triggered the program will catch it and exit gracefully
        while True:
            city_name = input("\nEnter a city name or ZIP code (or type 'exit' to quit): ").strip()
            if city_name.lower() == "exit":
                print("Goodbye!")
                break  # The loop will exit if the user types 'exit'

            if not city_name:
                print("Please enter a valid city name or ZIP code.")
                continue  # The loop will continue if input is empty

            units = get_units()

            # Construct the API request URL
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units={units}'

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                display_weather(city_name, data, units)
            else:
                print(f"\nFailed to fetch data for '{city_name}'. HTTP Status Code: {response.status_code}")
                print("Response:", response.json())
                print("Please check the city name or try again later.")
                continue  # Continues asking for a city if the request fails

    except KeyboardInterrupt:#When the user interrupts the program, it prints: "Program interrupted. Exiting gracefully..." instead of showing a traceback error.
        print("\nProgram interrupted. Exiting gracefully...")

if __name__ == "__main__":
    get_weather()
