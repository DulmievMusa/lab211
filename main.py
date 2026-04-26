from mnk import *
from my_library import *
from math import pi

d = 0.95
L = 125 * (10 ** -3)

h_es, v_es, t_es = get_all_columns_from_file("data1.csv")
q_es = [(v_es[i] * (10 ** -6)) / t_es[i] for i in range(len(v_es))]
h_es = [h/1000 for h in h_es]

k, b, sigma_k, sigma_b = linear_regression(h_es, q_es)

print(f"vyaskost: {(pi * ((0.95 * 10 ** -3) ** 4) * 1000 * 9.81)/(8 * 125 * (10 ** -3) * k)}")


print("k", k)
paint_line_function(k, b, h_es, y_es=q_es)



set_end()