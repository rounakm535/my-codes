import requests

MY_LAT = 28.6139  # Latitude for New Delhi
MY_LNG = 77.2090  # Longitude for New Delhi

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

try:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # This will raise an exception for 4XX/5XX errors

    data = response.json()

    s_rise = data["results"]["sunrise"]
    s_set = data["results"]["sunset"]

    print(f"Sunrise: {s_rise}")
    print(f"Sunset: {s_set}")

    print(s_rise.split("T")[1].split(":"))
    print(s_set.split("T")[1].split(":"))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    print(f"Response content: {response.content}")  # This will print the response content if available


