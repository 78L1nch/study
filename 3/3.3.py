x = float(input("Введите число x: "))

if x > 3.6:
    F_x = 45 * x**2 + 5
else:
    F_x = (5 * x) / (10 * x**2 + 1)

# Вывод результата
print("F(x) =", F_x)