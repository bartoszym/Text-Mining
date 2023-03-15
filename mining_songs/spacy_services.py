import spacy

from collections import Counter


def lemmatizer_lookup(lyrics: str) -> spacy.tokens.doc.Doc:
    nlp = spacy.load("en_core_web_sm", exclude=["lemmatizer"])
    config = {"mode": "lookup", "overwrite": True}
    nlp.add_pipe("lemmatizer", config=config)
    nlp.initialize()


def most_frequent_words(lyrics: str, top_n_words: int = None) -> dict:
    nlp = spacy.load(
        "en_core_web_sm", enable=["tagger", "attribute_ruler", "lemmatizer"]
    )
    doc = nlp(lyrics)
    cleaned_lyrics2 = [
        token.lemma_ for token in doc if not (token.is_stop or not token.is_alpha)
    ]
    freq_dist = Counter(cleaned_lyrics2)
    return dict(freq_dist.most_common(top_n_words))
