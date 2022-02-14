from collections import Counter
from sklearn.decomposition import LatentDirichletAllocation
from typing import List, Dict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from sklearn import cluster

freedom_sentances = [
    "wolność nie istnieje wolność, jak tylko jako wolność wolność konkretnego człowieka.",
    "wolność wolność, który nie wolność przyznać się do wolność.",
    "Nie jesteśmy. wolność i z tego wolność rachunek. wolność zło oznacza chorobę wolność.",
    "Potrafimy walczyć o wolność, ale wolność się nam jej wolność.",
    "Wyzwolenie wolność zaczyna się od wolność."]

about_kids = [
    "Chyba nikt dziećmi nie Dzieci, co to dziećmi bać się, dziećmi jego dziećmi nie dziećmi nagle dziećmi w nocy.",
    "Jeśli będąc dziećmi, Dzieci się żyć, to będąc dorosłymi, uczymy się umierać.",
    "Dzieci do końca życia nie Dzieci kłamstw swoich rodziców.",
    "Tylko dzieci mówią całą prawdę. Dlatego właśnie są dziećmi.",
    "Dzieci muszą Dzieci dziećmi jak do za dziećmi butów."
]

success = [
    "To co znamy jako sukces, ma tak wiele sukces, jak wielu jest ludzi którzy chcą go osiągnąć.",
    "Sukces jest wynikiem sukces decyzji.",
    "Dopóki sukces, jesteś sukces.",
    "Ten, kto nie jest wystarczająco sukces, by podjąć sukces, niczego w sukces nie osiągnie."
]

def format_sentence_list(sentances):
    # Zwraca slowniki z slowami oraz czestoscia ich wystepownia oraz liste wszystkich slow
    result = []
    words = []

    for i in range(len(sentances)):
        # Usuniecie znakow
        tweet = sentances[i].replace(",", "")
        tweet = tweet.replace(".", "")

        # Zamienic na male litery
        tweet = tweet.lower()

        # Rozdzielic do tablicy
        tweets = tweet.split(" ")
        words.extend(tweets)

        # Policzyc slowa w danej liscie
        result.append(dict(Counter(tweets)))
    
    return result, list(set(words))

def matrix_from_dict(sentence_list: List[Dict], words: list) -> np.ndarray:
    result = []
    for sent in sentence_list:
        row = []
        for word in words:
            if sent.get(word) is not None:
                row.append(sent[word])
            else:
                row.append(0)
        result.append(row)
    return np.array(result)

sentances = freedom_sentances + success + about_kids
# random.shuffle(sentances)
sentence_list, words = format_sentence_list(sentances)

data = matrix_from_dict(sentence_list, words)

n = 25
# Redukcja wymiarow macierzy do n
lda = LatentDirichletAllocation(n_components=n)
transformed_data = lda.fit_transform(data)

# KMeans tworzymy model z 3 klastrami
MyKmeans = cluster.KMeans(n_clusters=3)
MyKmeans.fit(data)

# Agglomerative clustering
Aglomerative = cluster.AgglomerativeClustering(n_clusters=3, affinity="cosine", linkage="complete")
Aglomerative.fit(data)


print("KMeans clustering")
# Pierwszy zbior
print(MyKmeans.labels_[:5])

# Drugi zbior
print(MyKmeans.labels_[5:10])

# Trzeci zbior
print(MyKmeans.labels_[10:])

print()
print("Agglomerative clustering")

# Pierwszy zbior
print(Aglomerative.labels_[:5])

# Drugi zbior
print(Aglomerative.labels_[5:10])

# Trzeci zbior
print(Aglomerative.labels_[10:])
