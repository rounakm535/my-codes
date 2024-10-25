import requests

import datetime

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
from spotipy.cache_handler import CacheFileHandler


def process_artist(s: str) -> str:
    """ Returns a more 'friendly' string for Spotify search engine. """
    out = s.replace("'", "")

    open_par = out.find("(")
    close_par = out.find(")")
    if 0 <= open_par < close_par:
        out = out.split("(")[0] + out.split(")")[1]
    out = out.split("Feat")[0]

    return out


def process_track(s: str) -> str:
    """ Returns a more 'friendly' string for Spotify search engine. """
    out = s.replace("'", "")

    open_par = out.find("(")
    close_par = out.find(")")
    if 0 <= open_par < close_par:
        out = out.split("(")[0] + out.split(")")[1]

    words = out.split(" ")
    out = ""
    for w in words:
        if w.find('*') < 0:
            out = out + w + " "

    return out


def get_song_uris(client: Spotify, tracks: [str], track_artists: [str]) -> [str]:
    """ Returns song uris from tracks and artists names. """
    uris = []
    for track, artist in zip(tracks, track_artists):
        processed_track = process_track(track)
        processed_artist = process_artist(artist)

        query = f"{processed_track} {processed_artist}"
        results = client.search(q=query, type="track", market="US", limit=1)
        try:
            uris.append(results["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"'{track} --- {artist}' not found.")
            print(f"{processed_track} --- {processed_artist}.")

    return uris


def get_playlist(client: Spotify, user: int, name: str) -> int:
    """ Returns playlist's id by name. Returns 0 if it already existed. """
    playlists = spotify.user_playlists(user_id)["items"]

    for p in playlists:
        if p["name"] == name:
            return 0

    playlist = client.user_playlist_create(user=user, name=name, public=False)

    return playlist["id"]


def get_spotify_client() -> Spotify:
    """ Returns a spotipy client based on inside-function data. """
    spotify_client_id = "4222374e4be8457aa603e0ea22c3c131"
    spotify_client_secret = "dee0b35939764a679af79a57786219b7"
    spotify_redirect_uri = "www.example.com"
    spotify_scope = "playlist-modify-private playlist-read-private"  # Allows us to read and modify private playlists
    spotify_cache_handler = CacheFileHandler("./token.txt")

    return Spotify(
        auth_manager=SpotifyOAuth(
            client_id=spotify_client_id,
            client_secret=spotify_client_secret,
            redirect_uri=spotify_redirect_uri,
            scope=spotify_scope,
            cache_handler=spotify_cache_handler
        )
    )


def get_billboard_songs_artists(date_str: str) -> ([str], [str]):
    """ Gets top 100 billboard title songs and artists from parameter date.
        Returns ([song_list], [artist_list]). """
    billboard_url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(billboard_url + date_str)

    soup = BeautifulSoup(response.text, "html.parser")
    # There are a lot of trash '\n' and '\t' in raw content
    raw_titles = [t.getText() for t in soup.select("li > h3.c-title")]
    raw_artists = [artist.getText() for artist in soup.select("li > span.a-no-trucate")]

    # Get rid of those \n and \t
    processed_titles = [t.replace("\n", "").replace("\t", "") for t in raw_titles]
    processed_artists = [a.replace("\n", "").replace("\t", "") for a in raw_artists]

    return processed_titles, processed_artists


def check_date(date_str: str) -> bool:
    """Checks if date format is correct and if date <= today"""
    wrong_format_msg = "Wrong date format. Must be -> YYYY-MM-DD"
    # Date to int
    try:
        ymd = [int(i) for i in date_str.split("-")]
    except ValueError:
        print(wrong_format_msg)
        return False
    # Check that we got three values
    if len(ymd) != 3:
        print(wrong_format_msg)
        return False
    # Check date format is valid
    try:
        date_obj = datetime.date(year=ymd[0], month=ymd[1], day=ymd[2])
    except ValueError as e:
        print(e)
        return False

    today = datetime.date.today()
    # A future date is not allowed
    if date_obj > today:
        print("Input date can't be higher than current date")
        return False
    # Everything is OK
    return True


if __name__ == "__main__":
    date = input("Enter date YYYY-MM-DD: ")
    if check_date(date):
        songs, artists = get_billboard_songs_artists(date)

        spotify = get_spotify_client()
        user_id = spotify.me()["id"]
        playlist_name = "Top 100. " + date

        playlist_id = get_playlist(spotify, user_id, playlist_name)

        if playlist_id != 0:  # Playlist didn't exist
            song_uris = get_song_uris(spotify, songs, artists)
            spotify.playlist_add_items(playlist_id, song_uris)
        else:
            print("That playlist already existed.")
