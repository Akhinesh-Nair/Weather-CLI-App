"""
weather.py

This module contains functions to:
1. Fetch weather by city name.
2. Fetch weather by PIN code.
3. Save search history.
"""

import requests
from datetime import datetime
from config import API_KEY, BASE_URL 


def save_history(search_type,search_value):
    """
    Save the user's search query with the current date and time.

    Parameters:
        search_type (str): Type of search (city or pincode).
        search_value (str): The city name or PIN code entered by the user.
    """
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M%p")
    # Open the history file in append mode.
    with open("history.txt", "a") as file:

        # Write the search along with the current timestamp.
        file.write(f"{current_time}|{search_type}: {search_value}\n")


def get_weather_by_city(city):
    """
    Fetch weather information using the city name.

    Parameters:
        city (str): Name of the city.

    Returns:
        dict: Weather information in JSON format.
        None: If the city is not found.
    """

    # Create request parameters.
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    # Send request to OpenWeatherMap API.
    response = requests.get(BASE_URL, params=params)

    # Check whether the request was successful.
    if response.status_code != 200:
        return None

    # Save successful search.
    save_history("City", city)

    # Return weather data.
    return response.json()


def get_weather_by_pincode(pin, country="IN"):
    """
    Fetch weather information using a PIN code.

    Parameters:
        pin (str): Postal/PIN code.
        country (str): Country code (Default = IN).

    Returns:
        dict: Weather information.
        None: If the PIN code is invalid.
    """

    # Create request parameters.
    params = {
        "zip": f"{pin},{country}",
        "appid": API_KEY,
        "units": "metric"
    }

    # Send request.
    response = requests.get(BASE_URL, params=params)

    # Return None if request fails.
    if response.status_code != 200:
        return None

    # Save successful search.
    save_history("PIN", pin)

    # Return JSON response.
    return response.json()