import math
x = 2 # 1 переменная
y = 3 # 2 переменная
numerator = x**14 + math.exp(y - 1)
denominator = 1 + x**y
root_part = (abs(y - x)**2 / 2) + abs(y - x)**3
h = (numerator / denominator) * root_part**(1/3)
print(f"Значение h: {h}") # ВЫВОД РЕЗУЛЬТАТА
