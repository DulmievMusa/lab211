from mnk import *
from my_library import *
from math import pi

alpha = 0.051
beta = 40.7
pot_es = []
N_es = []

I_es, U_es, E_es = get_all_columns_from_file("data10.csv")

for i in range(4):
    pot_es.append(alpha * (E_es[i]/beta))
    N_es.append((I_es[i] * U_es[i]) / 1000)

print("Первая серия опытов")
for i in range(4):
    print(my_round(pot_es[i]/N_es[i], 4))
print()


pot_es = []
N_es = []

I_es, U_es, E_es = get_all_columns_from_file("data3.csv")

for i in range(4):
    pot_es.append(alpha * (E_es[i]/beta))
    N_es.append((I_es[i] * U_es[i]) / 1000)

print("Вторая серия опытов")
for i in range(4):
    print(my_round(pot_es[i]/N_es[i], 4))

