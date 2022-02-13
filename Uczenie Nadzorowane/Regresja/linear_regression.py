"""
Regresja liniowa

Kiedy używa się regresji liniowej?

- Przewidywanie sprzedaży
- Ustalanie optymalnej ceny produktów
- Wyliczanie związku przyczynowego między zdarzeniem a odpowiedzią
- Wzskazanie wzorców służących do przewidywania przyszłych zachowań opartych na znanych kryteriach

Wady

- Nie radzi sobie z brakującymi danymi
- Stosuje sie do danych numerycznych
"""
from sklearn.linear_model import LinearRegression
from preprocessing import X_train, y_train, X_test, y_test
from sklearn.metrics import mean_squared_error
from math import sqrt

# Uczenie modelu
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predykcja
y_pred = regressor.predict(X_test)

# Jakosc modelu
print(sqrt(mean_squared_error(y_test, y_pred)))
