import numpy as np
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Klasyfikatory
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

# Pobieramy dane z pliku tsv
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter='\t', quoting=3)

corpus = []

# Dla każdej oceny:
# Usuwamy niepotrzebne znaki (kropki, przecinki, itd.)
# Zamieniamy wszystko na małe litery
# Wykonujemy stemming (zamieniamy slowa na jedna forme)
# Łaczymy wszystko w jedni zdanie.
# Powstaje lista przetworzonych już zdań.
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# Zamiana na macierz cech
# Każdy wiersz to wektor cech dla danej recenzji.
cv = CountVectorizer(max_features=1500)

X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Uzycie Naive Gaussian Classifier 

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
# print("Macierz pomyłek: ", confusion_matrix(y_test, y_pred))
print("Klasyfikator Gausowski")
print("Dokładność : ", accuracy_score(y_test, y_pred))
print("Czulosc: ", precision_score(y_test, y_pred))
print()


# Uzycie Drzewa Decyzyjnego
classifier = DecisionTreeClassifier(criterion="entropy", random_state=50, max_depth=4)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
# print("Macierz pomyłek: ", confusion_matrix(y_test, y_pred))
print("Drzewo Decyzyjne")
print("Dokładność : ", accuracy_score(y_test, y_pred))
print("Czulosc: ", precision_score(y_test, y_pred))
print()


# Uzycie klasyfikatora Random Forest
classifier = RandomForestClassifier(n_estimators=10, max_depth=4, criterion="entropy", random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
# print("Macierz pomyłek: ", confusion_matrix(y_test, y_pred))
print("Random Forest")
print("Dokładność : ", accuracy_score(y_test, y_pred))
print("Czulosc: ", precision_score(y_test, y_pred))
print()