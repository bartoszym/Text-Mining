import os

DATA_PATH = os.getenv("DATA_DIRECTORY_PATH")


def is_artist_dir_exists(artist_name: str) -> bool:
    dir_list = os.listdir(DATA_PATH)
    dir_list_lowered = [dir_name.lower() for dir_name in dir_list]
    for dir_name in dir_list_lowered:
        if artist_name.lower() == dir_name:
            return True
    return False


def create_artist_directory(artist_name: str):
    new_directory = os.path.join(DATA_PATH, artist_name)
    try:
        os.mkdir(new_directory)
    except FileExistsError:
        print("Directory for the artist already exists")
