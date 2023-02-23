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


def get_most_frequent_words(tokens: list) -> dict:
    stemmer = SnowballStemmer("english")
    tokens = [word.lower() for word in tokens if word.isalpha()]
    stemmed_words = [
        stemmer.stem(word) for word in tokens if word not in stopwords.words("english")
    ]
    fdist = FreqDist(stemmed_words)
    return dict(fdist)


def get_song_sentiment(lyrics: str) -> dict:
    sentiment_analyzer = SentimentIntensityAnalyzer()
    return sentiment_analyzer.polarity_scores(lyrics)
