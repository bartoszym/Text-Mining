import spacy

from collections import Counter, defaultdict

LANGUAGES_PACKAGES = {"en": "en_core_web_sm", "pl": "pl_core_news_sm"}


def lemmatizer_lookup(lyrics: str) -> spacy.tokens.doc.Doc:
    language_package = LANGUAGES_PACKAGES[kwargs["language"]]
    nlp = spacy.load(language_package, exclude=["lemmatizer"])
    config = {"mode": "lookup", "overwrite": True}
    nlp.add_pipe("lemmatizer", config=config)
    nlp.initialize()


def most_frequent_words(lyrics: str, top_n_words: int = None, **kwargs) -> dict:
    language_package = LANGUAGES_PACKAGES[kwargs["language"]]
    nlp = spacy.load(
        language_package, enable=["tagger", "attribute_ruler", "lemmatizer"]
    )
    doc = nlp(lyrics)
    cleaned_lyrics = [
        token.lemma_ for token in doc if not (token.is_stop or not token.is_alpha)
    ]
    freq_dist = Counter(cleaned_lyrics)
    return dict(freq_dist.most_common(top_n_words))


def get_NERS(lyrics: str, **kwargs):
    interesting_entities = {
        "en": (
            "PERSON",
            "GPE",
            "ORG",
            "NORP",
            "MONEY",
            "WORK_OF_ART",
            "LOC",
            "PRODUCT",
        ),
        "pl": ("date", "geogName", "orgName", "persName", "placeName", "time"),
    }
    language_package = LANGUAGES_PACKAGES[kwargs["language"]]
    breakpoint()
    nlp = spacy.load(language_package)
    NER_dict = defaultdict(set)
    doc = nlp(lyrics)

    for ent in doc.ents:
        if ent.label_ in interesting_entities[kwargs["language"]]:
            NER_dict[ent.label_].add(ent.text)
    return NER_dict


# def get_POS(lyrics: str):
#     nlp = spacy.load("en_core_web_sm")
#     POS_dict = defaultdict(defaultdict(0))
#     doc = nlp(lyrics)
#     for token in doc:
#         POS_dict[token.pos_] =
