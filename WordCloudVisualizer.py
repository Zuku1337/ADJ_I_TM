from functions import CsvReader
from functions.TextPreparation import prepared_text, words_bag_helper
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = CsvReader.read_csv("alexa_reviews.csv")


def visual() -> None:
    text = ""
    for i in range(len(file['verified_reviews']))[:400]:
        text += file['verified_reviews'].iloc[i]
        text_wordcloud = prepared_text(text)
        bow = words_bag_helper(text_wordcloud)

    wc = WordCloud()
    wc.generate_from_frequencies(bow)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()