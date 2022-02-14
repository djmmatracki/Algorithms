# Algorytmy drzewa decyzyjnego

Opiera się na podejściu rekurencyjnym "dziel i rządź", generującego zestaw reguł, na podstawie których można przewidzieć etykietę.

Algorytm:

1. Znalezienie najważniejszej cechy. Obliczenia te opierają się na współczynnikach takich jak współczynnik wzmocnienia czy współczynnik nieczystości.

2. Podział. Na podstawie najważniejszej cechy algorytm tworzy kryterium podziału zbioru treningowego na dwie gałęzie: próbki spełniające kryterium oraz niespełniające.

3. Poszukiwanie liści. Jeśli powstała w ten sposób gałąź zawiera głównie etykiety jednej klasy, kończy się tworząc liść.

4. Sprawdzenie warunku wyjścia i powtórzenie.

## Wady i zalety klasyfikatorów drzewa decyzyjnego

#### Zalety

- Reguły modelu są zrozumiałe dla ludzi. Tak zwane białoskrzynkowe algorytmy. Wykorzystywane w sektorze publicznym czy ubezpieczeniowym.

- Klasyfikatory oparte na drzewach decyzyjnych zostały zaprojektowane do pozyskiwanania informacji w przestrzeni dyskretnej, co oznacza, że więkrzość to zmienne jakościowe.

### Wady

- Jeżeli drzewo za bardzo się rozrośnie może to skutkować zbyt dużym dopasowanie modelu.

- Niemożliwość uchwycenia nie liniowych zależności w regułach.

## Przypadki użycia

#### Klasyfikacja rekordów

- We wnioskach kredytowych. Klasyfikator binarny czy kredytobiorca będzie terminowo spłacał swoje zobowiązania.

- W segmentacji klientów. Dzielenie klientów na klasę premium, średnią oraz niższą by dostosować strategie marketingowe.

- W diagnozach lekarskich. Oznaczające łagodne i złośliwe guzy.

- W analizie skuteczności lekarskiej. Trenujemy klasyfikatory wskazujący pacjentów którzy dobrze zareagowali na daną kurację.