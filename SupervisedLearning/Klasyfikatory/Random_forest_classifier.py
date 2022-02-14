# Łączy ze sobą kilka drzew decyzyjnych
from sklearn.ensemble import RandomForestClassifier
from preprocessing import X_train, y_train, X_test, y_test
import sklearn.metrics as metrics

classifier = RandomForestClassifier(n_estimators=10, max_depth=4, criterion="entropy", random_state=0)
classifier.fit(X_train, y_train)

# Tworzymy predykcje
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