# Naiwny klasyfikator bayesowski
from sklearn.naive_bayes import GaussianNB
import sklearn.metrics as metrics
from preprocessing import X_test, X_train, y_train, y_test

classifier = GaussianNB()
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



