# Anatomia sieci neuronowych

Z czego składa się sieć neuronowa:

- **Warstwy** - 
- **Funkcja Straty** - dostarcza informacji zwrotnej, która jest wykorzystywana w wielu iteracjach. Funkcja straty wskazuje odchylenie.
- **Funkcja kosztu** - To funkcja straty dla całego zbioru próbek.
- **Optymalizator** - Określa jak interpretowany będzie sygnał zwrotny.
- **Wagi** - Wagi wylicza się poprzez trenowanie sieci. Przekształca dany zbiór danych zgodnie z jego istotnością.
- **Dane wejściowe** - Dane używane do trenowania
- **Funkcja aktywacji** - Wartości są mnożone przez różne wagi, a następnie agregowane. Szczegóły agregacji i interpretacji wartości określa funkcja aktywacji.

### Definicja Gradientu Prostego

Punktem wyjściowym algorytmu gradientu prostego są losowe wartości wag, które wymagają optymalizacji, w miarę jak w pętli wykonujemy algorytm. W każdej kolejnej iteracji algorytmu zmienia wartości wag tak, by ograniczyć koszt. Zmiana wag będzie zależała od:

- Kierunku
- Szybkości uczenia

### Funkcje aktywacji

Funkcja aktywacji definiuje jak przetworzone zostaną dane wejściowe do danego neuronu w celu wygenerowania danych wyjściowych.

#### Funkcja Progowa

Jej resulatat jest binarny. Jej wynikiem będzie 1 jeśli jakiekolwiek dane wejściowe mają wartość wyższą od 0. Jest ona bardzo czuła.

#### Funkcja sigmoidalna

To ulepszenie funkcji progowej. Mamy w niej kontrolę nad czułością funkcji aktywacji.

```python
    def sigmoidFunction(z):
        return 1 / (1+np.exp(-z))
```

#### Relu

Kiedy x <= 0 to wynikiem jest 0, inaczej jest równa x. Najbardziej popularna w uczeniu sieci neuronowych.

```python
    def ReLu(x):
        if x<0:
            return 0
        else:
            return x
```

#### Leaky Relu

Bardziej oddaje od zwykłego ReLu. Jest kilka sposobów wyznaczenia beta:

- Możemy przypisać wartość domyślną.
- Możemy zrobić z niej parametr sieci neuronowej i pozwolić sieci ustalić jej wartość.
- Możemy jej przypisać wartość losową.

```python
    def leakyReLu(x, beta=0.01):
        if x<0:
            return (beta*x)
        else:
            return x
```

#### Tanges hiperboliczny

Jest podobny do funckji sigmoidalnejm, ale pozwala na obsługę negatywnego sygnału

```python
    def tanh(x):
        numerator = 1-np.exp(-2*x)
        denominator = 1+np.exp(-2*x)
```


#### Znormalizowana funkcja wykładnicza (funkcja softmax)

Sprawdza się w problemach klasyfikacji z wieloma kategoriami. Kiedy mamy więcej niż dwa wymiary w danych wejściowych.