# Weather-Analysis
Overview:
This Python-based desktop application is designed to deliver real-time weather updates for any city you choose. By leveraging the Tkinter library for its graphical user interface and the Plyer library for desktop notifications, the app seamlessly integrates with the OpenWeatherMap API to fetch and display accurate weather data.


Features:
User-Friendly Interface:
A clean and simple GUI allows users to input the desired city name easily.
Labels and buttons are well-organized for intuitive navigation.

Real-Time Weather Data:
Retrieves up-to-date weather information from the OpenWeatherMap API.

Displays the following details:
Temperature (in Celsius, converted from Kelvin). Atmospheric pressure (in hPa).Humidity percentage. A brief description of current weather conditions (e.g., "clear sky," "rain").

Desktop Notifications:
Weather details are displayed as desktop notifications for easy accessibility.Notifications appear with a timeout of 2 seconds, ensuring non-intrusiveness.

Error Handling:
Provides user feedback through pop-up messages in case of invalid city names or API errors.

Technical Details:
Temperature Conversion:
The app converts the temperature from Kelvin (as provided by the API) to Celsius for user-friendliness.
Formula used: Celsius = Kelvin - 273.15.
API Integration:
The app uses the OpenWeatherMap API to fetch weather details.
Users need to replace the placeholder API key (apiKey) with their personal API key obtained from OpenWeatherMap.

Requirements:
Python Version: Python 3.x (tested for compatibility).
Libraries:
tkinter: Pre-installed with Python.
plyer: Install using pip install plyer.
requests: Install using pip install requests.
OpenWeatherMap API Key:
Sign up for a free account on OpenWeatherMap to obtain an API key.
Replace the placeholder key (apiKey) in the code with your personal key.
