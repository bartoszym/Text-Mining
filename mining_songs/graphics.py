import os
import wordcloud
import matplotlib.pyplot as plt

from data_managing import DATA_PATH


def create_bar_plot(frequency_dict: dict, artist_name: str):
    plt.barh(list(frequency_dict.keys()), list(frequency_dict.values()))
    plt.title(f"{artist_name}'s most used words")
    plot_path = os.path.join(DATA_PATH, artist_name, "bar_plot.png")
    plt.savefig(fname=plot_path)


def create_word_cloud(frequency_dict: dict, artist_name: str):
    word_cloud = wordcloud.WordCloud(width=800, height=800).generate_from_frequencies(
        frequency_dict
    )
    word_cloud.to_file(os.path.join(DATA_PATH, artist_name, "lyrics_word_cloud.png"))
