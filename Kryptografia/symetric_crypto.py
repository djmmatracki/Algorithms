import cryptography
from cryptography.fernet import Fernet

# Wygenerowanie klucza
key = Fernet.generate_key()

print(key)

# Zapisanie klucza do pliku
# file = open("mykey.key", "wb")
# file.write(key)
# file.close()

# Odczytanie klucza z pliku
# file = open("mykey.key", "wb")
# file.read()
# file.close()

# Zaszyfrowanie wiadomości
message = "W Ottawie jest bardzo zimno.".encode()
f = Fernet(key)
encrypted = f.encrypt(message)

# Odszyfrowanie
decrypted = f.decrypt(encrypted)
print(decrypted)
