from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from functions.TextPreparation import prepared_text
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
from functions.CsvReader import read_csv

file = read_csv("alexa_reviews.csv")


def visual() -> None:
    vectorizer = CountVectorizer(tokenizer=prepared_text)
    file_vectorizer = vectorizer.fit_transform(file['verified_reviews'])

    x_train, x_test, y_train, y_test = train_test_split(file_vectorizer, file['rating'], test_size=0.20)

    classifiers = [DecisionTreeClassifier(), RandomForestClassifier(), LinearSVC(), AdaBoostClassifier(),
                   BaggingClassifier()]

    for classifier in classifiers:
        classifier.fit(x_train, y_train)
        y_pred = classifier.predict(x_test)
        print(f"{classifier} - Accuracy: {round(metrics.accuracy_score(y_test, y_pred) * 100, 2)}%")
