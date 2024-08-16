# Задача "А как делить?":
from fake_math import divide as f_m
from true_math import divide as t_m
result_1 = f_m(69, 3)
result_2 = f_m(3, 0)
result_3 = t_m(49, 7)
result_4 = t_m(15, 0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)