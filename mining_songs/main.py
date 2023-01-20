from genius_api import GeniusAPI


def find_artist(api: GeniusAPI):
    artist_name = input("Please provide artist name: ")
    found_name, api_path = api.find_artist(artist_name)
    is_found_name_good = input(
        f"""Is found name "{found_name}" the artist you are looking for?"""
    )

    if is_found_name_good:
        print("essa")

    return found_name, api_path


def interacting_with_user():
    api = GeniusAPI()
    artist_name, artist_api_path = find_artist(api)


if __name__ == "__main__":
    interacting_with_user()
