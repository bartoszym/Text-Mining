import os
import requests

ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")


class GeniusAPI:
    base_url = "https://api.genius.com"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    def __init__(self) -> None:
        pass

    def find_artist(self, artist_name: str) -> tuple[str, str, str]:
        search_endpoint = "/search"
        url = self.base_url + search_endpoint
        params = {"q": artist_name}
        response_json = requests.get(
            url=url, headers=self.headers, params=params
        ).json()
        found_artist_name = response_json["response"]["hits"][0]["result"][
            "primary_artist"
        ]["name"]
        artist_api_path = response_json["response"]["hits"][0]["result"][
            "primary_artist"
        ]["api_path"]
        artist_id = response_json["response"]["hits"][0]["result"]["primary_artist"][
            "id"
        ]

        return found_artist_name, artist_api_path, artist_id

    def get_artist_songs_urls(
        self, artist_api_path: str, artist_id: int
    ) -> tuple[list, str]:
        url = self.base_url + artist_api_path + "/songs"
        params = {"sort": "popularity"}
        response_json = requests.get(
            url=url, headers=self.headers, params=params
        ).json()
        songs_urls = {
            song["title"]: song["path"]
            for song in response_json["response"]["songs"]
            if song["primary_artist"]["id"] == artist_id
        }
        language = response_json["response"]["songs"][0]["language"]
        return songs_urls, language