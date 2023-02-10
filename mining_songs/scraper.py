import re
import requests

from bs4 import BeautifulSoup

GENIUS_URL = "https://genius.com"


class Scraper:
    def __init__(self, songs_urls_dict: str, language: str) -> None:
        self.language = language
        self.songs_urls_dict = songs_urls_dict

    def get_artist_lyrics(self) -> dict:
        self.lyrics_dict = {
            title: self.__extract_lyrics(song_url)
            for title, song_url in self.songs_urls_dict.items()
        }
        dict_to_save = {"language": self.language, "lyrics": self.lyrics_dict}
        return dict_to_save

    def __create_soup_object(self, url: str) -> BeautifulSoup:
        target_url = GENIUS_URL + url
        response = requests.get(target_url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    def __extract_lyrics(self, url: str) -> str:
        soup = self.__create_soup_object(url)
        found_divs = soup.find_all(
            "div",
            {
                "class": "Lyrics__Container-sc-1ynbvzw-6 YYrds",
                "data-lyrics-container": "true",
            },
        )

        for div in found_divs:
            for i in div("i"):
                i.unwrap()
            for b in div("b"):
                b.unwrap()
        song_lyrics = "".join([div.get_text("\r\n") for div in found_divs])
        song_lyrics = self.remove_brackets(song_lyrics)
        return song_lyrics

    @staticmethod
    def remove_brackets(lyrics: str) -> str:
        lyrics = re.sub(r"\r\n\]", "]", lyrics)
        lyrics = re.sub(r"\[.*\]", "", lyrics)
        lyrics = re.sub(r"\[.*", "", lyrics)
        lyrics = re.sub(r".*\]", "", lyrics)
        lyrics = re.sub(r"\r\n\)", ")", lyrics)
        lyrics = re.sub(r"\(.*\)", "", lyrics)
        return lyrics
