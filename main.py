from mnk import *
from my_library import *
from math import pi

d = 0.95
L = 125 * (10 ** -3)
beta = 40.7

I_es, U_es, E_es = get_all_columns_from_file("data3.csv")
print("eps, U, I, delta T, N, R_н")
for i in range(4):
    print(f"{E_es[i]}, {U_es[i]}, {I_es[i]}, {my_round(E_es[i]/beta, 2)}, {my_round((I_es[i] * U_es[i])/1000, 2)}, {my_round((U_es[i]*1000)/I_es[i], 2)}")