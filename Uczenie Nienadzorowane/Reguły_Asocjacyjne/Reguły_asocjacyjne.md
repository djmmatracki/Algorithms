## Reguły asocjacyjne

Zastosowania:
- Jakie wartości powietrza, zachmurzenia i temperatury mogą prowadzić do opadów deszczu kolejnego dnia?
- Jak rodzaj szkody zgłoszony ubezpieczycielowi może wskazywać na oszustwo?
- Jakie połączenie leków może spowodować powikłania u pacjentów?

Istnieje grupa algorytmów odpowiadająca za wykrywanie wzorców w zbiorach danych. Jednym z nich jest Apriori, który umożliwia:

- Zmierzenie częstotliwości występowania wzorca.
- Ustalenie relacji przyczynowo-skutkowej pośród wzorców.
- Wyliczenie przydatności wzorców.

Reguły asocjacyjne można podzielić na:

- trywialne
- niewytłumaczalne
- użyteczne

### Wskaźniki reguł

- wsparcie - wskazuje jak często w zbiorze danych występuje wzorzec. Liczba danego wzorca / liczba całkowitych transakcji
- zaufanie - prawdopodobienstwo warunkowe
- przyrost

### Algorytmy analizy asocjacyjnej

- algorytm Apriori
- algorytm FP-Growth - obejmuje dwa etapy. Stworzenie drzewa FP oraz analizy drzewa.