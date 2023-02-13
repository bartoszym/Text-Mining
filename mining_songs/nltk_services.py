from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


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
