from sklearn.tree import DecisionTreeClassifier
from preprocessing import X_train, y_train, X_test, y_test
import sklearn.metrics as metrics

classifier = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=2)
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