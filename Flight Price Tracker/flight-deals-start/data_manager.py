import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/369d8aee12a0a1dc369d6d93e0bfdc18/flightDeals/flightDealsPricesCsv"

class DataManager:

    def __init__(self):
        self._user = "rounakm535"
        self._password = "Rounak@1879"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        print("API Response:")
        pprint(data)  # This will print the entire response structure

        # Check if the response contains any data
        if not data:
            print("Error: Empty response from API")
            return []

        # Try to find the correct key for the data
        possible_keys = ['flightDealsPricesCsv', 'flightdealspricescsv', 'FlightDealsPricesCsv', 'sheet1', 'Sheet1']
        for key in possible_keys:
            if key in data:
                self.destination_data = data[key]
                return self.destination_data

        # If we couldn't find the data, print the available keys
        print("Error: Could not find expected data in the response")
        print("Available keys in the response:", list(data.keys()))
        return []

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "flightDealsPricesCsv": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)