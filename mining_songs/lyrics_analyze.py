import nltk_services
import os
import wordcloud
from dataclasses import dataclass

from data_managing import get_artist_lyrics, DATA_PATH


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
