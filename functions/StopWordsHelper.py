from nltk.corpus import stopwords


def stop_words(text: str) -> list:
    english_stop_words = set(stopwords.words('english'))
    return [word for word in text if word not in english_stop_words]