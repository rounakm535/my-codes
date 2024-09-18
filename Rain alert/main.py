import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import socket


def check_internet_connection():
    try:
        # Try to resolve Google's DNS
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


# OpenWeatherMap configuration
api_key = "483b85d1157af3b2b013c6b8b8e10849"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 19.816380,
    "lon": 85.830650,
    "cnt": 4,
    "appid": api_key
}

# Twilio configuration
account_sid = 'AC8bc294ed3130da69d96031e047985739'
auth_token = '43adaa7e7dcd5cf9b84a4bbc1202faf8'

if not check_internet_connection():
    print("No internet connection. Please check your network settings.")
else:
    try:
        # Get weather data
        response = requests.get(endpoint, params=weather_params)
        response.raise_for_status()
        data = response.json()

        # Check if it will rain
        will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in data["list"])

        if will_rain:
            # Initialize Twilio client
            client = Client(account_sid, auth_token)

            try:
                # Send WhatsApp message
                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body="It's going to rain today. Remember to bring an umbrella!",
                    to='whatsapp:+919852637240'
                )
                print(f"Message sent successfully. Status: {message.status}")
            except TwilioRestException as e:
                print(f"Twilio API error: {e}")
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to Twilio API: {e}")
        else:
            print("No rain forecasted.")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
