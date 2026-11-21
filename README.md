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

Clone this repository.

Install dependencies:

pip install -r requirements.txt

Create a .env file using .env.example as a template.

Add your own API credentials to .env.

Run the project:

python main.py


## Security
API keys and Twilio credentials are stored in `.env` and are not included in this repository.
