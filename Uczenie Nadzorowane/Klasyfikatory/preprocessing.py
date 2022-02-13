import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("Social_Network_Ads.csv")

dataset = dataset.drop(columns=['User ID'])

# print(dataset.head(5))

# Zakodowanie płci
enc = OneHotEncoder()
enc.fit(dataset.iloc[:,[0]])

onehotlabels = enc.transform(dataset.iloc[:,[0]]).toarray()
genders = pd.DataFrame({'Female': onehotlabels[:, 0], 'Male': onehotlabels[:, 1]})

result = pd.concat([genders, dataset.iloc[:,1:]], axis=1, sort=False)

# Wskazanie cech i etykiet
y = result['Purchased']
X = result.drop(columns=['Purchased'])

# Podzielenie na zbior testowy i treningowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


# Skalowanie cech (Normalizacja by zawierały się w zakresie 0-1)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
