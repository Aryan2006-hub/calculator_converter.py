
import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_weather(city):
    if not API_KEY:
        print("Please set your OpenWeather API key first.")
        return

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            f"{BASE_URL}/weather",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        print("\n--- Current Weather ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])

        forecast_response = requests.get(
            f"{BASE_URL}/forecast",
            params=params,
            timeout=10
        )
        forecast_response.raise_for_status()
        forecast = forecast_response.json()

        print("\n--- Forecast (Next 5 Days) ---")
        shown_dates = set()

        for item in forecast["list"]:
            date_text = item["dt_txt"].split()[0]

            if date_text not in shown_dates:
                shown_dates.add(date_text)
                print(
                    date_text,
                    "|", item["main"]["temp"], "°C",
                    "|", item["weather"][0]["description"]
                )

    except requests.exceptions.HTTPError as error:
        if response.status_code == 401:
            print("Invalid or not-yet-active API key.")
        elif response.status_code == 404:
            print("City not found. Check the spelling.")
        else:
            print("API error:", error)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    except (KeyError, ValueError) as error:
        print("Could not process weather data:", error)


while True:
    print("\n--- Weather App ---")
    print("1. Check Weather")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        city = input("Enter city name: ").strip()
        if city:
            get_weather(city)
        else:
            print("City name cannot be empty.")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
