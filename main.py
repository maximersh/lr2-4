import math
x = 2  
y = 3 
numerator = x**14 + math.exp(y - 1)
denominator = 1 + x**y
root_part = (abs(y - x)**2 / 2) + abs(y - x)**3
h = (numerator / denominator) * root_part**(1/3)
print(f"Значение h: {h}")
