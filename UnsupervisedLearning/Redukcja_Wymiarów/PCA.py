from sklearn.decomposition import PCA
import pandas as pd

iris = pd.read_csv("iris.csv")
X = iris.drop('variety', axis=1)
pca = PCA(n_components=4)
pca.fit(X)

pca_df = pd.DataFrame(pca.components_, columns=X.columns)

X['PC1'] = X['sepal.length'] * pca_df['sepal.length'][0] + \
           X['sepal.width'] * pca_df['sepal.width'][0] + \
           X['petal.length'] * pca_df['petal.length'][0] + \
           X['petal.width'] * pca_df['petal.width'][0]

X['PC2'] = X['sepal.length'] * pca_df['sepal.length'][1] + \
           X['sepal.width'] * pca_df['sepal.width'][1] + \
           X['petal.length'] * pca_df['petal.length'][1] + \
           X['petal.width'] * pca_df['petal.width'][1]

X['PC3'] = X['sepal.length'] * pca_df['sepal.length'][2] + \
           X['sepal.width'] * pca_df['sepal.width'][2] + \
           X['petal.length'] * pca_df['petal.length'][2] + \
           X['petal.width'] * pca_df['petal.width'][2]

X['PC4'] = X['sepal.length'] * pca_df['sepal.length'][3] + \
           X['sepal.width'] * pca_df['sepal.width'][3] + \
           X['petal.length'] * pca_df['petal.length'][3] + \
           X['petal.width'] * pca_df['petal.width'][3]

print(X)

# Macierz wariancji oznacza że jeśli zdecydujemy się zastąpić cztery pierwotne cechy składową PCA1, będziemy w stanie uchwycić ok. 93% wariancji oryginalnych zmiennych.
# Jeżeli zdecydujemy się zastąpić 2 składowymi PCA1 i PCA2 to będziemy mieli 93% + 5% uchwyconej wariancji.
print(pca.explained_variance_ratio_)