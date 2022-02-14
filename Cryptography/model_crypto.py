import cryptography as crypt
from sklearn.linear_model import LogisticRegression
from cryptography.fernet import Fernet
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from pickle import dump
iris = load_iris()


X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Wytrenowanie modelu
model = LogisticRegression()
model.fit(X_train, y_train)

# Zdefiniowanie nazw plikow
filename_source = "myModel_source.sav"
filename_destionation = "myModel_destination.sav"
filename_sec = "myModel_sec.sav"

# Skorzystanie z pickle do przechowania modelu
dump(model, open(filename_source, "wb"))

# Funkcja ktora wygeneruje klucz symetryczny
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Funkcja ktora czyta klucz z pliku
def load_key():
    return open("key.key", "rb").read()

# Funkcja ktora zaszyfruje model i zachowa go w pliku
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename_source, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename_sec, "wb") as file:
        file.write(encrypted_data)
    
write_key()
encrypt(filename_source, load_key())

def decrypt(filename, key):
    f = Fernet(key)

    with open(filename_sec, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename_destionation, "wb") as file:
        file.write(decrypted_data)

decrypt(filename_sec, load_key())

loaded_model = open(filename_destionation, 'rb')
result = loaded_model.score(X_test, y_test)
print(result)
