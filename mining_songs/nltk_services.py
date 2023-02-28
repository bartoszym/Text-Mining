import re

from nltk.text import Text
from nltk.tokenize import word_tokenize, WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer


def get_tokenized_text_whitespace(lyrics: str) -> list:
    whitespace_tokenizer = WhitespaceTokenizer()
    sth = whitespace_tokenizer.tokenize(lyrics)
    return sth


def get_tokenized_text(lyrics: str) -> list:
    return word_tokenize(lyrics)


def get_most_frequent_words(tokens: list, top_n_words: int = None) -> dict:
    stemmer = SnowballStemmer("english")
    tokens = [word.lower() for word in tokens if word.isalpha()]
    stemmed_words = [
        stemmer.stem(word) for word in tokens if word not in stopwords.words("english")
    ]
    fdist = FreqDist(stemmed_words)
    return dict(fdist.most_common(top_n_words))


def get_song_sentiment(lyrics: str) -> dict:
    sentiment_analyzer = SentimentIntensityAnalyzer()
    return sentiment_analyzer.polarity_scores(lyrics)


def get_collocation_words(lyrics: str, n_pairs: int) -> list:
    cleared_lyrics = re.sub(r"[',-]", "", lyrics)
    tokens = get_tokenized_text(cleared_lyrics)
    lyrics_text = Text(tokens)
    return lyrics_text.collocation_list(num=n_pairs)
