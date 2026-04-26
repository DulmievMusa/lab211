from mnk import *
from my_library import *
from math import pi

beta = 40.7

I_es, U_es, E_es = get_all_columns_from_file("data3.csv")
N_es = []
dT_es = []

for i in range(4):
    dT_es.append(E_es[i]/beta)
    N_es.append((I_es[i] * U_es[i])/1000)

k, b, sigma_k, sigma_b = linear_regression(N_es, dT_es)



print("k", k)
print("sigma_k", sigma_k)
print("eps", (sigma_k/k) * 100)
paint_line_function(k, b, N_es, y_es=dT_es)



set_end(title="График изменения мощности от изменения температуры", y_label="$\Delta T, \\text{К}$", x_label="N, Вт")