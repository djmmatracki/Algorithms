"""
Kiedy używać regresji logistycznej?

Sprawdza się znakomicie w przypadku binarnych klasyfikatorów.
Nie będzie jednak działać dobrze gdy zbiór danych jest bardzo duży.
Algorytm nie jest w stanie wychwycić relacji które są szczególnie złożone.
"""
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as metrics
from preprocessing import X_train, X_test, y_train, y_test

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Tablica pomyłek
cm = metrics.confusion_matrix(y_test, y_pred)

# Dokladność
accuracy = metrics.accuracy_score(y_test, y_pred)

# Czułość
recall = metrics.recall_score(y_test, y_pred)

# Precyzja
precision = metrics.precision_score(y_test, y_pred)

print(accuracy, recall, precision)
