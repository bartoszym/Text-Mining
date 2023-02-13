from genius_api import GeniusAPI
from data_managing import *
from lyrics_analyze import Artist
from scraper import Scraper

from typing import Union


def get_artist_data(api: GeniusAPI) -> Union[str, str, str]:
    artist_name = input("Please provide artist name: ")
    found_name, api_path, artist_id = api.find_artist(artist_name)
    is_found_name_good = input(
        f"""Is found name "{found_name}" the artist you are looking for?"""
    )

    if is_found_name_good:
        print("essa")

    return found_name, api_path, artist_id


def prepare_data() -> str:
    api = GeniusAPI()
    artist_name, artist_api_path, artist_id = get_artist_data(api)
    if not artist_dir_exists(artist_name):
        songs_urls_dict, language = api.get_artist_songs_urls(
            artist_api_path, artist_id
        )
        scraper = Scraper(songs_urls_dict, language)
        create_artist_directory(artist_name)
        save_lyrics_json(scraper.get_artist_lyrics(), artist_name)

    return artist_name


def main():
    artist_name = prepare_data()
    artist = Artist(artist_name)
    artist.create_word_cloud()


if __name__ == "__main__":
    main()
