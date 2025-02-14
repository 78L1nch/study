import math

n = int(input("Введите натуральное число n: "))
x = float(input("Введите действительное число x: "))

if n < 1:
    print("Ошибка: n должно быть натуральным числом")
else:
    S = 0.0
    current = math.sin(x)
    for _ in range(n):
        S += current
        current = math.sin(current)
    print("Сумма S =", S)