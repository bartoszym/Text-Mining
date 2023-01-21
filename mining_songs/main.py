from musixmatch_api import MusixmatchAPI


def find_artist(api: MusixmatchAPI):
    artist_name = input("Please provide artist name: ")
    found_name, api_path = api.find_artist(artist_name)

    return found_name, api_path


def find_song(api: MusixmatchAPI):
    song_name = input("Please provide song name: ")
    found_name, api_path = api.find_song(song_name)

    return found_name, api_path


def interacting_with_user():
    api = MusixmatchAPI()
    _, _ = api.find_lyrics()


if __name__ == "__main__":
    interacting_with_user()
