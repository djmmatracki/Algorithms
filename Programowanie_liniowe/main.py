"""
    Planowanie przepustowosci w fabryce.

    Tabelka z potrzebnymi dniami by wyprodukowac robota:

                Technik     Specialista AI      Inzynier
    
    Robot A     3 dni           4 dni             4 dni
    Robot B     2 dni           3 dni             3 dni


    Cel zmaksymalizowac zyski w fabryce. Na robocie A mamy zysk 4200, Robot B 2800.
"""
import pulp


model = pulp.LpProblem("Profit maxing problem", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat="Integer")
B = pulp.LpVariable('B', lowBound=0, cat="Integer")

model += 5000 * A + 2500 * B, "Profit"

model += 3 * A + 2*B <= 20
model += 4 * A + 3*B <= 30
model += 4 * A + 3*B <= 44

model.solve()
print(A.varValue)
print(B.varValue)