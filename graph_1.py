from mnk import *
from my_library import *
from math import pi

beta = 40.7

I_es, U_es, E_es = get_all_columns_from_file("data10.csv")
N_es = []
dT_es = []

for i in range(4):
    dT_es.append(E_es[i]/beta)
    N_es.append((I_es[i] * U_es[i])/1000)

k, sigma_k = origin_linear_regression(N_es, dT_es)



print("k", k)
print("sigma_k", sigma_k)
print("eps", (sigma_k/k) * 100)
N_es.insert(0, 0)
dT_es.insert(0, 0)
paint_line_function(k, 0, N_es, y_es=dT_es, color_number=8, size=4)



set_end(title="График изменения мощности от изменения температуры", y_label="$\Delta T, \\text{К}$", x_label="N, Вт", show_origin=True)