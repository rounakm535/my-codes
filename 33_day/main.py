import requests

MY_LAT = 26.234252
MY_LNG = 86.273094

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

print(data)

