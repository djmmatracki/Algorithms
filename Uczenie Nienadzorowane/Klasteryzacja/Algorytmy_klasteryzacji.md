## Algorytmy klasteryzacji

### Metody obliczania odleglosci miedzy punktami danych

- Odleglosc euklidesowa - określa się jako pierwiastek sumy kwadratów różnicy między odpowiednimi składowymi.
- Metryka miejska
    Lepiej oddaje niz euklidesowa czesto. Najdluzsza droga miedzy punktami.
- Miara kosinusowa
    Oddaje przy duzych wymiarach.


### Algorytm k-średnich (algorytm centroidów)

- Wybieramy liczbę klastrów k
- Spośród próbek danych losowo wybieramy k punktów jako centroidy
- Przypisujemy każdą próbkę danych do najbliżeszgo jej klastra
- Wyliczamy średnią odległości każdego punktu od środka danego każdego klastra.


### Algorytm grupowania hierarchicznego

- Tworzymy osobny klaster dla każdej próbki danych w dziedzinie problemu.
- Grupujemy ze sobą najbliższe sobie próbki.
- Sprawdzamy warunek wyjścia, jeżeli nie jest spełniony powtarzamy krok 2.

Powstaje dendogram

### Metody oceny klastrów

Metoda sylwetki