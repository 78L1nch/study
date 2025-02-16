epsilon = float(input("Введите значение epsilon: "))

n = 1
a_n = 1 / ((n + 1) ** 2)

while abs(a_n) >= epsilon:
    n += 1
    a_n = 1 / ((n + 1) ** 2)

print(f"Наименьший номер n = {n}, a_n = {a_n:.6f}")