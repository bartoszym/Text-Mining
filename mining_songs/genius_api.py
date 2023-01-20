import os
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
        found_artist_name = r.json()["response"]["hits"][0]["result"]["primary_artist"][
            "name"
        ]
        artist_api_path = r.json()["response"]["hits"][0]["result"]["primary_artist"][
            "api_path"
        ]

        return found_artist_name, artist_api_path
