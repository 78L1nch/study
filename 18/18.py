coefficients = [1, 2, 3]

x = 1 + 2j

result = 0

for power, coeff in enumerate(coefficients):
    result += coeff * (x ** power)

print(f"Значение многочлена в точке {x} равно {result}")