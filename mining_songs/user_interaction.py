from lyrics_analyze import Artist

MENU_ELEMENTS_DICT = [
    ("get_most_frequent_words", "Show most frequent words"),
    ("create_words_lengths_pie_chart", "Create pie chart with word lenghts")(
        "create_word_cloud", "Create world cloud"
    ),
    ("get_sentiment", "Show sentiment of artist's songs"),
    ("create_frequency_bar_plot", "Create bar plot with most frequent words"),
    ("get_most_significant_words", "Show the most significant words"),
    ("get_words_appearing_together", "Show words that appear together the most"),
    ("get_unique_words_amount", "Show amount of unique words"),
    ("get_word_contexts", "Show contextes of some word"),
    ("get_percent_of_stopwords", "Show how many % of words are stopwords"),
    ("get_named_enntities", "Show the list of appearing named entities"),
]


def menu(artist_name: str):
    artist = Artist(artist_name)
    while True:
        for i, menu_position in enumerate(MENU_ELEMENTS_DICT, start=1):
            print(f"{i}: {menu_position[1]}")
        selection = input("Type number of the menu item: ")
        getattr(artist, MENU_ELEMENTS_DICT[selection][0]("nltk", 5))

        # selection
