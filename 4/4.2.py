import math

n = int(input("Введите натуральное число n: "))
x = float(input("Введите действительное число x: "))

S = 0
current = x

for _ in range(n):
    S += math.sin(current)
    current = math.sin(current)

print(f"Сумма S = {S}")