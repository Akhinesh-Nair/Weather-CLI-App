"""
main.py

This is the main file of the Weather Application (CLI).

It provides a menu-driven interface that allows users to:
1. Search weather by city.
2. Search weather by PIN code.
3. View search history.
4. View application details.
5. Exit the program.
"""

# Import weather functions.
from weather import get_weather_by_city, get_weather_by_pincode


def display(data):
    """
    Display weather information in a readable format.

    Parameters:
        data (dict): Weather data returned by the API.
    """

    print("\n========== WEATHER REPORT ==========")

    print("City        :", data["name"])
    print("Country     :", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels Like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Pressure    :", data["main"]["pressure"], "hPa")
    print("Weather     :", data["weather"][0]["description"].title())
    print("Wind Speed  :", data["wind"]["speed"], "m/s")


def history():
    """
    Display all previous searches stored in history.txt.
    """
    print("\n========== SEARCH HISTORY ==========\n")
    try:

        # Open history file.
        with open("history.txt", "r") as file:
            lines=file.readlines()

            if not lines:
                print("No search history available.")
                return
            
            for i,line in enumerate(lines,start=1):
                print(f"{i}.{line.strip()}")

    except FileNotFoundError:

        # If history file doesn't exist.
        print("\nNo search history available.")


def about():
    """
    Display application information.
    """

    print("\n========== ABOUT ==========")
    print("Project : Weather CLI Application")
    print("Language : Python")
    print("API : OpenWeatherMap")
    print("Version : 1.0")


#  MAIN PROGRAM

while True:

    # Display menu.
    print("\n===================================")
    print("      WEATHER CLI APPLICATION")
    print("===================================")

    print("1. Search Weather by City")
    print("2. Search Weather by PIN Code")
    print("3. View Search History")
    print("4. About")
    print("5. Exit")

    # Accept user's choice.
    choice = input("\nEnter your choice: ")

    # Search using city.
    if choice == "1":

        city = input("Enter City Name: ")

        data = get_weather_by_city(city)

        if data:
            display(data)
        else:
            print("\nCity not found.")

    # Search using PIN code.
    elif choice == "2":

        pin = input("Enter PIN Code: ")

        data = get_weather_by_pincode(pin)

        if data:
            display(data)
        else:
            print("\nInvalid PIN Code.")

    # View history.
    elif choice == "3":
        history()

    # About project.
    elif choice == "4":
        about()

    # Exit application.
    elif choice == "5":

        print("\nThank you for using Weather CLI Application.")
        print("Goodbye!")

        break

    # Invalid menu choice.
    else:

        print("\nInvalid choice. Please try again.")