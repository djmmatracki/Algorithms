# Model bag-of-words

W modelu bag-of-words wyliczamy istotność każdego słowa w kontekście każdego dokumentu, jaki chcemy przeanalizować.

Sposoby oceniania wagi słów:

- Metoda binarna. Cecha będzie miała wartość 1, jeżeli pojawia się w tekście oraz 0 jeżeli nie.

- Sumy. Liczba wystąpień słowa w tekście.

- Ważenia częstością terminów. Wartość cechy będzie równa stosunkowi tego, jak niepowtarzalne jest słowo w pojedyńczym dokumencie do tego jak niepowtarzalne w całym korpusie.
