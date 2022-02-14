from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd
from word_formating import format_sentence_list

freedom_sentances = [
    "Dobro nie istnieje inaczej, jak tylko jako konkretna dobroć i wolność konkretnego człowieka.",
    "Nie jest wolny człowiek, który nie potrafi przyznać się do winy.",
    "Nie jesteśmy bezgranicznie wolni. Jesteśmy wolni wobec dobra i zła i z tego robimy rachunek. Wszelkie zło oznacza chorobę wolności.",
    "Potrafimy walczyć o wolność, ale trudno się nam jej dorabiać.",
    "Wyzwolenie człowieka zaczyna się od wewnątrz."]

about_kids = [
    "Chyba nikt naprawdę nie wie, co to znaczy bać się, dopóki jego dziecko nie zacznie nagle krzyczeć w nocy.",
    "Jeśli będąc dziećmi, uczymy się żyć, to będąc dorosłymi, uczymy się umierać.",
    "Dzieci do końca życia nie zapominają kłamstw swoich rodziców.",
    "Tylko dzieci mówią całą prawdę. Dlatego właśnie są dziećmi.",
    "Dzieci muszą dorosnąć do swojej wyobraźni jak do za dużych butów."
]

success = [
    "To co znamy jako sukces, ma tak wiele znaczeń, jak wielu jest ludzi którzy chcą go osiągnąć.",
    "Sukces jest wynikiem właściwej decyzji.",
    "Dopóki walczysz, jesteś zwycięzcą.",
    "Ten, kto nie jest wystarczająco odważny, by podjąć ryzyko, niczego w życiu nie osiągnie."
]

# Podejscie 1

# Modelowanie Tematu
# 1. Usunac kropki, przecinki i rodzielic kazdy tekst na liste slow.
# 2. Zmienic wszystkie slowa na male litery.
# 3. Polaczyc slowa ktore sie pokrywaja w 70%
# 4. Pobrac slowa ktore sie powtarzaja najczesciej i zapisac do zmiennej.
# 5. Usunac z kazdego tekstu slowa ktore nie naleza do najczestrzych.
# 6. Stworzyc dataframe gdzie kazdy rekord to liczba slow dla danego cytatu

#  Grupowanie
# Zastosowanie algorytmu KMeans cluster

cytaty = success + about_kids + freedom_sentances
data = success + about_kids + freedom_sentances

slowa = []

for i in range(len(cytaty)):
    # Usuniecie znakow
    cytaty[i] = cytaty[i].replace(",", "")
    cytaty[i] = cytaty[i].replace(".", "")

    # Zamienic na male litery
    cytaty[i] = cytaty[i].lower()

    # Rozdzielic do tablicy
    cytaty[i] = cytaty[i].split(" ")

    # Usunac koncowki slow
    for k in range(len(cytaty[i])):
        # d = (len(cytaty[i][k])*8)//10
        cytaty[i][k] = cytaty[i][k][:4]
        # Dodac slowa
        slowa.append(cytaty[i][k])

    # Policzyc slowa w danej liscie
    cytaty[i] = dict(Counter(cytaty[i]))


slowa = dict(Counter(slowa))

# Bierzemy 40 slow z najczesciej powtarzajacych sie
slowa = [(word, count) for word, count in slowa.items()]
slowa = sorted(slowa, key=lambda x: x[1])[-40:]
slowa = [s[0] for s in slowa]

# Usuwam slowa ktore nie naleza do slow najczesciej powtarzajacych sie
for d in cytaty:
    words = list(d.keys())
    for word in words:
        if word not in slowa:
            d.pop(word, None)

for c in cytaty:
    for s in slowa:
        if s not in c.keys():
            c[s] = 0

data_dict = dict()

for c in cytaty:
    for k in c.keys():
        if data_dict.get(k):
            data_dict[k].append(c[k])
        else:
            data_dict[k] = [c[k]]


# Grupowanie
dataset = pd.DataFrame(data_dict)
myKmeans = cluster.KMeans(n_clusters=3)
myKmeans.fit(dataset)

labels = myKmeans.labels_

for i in range(len(labels)):
    print(f"{data[i]} -- {labels[i]}")


