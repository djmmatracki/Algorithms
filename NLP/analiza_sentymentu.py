import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Model do klasyfikacji opini klientow


df = pd.read_csv("IMDB_Dataset.csv")

# Replace sentiment on digits
# df.loc[df['sentiment'] == "positive", 'sentiment'] = 1
# df.loc[df['sentiment'] == "negative", 'sentiment'] = 0

df.dropna(inplace=True)


X = df['review']
y = df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()), ('clf', MultinomialNB())])
text_clf_nb.fit(X_train, y_train)

predictions = text_clf_nb.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions))