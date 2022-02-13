import pandas as pd
from scipy.sparse import data
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('auto.csv')

dataset = dataset.drop(columns=["car name"])
dataset = dataset.drop(columns=["origin"])
dataset = dataset.drop(columns=["model year"])

# print(dataset.head(5))

# To numeric
dataset = dataset.apply(pd.to_numeric, errors='coerce')
dataset.fillna(0, inplace=True)

y = dataset.iloc[:, 0]
X = dataset.drop(columns=['mpg'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)