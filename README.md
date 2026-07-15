# 🌦️ Weather Application (CLI)

## Intern Details

- **Intern ID:** CITS6205
- **Full Name:** Akhinesh Nair
- **Duration:** 4 Weeks
- **Project Name:** Weather Application (CLI)

---

## Project Scope

The Weather CLI Application is a Python-based command-line program that allows users to retrieve real-time weather information using the OpenWeatherMap API. The application provides a simple menu-driven interface to search weather details by city name or PIN code, view search history, and access project information.

---

## Objectives

- Fetch real-time weather data using an API.
- Develop a menu-driven command-line application.
- Practice Python programming concepts such as functions, modules, file handling, and API integration.
- Store user search history.
- Implement proper exception handling and code documentation.

---

## Features

- Search weather by **City Name**
- Search weather by **PIN Code**
- Display:
  - City
  - Country
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Pressure
  - Weather Description
  - Wind Speed
- View search history
- Menu-driven interface
- Error handling for invalid inputs

---

## Technologies Used

- Python 3.12
- Requests Library
- OpenWeatherMap API

---

## Project Structure

```
Weather-CLI-App/
│
├── main.py
├── weather.py
├── config.py
├── history.txt
├── requirements.txt
├── README.md
├── screenshots/
├── documentation/
└── .gitignore
```

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/Akhinesh-Nair/Weather-CLI-App.git
```

2. Open the project folder.

```bash
cd Weather-CLI-App
```

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

5. Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Open `config.py` and add your OpenWeatherMap API key.

```python
API_KEY = "YOUR_API_KEY"
```

---

## Running the Application

```bash
python main.py
```

---

## Sample Menu

```
===================================
      WEATHER CLI APPLICATION
===================================

1. Search Weather by City
2. Search Weather by PIN Code
3. View Search History
4. About
5. Exit
```

---

## Sample Output

```
========== WEATHER REPORT ==========

City        : Kochi
Country     : IN
Temperature : 29°C
Feels Like  : 33°C
Humidity    : 78%
Pressure    : 1008 hPa
Weather     : Broken Clouds
Wind Speed  : 4.2 m/s
```

---

## Future Enhancements

- 5-day weather forecast
- Air Quality Index (AQI)
- Search using GPS coordinates
- Export weather reports to a text file
- Weather alerts

---

## Conclusion

The Weather CLI Application demonstrates Python programming, API integration, modular programming, exception handling, and file handling. It provides a simple and effective way to retrieve weather information from the command line and serves as a practical learning project.

---

## Author

**Akhinesh Nair**

Python Internship Project
