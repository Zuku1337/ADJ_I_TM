import CsvReader
from prettytable import PrettyTable
import sklearn.feature_extraction.text
from TextPreparation import prepared_text
import matplotlib.pyplot as plt
import numpy as np

file = CsvReader.read_csv("spam.csv")


def visual() -> None:
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(tokenizer=prepared_text)
    transform = vectorizer.fit_transform(file['v2'])
    sum_list = transform.toarray().sum(axis=0)
    count = -np.sort(-sum_list)[:10]
    words = vectorizer.get_feature_names_out()[-np.argsort(-sum_list)[:10]]

    plt.subplots(figsize=(10, 5))
    plt.bar(words, count, width=0.7, color='blue')
    plt.title('Top 10 najczęściej występujących tokenów')
    plt.show()

    columns = ["Words", "Count"]
    matrix = PrettyTable()
    matrix.add_column(columns[0], words)
    matrix.add_column(columns[1], count)
    print(matrix)

    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=prepared_text)
    X_transform = vectorizer.fit_transform(file['v2'])
    sum_list = X_transform.toarray().sum(axis=1)
    countTFIDF = -np.sort(-sum_list).round(2)[:10]
    wordsTFIDF = vectorizer.get_feature_names_out()[-np.argsort(-sum_list)[:10]]

    plt.subplots(figsize=(11, 5))
    plt.bar(wordsTFIDF, countTFIDF, width=0.8, color='blue')
    plt.title("Top 10 najważniejszych tokenów")
    plt.show()
    print()

    matrix = PrettyTable()
    matrix.add_column("Words TFIDF", wordsTFIDF)
    matrix.add_column("Count TFIDF", countTFIDF)
    print(matrix)

    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=prepared_text)
    X_transform = vectorizer.fit_transform(file['v2'])
    z4 = X_transform.toarray().sum(axis=1)
    copy_z4 = z4.copy()
    numbers = []
    for i in range(10):
        index = np.argmax(copy_z4)
        numbers.append(index)
        copy_z4[index] = 0
    words = vectorizer.get_feature_names_out()[numbers]

    plt.subplots(figsize=(16, 5))
    plt.bar(words, numbers, width=0.5)
    plt.title("Top 10 dokumentów zawierających najwięcej tokenów")
    plt.show()
    print()
