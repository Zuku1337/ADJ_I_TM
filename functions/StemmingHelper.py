from nltk.stem import PorterStemmer


def stemming(text: str) -> list:
    ps = PorterStemmer()
    x = []
    for word in text:
        x.append(ps.stem(word))
    return x