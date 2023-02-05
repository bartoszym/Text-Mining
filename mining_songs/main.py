from genius_api import GeniusAPI
from data_managing import *
from scraper import Scraper


def find_artist(api: GeniusAPI):
    artist_name = input("Please provide artist name: ")
    found_name, api_path = api.find_artist(artist_name)
    is_found_name_good = input(
        f"""Is found name "{found_name}" the artist you are looking for?"""
    )

    if is_found_name_good:
        print("essa")

    return found_name, api_path


def main():
    api = GeniusAPI()
    artist_name, artist_api_path = find_artist(api)
    # if not is_artist_dir_exists(artist_name):
    songs_urls = api.get_artist_songs_urls(artist_api_path)
    scraper = Scraper(songs_urls)
    scraper.get_artist_lyrics()

    print(is_artist_dir_exists(artist_name))
    create_artist_directory(artist_name)


if __name__ == "__main__":
    main()
