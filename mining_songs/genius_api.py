import os
import json
import pprint
import requests

ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")


class GeniusAPI:
    base_url = "https://api.genius.com"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    def __init__(self) -> None:
        pass

    def find_artist(self, artist_name: str) -> tuple[str, str]:
        search_endpoint = "/search"
        params = {"q": artist_name}
        r = requests.get(
            url=self.base_url + search_endpoint, headers=self.headers, params=params
        )
        print(r.url)
        found_artist_name = r.json()["response"]["hits"][0]["result"]["primary_artist"][
            "name"
        ]
        artist_api_path = r.json()["response"]["hits"][0]["result"]["primary_artist"][
            "api_path"
        ]

        return found_artist_name, artist_api_path

    def get_artist_albums(self, artist_url):
        search_endpoint = "/albums"
        r = requests.get(
            url="https://genius.com/api" + artist_url + search_endpoint,
            headers=self.headers,
        )
        print(r.url)
        pprint.pprint(r.json())
