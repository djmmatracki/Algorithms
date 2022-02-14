"""Szyfry podstawieniowe"""

import codecs


# Szyfr cezara
# Zamieniamy kazdy znak na odpowiednik przesuniety o 3 znaki w alfabecie
rotation = 3
P = 'CALM'

def szyfr(word, rotation):
    C = ''
    for letter in word:
        C += chr(ord(letter) + rotation)
    
    return C

print(szyfr(P, rotation))


#
P = "CALM"
C = codecs.encode(P, 'rot_13')
print(C)