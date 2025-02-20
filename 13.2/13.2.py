import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def triangle_perimeter_area(x1, y1, x2, y2, x3, y3):

    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)

    perimeter = a + b + c

    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return perimeter, area

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

perimeter, area = triangle_perimeter_area(x1, y1, x2, y2, x3, y3)

print(f"Периметр треугольника: {perimeter}")
print(f"Площадь треугольника: {area}")