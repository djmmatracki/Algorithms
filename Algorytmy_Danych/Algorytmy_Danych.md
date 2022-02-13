# Algorytmy Danych

Zagadnienia:

- klasyfikacja danych
- algorytmy przechowywania danych
- wykorzystywanie algorytmów do kompresji danych
- wykorzystywanie algorytmów do strumieniowania danych

## Klasyfikacja danych

Cechy które należy brać pod uwagę w kontekście algorytmów danych:

- Rozmiar wejścia. Ujmuje ona ilość danych którą należy przetworzyć i przechować w algorytmie.

- Szybkość narastania. Definiuje ona prędkość, z jaką generowane są nowe dane. "Hot data" - szybko narastaja, "Cold data" - wolno.

- Różnorodność treści i struktury. Odnosi się ona do zróżnicowania i liczby rodzajów ustrukturyzowanych i nieustrukturyzowanych danych, które trzeba połączyć w jedną tabelę.

## Algorytmy przechowywania danych

Rzetelne i wydajne repozytorium danych to serce systemu rozproszonego. Jeśli takie repozytorium zostało stworzone z myślą o analizie nazywamy je data lake'iem.

#### Strategie przechowywania danych

Właściwa strategia przechowywania danych zależy od rodzaju danych, planowanego schematu korzystania z nich i wymagań niefunkcjonalnych. Twierdzenie CAP (Consistency, avaibility, partition tolerance) stanowi podstawę więkrzości strategii przechowywania danych w systemach rozproszonych.

### Twierdzenie CAP

Zwraca ono uwagę na liczne kompromisy, nieuchronne w procesie projektowania rozproszonego systemu przechowywania.

Aby zrozumieć jego założenia warto zdefiniować trzy cechy: spójność, dostępność oraz odporność na partycjonowanie.

- **Spójność**. Spójność gwarantuje, że w pewnym punkcie czasu t1, niezależnie od tego, z którego węzła skorzystamy, uzyskamy taki sam rezultat. Każda operacja odczytu albo zwróci najnowsze spójne w całym repozytorium dane albo poskutkuje błędem.

- **Dostępność**. Gwarantuje że dowolny węzeł będzie w stanie natychmiastowo obsłużyć dane.

- **Odporność na partycjonowanie**. Odporność na partycjonowanie zapewnia, że jeśli następi błąd w komunikacji z pewną niewielką częścią węzłów, system będzie kontynuował pracę.

Twierdzenie mówi że system może charakteryzować się jedynie dwiema z trzech cech.

Trzy typy systemów rozproszonych:

#### Systemy CA

Charakteryzują się spójnością i dostępnością. Przykłady to MySQL, PostgreSQL, Oracle...

#### Systemy AP

Zoptymalizowane pod względem dostępności. Używane są do monitorowania w czasie rzeczywistym, np. w sieci czujników. Przykład to Cassandra.

#### Systemy CP

Zapewniają spójność oraz odporność na partycjonowanie. Typowym przypadkiem użycia takich systemów jest przechowywanie pliku w formacie JSON. MongoDB.


### Algorytmy strumieniowania danych

Zastosowania strumieniowania:

- wykrywanie oszustw
- monitorowanie systemów
- wytyczenie drogi zamówienia
- ekrany wizualizujące wskaźniki w czasie rzeczywistym
- czujniki ruchu na autostradach
- kontrola transakcji kartami kredytowymi

## Algorytmy kompresji danych

### Algorytmy kompresji bezstratnej

Są to algorytmy, które potrafią kompresować dane tak, że po ich dekompresji nie straci się żadnych informacji. Zastosowania:

- kompresja dokumentów
- kompresja pakietów kodu źródłowego
- zamianę dużej liczby małych plików na małą liczbę dużych

#### Kodowanie Hoffmana

Kodowanie hoffmana to jedna z najprostszych metod kompresji danych, opierająca się na tworzeniu drzewa Hoffmana, które stanowi podstawę kodowania i dekodowania danych.

Uwagi co do kodowania hoffmana:

- Kodowanie. W kontekście danych oznacza reprezentowania ich w innej formie.
- Słowo kodowe. Konkretny znak w formie zakodowanej.
- Kod stałej długości. Każdy znak jest kodowany na tej samej liczbie bitów.
- Kod zmiennej długości.