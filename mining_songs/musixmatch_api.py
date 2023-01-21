import os
import pprint
import requests

API_KEY = os.getenv("MUSIXMATCH_API_KEY")


class MusixmatchAPI:
    base_url = "https://api.musixmatch.com/ws/1.1/"

    def find_artist(self, artist_name: str):
        search_endpoint = "artist.search"
        print(API_KEY)
        params = {"apikey": API_KEY, "q_artist": artist_name}

        r = requests.get(url=self.base_url + search_endpoint, params=params)
        print(r.url)
        pprint.pprint(r.json())

        return "essa", "essa"

    def find_song(self, song_name: str):
        search_endpoint = "track.search"
        print(API_KEY)
        params = {"apikey": API_KEY, "q_track": song_name, "q_artist": "Mac Miller"}

        r = requests.get(url=self.base_url + search_endpoint, params=params)
        print(r.url)
        pprint.pprint(r.json())

        return "essa", "essa"

    def find_lyrics(self, track_id=153437944):
        search_endpoint = "track.lyrics.get"
        print(API_KEY)
        params = {"apikey": API_KEY, "track_id": "153437944"}

        r = requests.get(url=self.base_url + search_endpoint, params=params)
        # print(r.url)
        pprint.pprint(r.json())
        print(r.json()["message"]["body"]["lyrics"]["lyrics_body"])

        return "essa", "essa"
