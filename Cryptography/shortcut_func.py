"""
    Funkcje skrótu.
    Są jednokierunkowe.
    Używane są do weryfikacji spójności pliku po zrobieniu jego kopii.
    W tym celu plik jest kopiowany z miejsca źródłowego do docelowego. odpowiadający mu skrót jest kopiowany wraz z nim.

"""
from passlib.hash import md5_crypt, sha512_crypt

# Prosta funkcja skrótu md5, podatna na kolizje
myHash = md5_crypt.hash("myPassword")

print(myHash)

print(md5_crypt.verify("myPassword", myHash))

# 
myHash = sha512_crypt.using(salt="qIo0foX5", rounds=5000).hash("myPassword")

print(myHash)