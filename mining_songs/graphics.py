import os
import wordcloud
import matplotlib.pyplot as plt

from data_managing import DATA_PATH


def create_bar_plot(data: dict, artist_name: str, title: str, which_lib: str):
    plt.barh(list(data.keys()), list(data.values()))
    plt.title(title)
    plot_path = os.path.join(DATA_PATH, artist_name, f"{title}_bar_plot{which_lib}.png")
    plt.savefig(plot_path)
    plt.clf()


def create_pie_chart(data: dict, artist_name: str, title: str):
    labels = [f"{words_length} characters" for words_length in data.keys()]
    labels.append("other")
    values = [percent * 100 for percent in data.values()]
    others_percent = 100 - sum(values)
    values.append(others_percent)
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    fig.suptitle(title)
    chart_path = os.path.join(DATA_PATH, artist_name, f"{title}_pie_chart.png")
    fig.savefig(chart_path)


def create_word_cloud(frequency_dict: dict, which_lib: str, artist_name: str):
    word_cloud = wordcloud.WordCloud(width=800, height=800).generate_from_frequencies(
        frequency_dict
    )
    word_cloud.to_file(
        os.path.join(DATA_PATH, artist_name, f"{which_lib}_lyrics_word_cloud.png")
    )
