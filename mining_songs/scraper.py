import requests

from bs4 import BeautifulSoup

GENIUS_URL = "https://genius.com"


class Scraper:
    def __init__(self, songs_urls: str) -> None:
        self.songs_urls = songs_urls

    def open_url(self, url: str):
        target_url = GENIUS_URL + url
        sth = requests.get(target_url)
        print(sth.text)

    def get_artist_lyrics(self):
        for song_url in self.songs_urls:
            self.open_url(song_url)
