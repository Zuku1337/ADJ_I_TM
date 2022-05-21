import CsvReader
from TextPreparation import prepared_text, words_bag_helper
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = CsvReader.read_csv("spam.csv")


def visual() -> None:
    text = ""
    for i in range(len(file['v2']))[:400]:
        text += file['v2'].iloc[i]
        text_wordcloud = prepared_text(text)
        bow = words_bag_helper(text_wordcloud)

    wc = WordCloud()
    wc.generate_from_frequencies(bow)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
