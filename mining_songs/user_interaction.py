from lyrics_analyze import Artist
from mining_songs.menu_items import MENU_ITEMS


def menu(artist_name: str):
    artist = Artist(artist_name)
    while True:
        print(MENU_ITEMS)
        for i in MENU_ITEMS:
            print(f"{i.id + 1}: {i.human_readable_name}")
        selection = input("Type number of the menu item: ")
        chosen_item = MENU_ITEMS[selection - 1]
        if chosen_item.library_choice:
            selected_library = input("Choose library:\n 1. NLTK \n 2. SpaCy")
            if selected_library not in (1, 2):
                raise ValueError("Wrong value chosen")
        if chosen_item.amount_by_user:
            amount = int(input("Choose amount of words that will be provided: "))

        getattr(artist, chosen_item.function_name(selected_library, amount))
