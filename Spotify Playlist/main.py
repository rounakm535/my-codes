import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

time = input("Which year do you want to travel ? Type the date in this format YYYY-MM-DD: ")

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = "https://www.billboard.com/charts/hot-100/" + time

CLIENT_ID = "4222374e4be8457aa603e0ea22c3c131"
SECRET = "dee0b35939764a679af79a57786219b7"
USERNAME = "31vqqctsp76emer7hy3va26fd7mi"

response = requests.get(url=URL, headers=HEADER)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_name_listing = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)