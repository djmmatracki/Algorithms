## Projektowanie Algorytmów

Projektowanie algorytmu polega na wymyśleniu ściśle określonego ciągu czynności, by w najbardziej efektywny sposób rozwiązać dane zadanie. Zrozumienie problemu objemuje odniesienie do wymagań funkcjonalnych oraz niefunkcjonalnych. Czego one dotyczą:

- Wymagania funkcjonalne w sposób formalny wskazują interfejs wejścia i wyjścia dla danego problemu który mamy rozwiązać.

- Wymagania niefunkcjonalne stanowią zbiór oczekiwań co do efektywności i bezpieczeństwa algorytmu.

Aby zaprojektować dobry algorytm należy mieć na uwadze 3 kwestie:

1. Czy algorytm zwraca rezultat, jakiego oczekujemy?
2. Czy robi to w optymalny sposób?
3. Jak efektywny będzie ten algorytm przy więkrzych zbiorach danych?

### Określenie złożoności problemu

- **Typ 1.** Problemy co do których można udowodnić, że dla ich rozwiązania istnieje algorytm wielomianowy.

- **Typ 2.** Problemy co do których można udowodnić, że nie istnieje dla nich rozwiązanie w postaci algorytmu wielomianowego.

- **Typ 3.** Problemy dla których nie znaleziono rozwiązania w postaci algorytmu wielomianowego, ale nie można udowodnić, że takie rozwiązanie nie istnieje.

##### Problem niedetermistycznie wielomianowy (problem NP)

Da się udowodnić że istnieje co najmniej jeden algorytm wielomianowy, którego można użyć w celu zweryfikowania potencjalnego rozwiązania.

##### Problem wielomianowy (problem P)

Da się udowodnić że istnieje co najmniej jeden algorytm wielomianowy, którego można użyć do ich rozwiązania.

##### Problemy NP zupełne

Nieznane są algorytmy wielomianowe pozwalające na wygenerowanie certyfikatu. Istnieją algorytmy wielomianowe, które weryfikują czy poprawne rozwiązanie jest optymalne.

##### Problemy NP trudne

Ta klasa zawiera problemy co najmniej tak trudne, jak którykolwiek z problemów NP, ale same nie muszą należeć do problemów NP.

