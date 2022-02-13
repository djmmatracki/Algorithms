# Wprowadzenie do NLP

### Zastosowania NLP (Natural Language Processing):

- **Identyfikacja tematów**. Wykrywanie tematów w repozytoriach tekstowych i klasyfikowanie znajdujących się tam dokumentów zgodnie ze zidentyfikowanymi treściami.

- **Analiza sentymentu**. Klasyfikowanie tekstu na podstawie negatywnych lub pozytywnych uczuć.

- **Tłumaczenie maszynowe**. Tłumaczenie z jednego języka na inny.

- **Syntezowanie mowy**. Text-to-speach

- **Interpretacja subiektywna** - Inteligentne interpretowanie pytań.

- **Wykrywanie fałszywych wiadomości**

### Terminologia

#### Normalizacja

Bazowy rodzaj przetwarzania. Stosowany do danych wejściowych. Normalizacja obejmuje:

- zmianę całego tekstu na małe bądź wielkie litery
- usunięcie interpunkcji
- usunięcie liczb

#### Korpus

Zbiór dokumentów wejściowych.

#### Tokenizacja

Podzielenie tekstu na listę tokenów lub słów.

#### Rozpoznawanie podmiotów

Rozpoznawaniem podmiotów nazwanych.

#### Stop-lista

Usuwanie słów które nie mają więkrzego znaczenia w wykrywaniu tematu ('było', 'my'...)

#### Analiza sentymentu

Proces wskazania pozytywnych lub negatywnych emocji w tekście.

#### Steaming lub lematyzacja

Sprowadzenie każdego słowa do jego korzenia. (użył, użyliśmy, użyła) => użyć. Najczęściej używanym algorytmem do stemmingu w języku angielskim jest algorytm Portera.

### Sposoby implementacji NLP

- model NLP bag-of-words
- tradycyjne klasyfikatory NLP
- wykorzystanie uczenia głębokiego do NLP
