# Wykorzystanie przetwarzania języka naturalnego do przetwarzania sentymentu

Operacje które należy wykonać do analizy sentymentu na przykładzie tweetów ze strony www.sentiment140.com

1. Tweety dzieli się na pojedyncze słowa nazywane tokenami

2. Dane wejściowe z tego procesu tworzą model bag-of-words, czyli zbiór pojedyńczych słów w tekście

3. Tweety podlegają dalszemu filtrowaniu poprzez usunięcie liczb, oraz słów ze stop listy.

4. Za pomocą dopasowań do wzorca usuwane są znaki niebędące literami, takie jak #@ i liczby.

5. Rezultat podlega procesowi stemmingu. Słowa są sprowadzane do korzenia.

6. Po przetworzeniu dane są zamieniane na strukturę nazywaną macierzą terminów dokumentu.

7. Z macierzy tweet dociera do wytrenowanego klasyfikatora, gdzie wyliczana jest wartość wagi polaryzacji sentymentu każdego słowa. Przyjmuje ona wartości z zakresu -5 do +5.

Z analizy sentymentu można korzystać w celu klasyfikacji opini klientów.