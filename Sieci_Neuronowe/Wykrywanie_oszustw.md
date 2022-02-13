# Studium przypadku - uczenie głębokie do wykrywania oszustw

### Metodologia

Technika opiera się na strukturze która nazywa się syjamską siecią neuronową, którą charakteryzują dwie gałęzi, które mają taką samą architekturę.

Gdy trzeba zweryfikować autentyczność pewnego dokumentu, najpierw klasyfikujemy go w oparciu o jego wygląd, strukturę i rodzaj, a następnie porównujemy z oczekiwanym formatem i wzorem. Jeśli odchylenie przekracza pewien pułap to klasyfikujemy jako fałsz.

Aby porównać dokument z oczekiwanym wzorem, używamy dwóch identycznych konwolucyjnych sieci neuronowych w naszej architekturze syjamskiej. Zaletą tego typu sieci są detektory cech lokalnych niezmienne względem przesunięcia i możliwości uzyskania reprezentacji obrazu wejściowego pomimo jego licznych wad pod kątem geometrii obrazu. Naszym celem jest przepuścić dokument autentyczny i badany przez te same sieci a następnie porównać ich rezultaty.

Dla każdej klasy dokumentów będziemy wykonywać te same kroki:

1. Pobranie przechowywanego obrazu autentycznego dokumentu.

2. Autentyczny dokument przechodzi przez warstwy sieci neuronowej w celu stworzenia wektora cech, co stanowi matematyczną reprezentację wzorów w autentycznym dokumencie.

3. Dokument który ma podlegać weryfikacji to dokument testowy. Tworzymy drugi wektor cech.

4. Korzystamy z odległości euklidesowej między pierwszym i drugim wektorem cech. Rezultat tych obliczeń to miara podobieństwa. Przyjmuje ona wartość między 0 a 1. Czym więkrze prawdopodobieństwo tym dokumenty są bardziej podobne.
