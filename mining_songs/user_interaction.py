from lyrics_analyze import Artist
from menu_items import MENU_ITEMS


def select_library(LIBRARY_DICT: dict):
    while True:
        selected_library = int(input("Choose library:\n 1. NLTK \n 2. SpaCy\n"))
        if selected_library in LIBRARY_DICT.keys():
            return selected_library
        print(f"Chosen value has to be {LIBRARY_DICT.keys()}")


def menu(artist_name: str):
    LIBRARY_DICT = {1: "nltk", 2: "spacy"}
    artist = Artist(artist_name)
    while True:
        for i in MENU_ITEMS:
            print(f"{i.id + 1}: {i.human_readable_name}")
        selection = int(input("Type number of the menu item: "))
        chosen_item = MENU_ITEMS[selection - 1]
        if chosen_item.function_name == "get_word_contexts":
            chosen_word = input("Type word that you want to get contexts for: ")
            chosen_amount = int(
                input("Type how many lines of contexts you want to see: ")
            )
            chosen_line_length = int(
                input("Type how long should be the lines with contexts: ")
            )
            artist.get_word_contexts(chosen_word, chosen_amount, chosen_line_length)
            continue

        selected_library, amount = None, None
        if chosen_item.library_choice:
            selected_library = select_library(LIBRARY_DICT)
        if chosen_item.amount_by_user:
            amount = int(input("Choose amount of words that will be provided: "))

        selected_by_user = {
            "which_lib": LIBRARY_DICT[selected_library] if selected_library else None,
            "amount": amount,
        }
        params = {
            key: value for key, value in selected_by_user.items() if value is not None
        }
        function_result = getattr(artist, chosen_item.function_name)(**params)
        print(function_result)
