import pandas as pd
import numpy as np
import pyfpgrowth as fp

dict1 = {
    "id": [0, 1, 2, 3],
    "items": [
        ["bramki", "ochraniacze"],
        ["kij", "bramki", "ochraniacze", "kask"],
        ["kask", "ochraniacze"],
        ["kij", "ochraniacze", "kask"]
    ]}

transactionSet = pd.DataFrame(dict1)

patters = fp.find_frequent_patterns(transactionSet['items'], 1)
rules = fp.generate_association_rules(patters, 0.3)
print("Patterns:")
for key, val in patters.items():
    print(f"{key}: {val}")

# W skrocie osoby ktore kupuja to z lewej kupuja tez to z prawej z danym prawdopodobienstwem
print("Rules:")
for key, val in rules.items():
    print(f"{key}: {val}")