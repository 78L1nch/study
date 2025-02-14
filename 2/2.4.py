import math
a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
h = float(input("Введите шаг h: "))
x = a
while x <= b + 1e-9:
    # Проверка, не равен ли sin(x/4) нулю (с учетом погрешности)
    if abs(math.sin(x / 4)) < 1e-9:
        print(f"{x:} | не определена")
    else:
        ctg_term = 1 / math.tan(x / 4)
        F_x = 0.5 * ctg_term + 4
        print(f"{x:9.4f} | {F_x:9.4f}")
    x += h