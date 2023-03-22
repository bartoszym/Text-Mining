from lyrics_analyze import Artist
from user_interaction_constants import (
    READABLE_NAMES_LIST,
    FUNCTIONS_WITH_LIBRARY_CHOICE,
    FUNCTIONS_WITH_NUMBER_FROM_USER,
    MENU_ITEMS,
)


def menu(artist_name: str):
    artist = Artist(artist_name)
    while True:
        print(MENU_ITEMS)
        for i in MENU_ITEMS:
            print(f"{i.id + 1}: {i.human_readable_name}")
        # for i, menu_position in enumerate(READABLE_NAMES_LIST, start=1):
        #     print(f"{i}: {menu_position[1]}")
        selection = input("Type number of the menu item: ")
        chosen_func_name = READABLE_NAMES_LIST[selection - 1][0]

        getattr(artist, READABLE_NAMES_LIST[selection][0]("nltk", 5))

        # selection
