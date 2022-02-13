


centrality = dict()


# Nadajemy wierzcholkom oszustom stopien ich przewinienia
deg = {
    1: 0,
    2: 6,
    3: 0,
    4: 0,
    5: 7,
    6: 8,
    7: 10,
    8: 0,
    9: 0
}

# Wyznaczamy srednia ze wspolczynnikow centralnosci dla kazdego wierzcholka
for k in range(1, 10):
    centrality[k] = (cent1[k] + cent2[k] + cent3[k] + cent4[k])/4

# Mnozymy centralnosc razy stopnie przewinienia i dzielimi przez maksymalny stopien (czyli 10)

DOS = {k: (centrality[k]*deg[k])/10 for k in deg.keys()} # wspolczynniki podejrzen dla danych wierzcholkow
print(DOS)
plt.show()

