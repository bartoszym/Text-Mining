import nltk_services
import os
import wordcloud
from dataclasses import dataclass

from data_managing import get_artist_lyrics, DATA_PATH
from utils import progress_bar


@dataclass
class Song:
    title: str
    lyrics: str
    tokenized_lyrics: str


class Artist:
    def __init__(self, artist_name: str) -> None:
        self.artist_name = artist_name
        self.language, lyrics_dict = get_artist_lyrics(artist_name)
        self.songs = []
        for title, lyrics in lyrics_dict.items():
            tokenized_lyrics = nltk_services.get_tokenized_text(
                lyrics
            )  # TODO is it necessary? definietely to rethink
            self.songs.append(Song(title, lyrics, tokenized_lyrics))

    def most_frequent_words(self) -> dict:
        tokens = []
        for song in self.songs:
            tokens.extend(song.tokenized_lyrics)
        return nltk_services.get_most_frequent_words(tokens)

    def create_word_cloud(self):
        frequency_distribution = self.most_frequent_words()
        word_cloud = wordcloud.WordCloud(
            width=800, height=800
        ).generate_from_frequencies(frequency_distribution)
        word_cloud.to_file(
            os.path.join(DATA_PATH, self.artist_name, "lyrics_word_cloud.png")
        )

    def get_sentiment(self) -> dict:
        sentiment_dict = {
            "overall": {
                "neg": 0,
                "neu": 0,
                "pos": 0,
                "compound": 0,
            },
            "most_neg": {"score": 0, "title": "", "compound": 0},
            "most_pos": {"score": 0, "title": "", "compound": 0},
        }

        def check_highest_sentiments(
            sentiment_dict: dict, song_sentiment: dict
        ) -> dict:
            for i in ["pos", "neg"]:
                if song_sentiment[i] > sentiment_dict[f"most_{i}"]["score"]:
                    sentiment_dict[f"most_{i}"]["score"] = song_sentiment[i]
                    sentiment_dict[f"most_{i}"]["title"] = song.title
                    sentiment_dict[f"most_{i}"]["compound"] = song_sentiment["compound"]
            return sentiment_dict

        for counter, song in enumerate(self.songs):
            progress_bar(counter, len(self.songs))
            song_sentiment = nltk_services.get_song_sentiment(song.lyrics)
            for key in sentiment_dict["overall"].keys():
                sentiment_dict["overall"][key] += song_sentiment[key]
            sentiment_dict = check_highest_sentiments(sentiment_dict, song_sentiment)

        for key in sentiment_dict["overall"].keys():
            sentiment_dict["overall"][key] /= len(self.songs)
        print(
            f"The most positive song is {sentiment_dict['most_pos']['title']} with {sentiment_dict['most_pos']['score']} score. Compound: {sentiment_dict['most_pos']['compound']}"
        )
        print(
            f"The most negative song is {sentiment_dict['most_neg']['title']} with {sentiment_dict['most_neg']['score']} score. Compound: {sentiment_dict['most_neg']['compound']}"
        )
        return sentiment_dict
