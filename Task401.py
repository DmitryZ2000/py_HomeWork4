# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from math import pi
d = input('Задайте точность числа, например 0.001 : ')
k = len(d) - 2
print(f'Число pi с заданной точностью {d} составляет {round(pi, k)}')