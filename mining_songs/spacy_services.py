import spacy

from collections import Counter, defaultdict


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
    cleaned_lyrics = [
        token.lemma_ for token in doc if not (token.is_stop or not token.is_alpha)
    ]
    freq_dist = Counter(cleaned_lyrics)
    return dict(freq_dist.most_common(top_n_words))


def get_NERS(lyrics: str):
    nlp = spacy.load("en_core_web_sm")
    NER_dict = defaultdict(set)
    doc = nlp(lyrics)
    interesting_entities = (
        "PERSON",
        "GPE",
        "ORG",
        "NORP",
        "MONEY",
        "WORK_OF_ART",
        "LOC",
        "PRODUCT",
    )
    for ent in doc.ents:
        if ent.label_ in interesting_entities:
            NER_dict[ent.label_].add(ent.text)
    return NER_dict


def get_POS(lyrics: str):
    nlp = spacy.load("en_core_web_sm")
    POS_dict = defaultdict(defaultdict(0))
    doc = nlp(lyrics)
    for token in doc:
        POS_dict[token.pos_] = 
