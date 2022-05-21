from CsvReader import read_csv
from sklearn.model_selection import train_test_split
from TextTokenizer import prepared_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics

file = read_csv("spam.csv")

vectorizer = CountVectorizer(tokenizer=prepared_text)
file_vectorizer = vectorizer.fit_transform(file['v2'])

x_train, x_test, y_train, y_test = train_test_split(file_vectorizer, file['v1'], test_size=0.20)

classifiers = [DecisionTreeClassifier(),RandomForestClassifier(),LinearSVC(),AdaBoostClassifier(),BaggingClassifier()]

for classifier in classifiers:
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    print(f"{classifier} - Accuracy: {round(metrics.accuracy_score(y_test,y_pred)*100,2)}%")
