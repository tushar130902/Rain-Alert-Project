# Rain Alert Project
Rain Alert Project

# Rain Alert Project 🌧️

## About
A Python-based Rain Alert application that checks upcoming weather forecasts using the OpenWeatherMap API and sends an SMS notification through Twilio if rain is expected.

## Features
- Fetches weather forecast data using OpenWeatherMap API.
- Checks upcoming weather conditions.
- Detects rain conditions.
- Sends SMS alerts using Twilio.

## Technologies Used
- Python
- Requests
- OpenWeatherMap API
- Twilio API
- Python-dotenv

## Installation

1. Clone this repository.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Create a `.env` file using `.env.example` as a template.
4. Add your own API credentials to `.env`.
5. Run the project:

   `python main.py`

## Security
API keys and Twilio credentials are stored in `.env` and are not included in this repository.