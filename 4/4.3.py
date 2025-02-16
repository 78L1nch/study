import math

a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
h = float(input("Введите шаг h: "))

print("x\t\tF(x)")
print("---------------------")

x = a
while x <= b:
    F = 0.5 * (1 / math.tan(x / a)) + 4
    print(f"{x:.2f}\t\t{F:.4f}")
    x += h