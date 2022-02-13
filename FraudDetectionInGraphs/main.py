from typing import Tuple, List
import networkx as nx
import matplotlib.pyplot as plt
import random


vertices = range(1, 11)

def random_edges(n:int) -> List[Tuple[int]]:
    return [(random.randint(1, 10), random.randint(1, 10)) for _ in range(n)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(random_edges(len(vertices)))

nx.draw(G, with_labels=True,node_color="y", node_size=800)
plt.show()

# Metody obliczania centralnosci dla poszczegolnych wierzcholkow w grafie

print("Stopniowa", nx.degree_centrality(G))
print("Oddalenie", nx.betweenness_centrality(G))
print("Bliskosc", nx.closeness_centrality(G))
print("Wektor wlasny", nx.eigenvector_centrality(G))