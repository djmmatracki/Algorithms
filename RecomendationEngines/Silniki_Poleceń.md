# Silniki Poleceń

Systemy rekomendacji opierają się na metodzie stworzonej do przewidywania produktów którymi użytkownik będzie najbardziej zainteresowany. Używane w aplikacjach e-commerce silniki poleceń używają zaawansowanych algorytmów do poprawy doświadczenia zakupowego użytkoników i pozwalają dostawcom usług na dopasowywanie swoich produktów zgodnie z preferencjami.

### Rodzaje silników poleceń

- silniki oparte na treści
- filtrowanie kooperacyjne
- hybrydowe silniki poleceń

## Silniki oparte na treści

Podstawowe założenie silników opartych na treści to sugerowanie produktów podobnych do tych, które wcześniej wzbudziły zainteresowanie użytkownika. Efektywność takich narzędzi zależy od naszej umiejętności wyliczania prawdopodobieństwa między produktami.

Centralnym problemem w tej sytuacji staje się określenie, które produkty są do siebie podobne.

#### Znajdowanie podobieństw między nieustrukturyzowanymi dokumentami

Jednym ze sposobów znajdowania podobieństw między dokumentami jest ich przetworzenie. Powstaje w ten sposób struktura danych nazywana macierzą terminów.

Gdy wyznaczymy macierz są dwa sposoby wyznaczenia podobieństwa:

- Na podstawie częstości występowania
- (Lepszy sposób) Przy użyciu ważenia częstością terminów. Jest to wskaźnik wyliczający wagę każdego słowa w kontekście problemu, jaki stramy się rozwiązać. Jest to iloczyn częstości terminu oraz odwrotnej częstości w dokumentach.

#### Macierz współwystępowania

Metoda ta opiera się na założeniu, że jeśli dwa produkty występują zwykle razem, istnieje duża szansa że są podobne lub przynajmniej należą do tej samej kategorii. (Było w poprzednich rozdziałach)

#### Silniki poleceń oparte na filtrowaniu kooperacyjnym

Silniki poleceń oparte na filtrowaniu kooperacyjnym korzystają z analizy danych historycznych zwyczajów zakupowych urzytkowników. Podstawowe założenie polega na tym, że jeżeli dwóch użytkowników interesują te same produkty, możemy zakwalifikować ich jako podobnych. Co za tym idzie jeżeli jeden użytkownik kupi jakiś inny produkt to możemy zaproponować go drugiemu użytkownikowi.

### Hybrydowe Silniki poleceń

Jeżeli połączymy filtrowanie kooperacyjne oraz silniki oparte na treści to powstaną hybrydowe silniki poleceń.

##### Generowanie macierzy podobieństw

W poleceniach hybrydowych zaczynamy od zbudowania macierzy podobieństw produktów na podstawie poleceń opartych na treści. Macierz podobieństw między produktami. n x n (n - liczba produktów)

##### Generowanie wektorów preferencji

W oparciu o historię każdego użytkownika w systemie stworzymy wektor preferencji, który wskaże zainteresowania poszczególnych osób danym produktem. (wektor kolumnowy dla danego użytkownika określa zainteresowanie danych przedmiotem 1 x n)


##### Generowanie poleceń

Aby stworzyć rekomendacje należy pomnożyć macierze. Dla każdego użytkownika zostanie utworzony wektor (1 x n)


## Obszary Zastosowań

- Dwie trzecie filmów na Netflixsie jest polecanych.
- 35% transakcji na Amazonie pochodzi z poleceń
- Na Google News polecenia generują 38% więcej kliknięć.
- Dopasowywanie CV do ofert pracy.
- Sugerowanie zajęć fakultatywnych
