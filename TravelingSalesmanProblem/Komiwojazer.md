# Komiwojażer

Problem komiwojażera określa następujące zadanie: mając liste miast oraz odległości między ich każdą parą, jaka jest najkrótsza ścieżka pozwalająca odwiedzuć wszystkie miasta i wrócić do miasta początkowego?

## Przybliżenie problemu

Problem komiwojażera to problem np-trudny czyli nie istnieją algorytmy o wielomianowej złożoności obliczeniowej pozwalające na rozwiązanie tego problemu. Jednak dla małej liczby miast istnieją algorytmy które pozwalają wyznaczyć optymalne trasy.

## Teoretycznie

Zadanie polega na znalezieniu minimalnego cyklu Hamiltona w pełnym Grafie ważonym krawędziowo.

**Graf pełny** - taki graf gdzie każdy wierzchołek jest połączony ze wszystkimi innymi wierzchołkami.

**Graf ważony krawędźowo** - wprowadza liczbowe etykiety przyporządkowane krawędziom łączącym wierzchołki.

**Cykl** - jest to ścieżka zamknięta z takim samym pierwszym i ostatnim wierzchołkiem.

**Cykl Hamiltona** - szuka się cyklu prostego (czyli takiej ścieżki, w której każdy oprócz pierwszego - wierzchołek odwiedzony jest tylko raz)

## Przykład

#### Krok 1 - redukcja

Redukujemy wartości - dla każdego rzędu znajdujemy wartość minimalną i odejmujemy ją od wszystkich elementów w tym rzędzie. Sprawdzamy czy w każdej kolumnie występuje co najmniej jedno zero - jeżeli nie, to redukujemy w kolumnach.

Suma odjętych wartości oznacza **lower bound**.

#### Krok 2 - wybór przejścia

Następnie sprawdzamy wszystkie możliwe przejścia: wybieramy te pary wierzchołków, na których przejściu w tabeli występuje wartość 0. Następnie wyznaczamy sumę minimalnych wartości w wyznaczonym wierszu i kolumnie.

Wybieramy krawędź o maksymalnej z wyznaczonych wartości, dodajemy do szukanego rozwiązania.

#### Krok 3 - aktualizacja macierzy kosztów

Należy teraz usunąć z macierzy kosztów odpowiedni rząd i kolumnę. Należy również sprawdzić czy istnieje możliwość utworzenia innego cyklu w bierzącym rozwiązaniu.
