## Grupowanie podobnych tweetów

Algorytm obejmuje dwa etapy:

- Modelowanie tematu. Algorytm odkryje wszystkie tematy pojawiające się w danym zbiorze danych.

- Grupowanie. Przypisze każdej wiadomości dany temat zdefiniowany wcześniej.


### Modelowanie tematu

To proces odkrywania pojęć przewijających się w zbiorze dokumentów, pozwalajacych na ich rozróżnienie. W celu kategoryzacji tweetow często korzysta się z algorytmów opartych na zasadzie szufladkowania Dirichleta np. LDA.

Ponieważ tweet to krótki dokument w całości poświęcony jednemu tematu. Możemy napisać prosty algorytm modelujący:

- Przeprowadź analizę leksykalną.
- Wstępnie przetwórz dane. Wykonać stemming.
- Stwórz macierz częstości dokument-słowo (macierz TDM) dla danego zbioru tweetów. Wybrać pierwsze 200 słów które pojawią się najczęściej.
- Wybierz 10 pierwszych słów które pośrednio lub bezpośrednio przedstawiają jakiś temat albo koncepcję.

### Klasteryzacja
Gdy wskazaliśmy powtarzające się w zbiorze tematy, ustawimy je środkami klastrów. Następnie możemy skorzystać z algorytmu k-średnich, który przypisze każdy tweet do któregoś z tematów.

