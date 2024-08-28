import requests
from datetime import datetime

USERNAME = "rounakm535"
TOKEN = "isitanapikey"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "streak2"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Codes",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {

    "date": today.strftime("%Y%m%d"),
    "quantity": "25",
}

response = requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)
print(response.text)
