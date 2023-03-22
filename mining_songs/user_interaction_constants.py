from dataclasses import dataclass, field
from itertools import count


@dataclass
class MenuItem:
    id: int = field(init=False, default_factory=count().__next__)
    function_name: str
    human_readable_name: str
    library_choice: bool = False
    amount_by_user: bool = False


def get_menu_items() -> list:
    menu_items = []
    for i in READABLE_NAMES_LIST:
        item = MenuItem(function_name=i[0], human_readable_name=i[1])


MOST_FREQUENT_WORDS_FUNC_NAME = "get_most_frequent_words"
WORDS_LENGTH_PIE_CHART_FUNC_NAME = "create_words_lengths_pie_chart"
WORD_CLOUD_FUNC_NAME = "create_word_cloud"
GET_SENTIMENT_FUNC_NAME = "get_sentiment"
FREQUENCY_BAR_PLOT_FUNC_NAME = "create_frequency_bar_plot"
MOST_SIGNIFICANT_WORDS_FUNC_NAME = "get_most_significant_words"
WORDS_APPEARING_TOGETHER_FUNC_NAME = "get_words_appearing_together"
UNIQUE_WORDS_FUNC_NAME = "get_unique_words_amount"
WORDS_CONTEXT_FUNC_NAME = "get_word_contexts"
PERCENT_STOPWORDS_FUNC_NAME = "get_percent_of_stopwords"
NAMED_ENTITIES_FUNC_NAME = "get_named_entities"

MENU_ITEMS = [
    MenuItem(
        function_name="get_most_frequent_words",
        human_readable_name="Show most frequent words",
        library_choice=True,
        amount_by_user=True,
    ),
    MenuItem(
        function_name="create_words_lengths_pie_chart",
        human_readable_name="Show most frequent words",
        library_choice=True,
        amount_by_user=True,
    ),
    MenuItem(
        WORDS_LENGTH_PIE_CHART_FUNC_NAME,
        "Create pie chart with word lenghts",
        False,
        True,
    ),
    (WORD_CLOUD_FUNC_NAME, "Create world cloud"),
    (GET_SENTIMENT_FUNC_NAME, "Show sentiment of artist's songs"),
    (FREQUENCY_BAR_PLOT_FUNC_NAME, "Create bar plot with most frequent words"),
    (MOST_SIGNIFICANT_WORDS_FUNC_NAME, "Show the most significant words"),
    (WORDS_APPEARING_TOGETHER_FUNC_NAME, "Show words that appear together the most"),
    (UNIQUE_WORDS_FUNC_NAME, "Show amount of unique words"),
    (WORDS_CONTEXT_FUNC_NAME, "Show contextes of some word"),
    (PERCENT_STOPWORDS_FUNC_NAME, "Show how many % of words are stopwords"),
    (NAMED_ENTITIES_FUNC_NAME, "Show the list of appearing named entities"),
]

READABLE_NAMES_LIST = [
    (MOST_FREQUENT_WORDS_FUNC_NAME, "Show most frequent words"),
    (WORDS_LENGTH_PIE_CHART_FUNC_NAME, "Create pie chart with word lenghts"),
    (WORD_CLOUD_FUNC_NAME, "Create world cloud"),
    (GET_SENTIMENT_FUNC_NAME, "Show sentiment of artist's songs"),
    (FREQUENCY_BAR_PLOT_FUNC_NAME, "Create bar plot with most frequent words"),
    (MOST_SIGNIFICANT_WORDS_FUNC_NAME, "Show the most significant words"),
    (WORDS_APPEARING_TOGETHER_FUNC_NAME, "Show words that appear together the most"),
    (UNIQUE_WORDS_FUNC_NAME, "Show amount of unique words"),
    (WORDS_CONTEXT_FUNC_NAME, "Show contextes of some word"),
    (PERCENT_STOPWORDS_FUNC_NAME, "Show how many % of words are stopwords"),
    (NAMED_ENTITIES_FUNC_NAME, "Show the list of appearing named entities"),
]

FUNCTIONS_WITH_LIBRARY_CHOICE = (
    MOST_FREQUENT_WORDS_FUNC_NAME,
    WORD_CLOUD_FUNC_NAME,
    FREQUENCY_BAR_PLOT_FUNC_NAME,
)

FUNCTIONS_WITH_NUMBER_FROM_USER = (
    MOST_FREQUENT_WORDS_FUNC_NAME,
    WORDS_LENGTH_PIE_CHART_FUNC_NAME,
    FREQUENCY_BAR_PLOT_FUNC_NAME,
    MOST_SIGNIFICANT_WORDS_FUNC_NAME,
    WORDS_APPEARING_TOGETHER_FUNC_NAME,
    WORDS_CONTEXT_FUNC_NAME,
)
