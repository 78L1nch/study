def has_opposite_pair(a, b, c):
    if (a == -b) or (a == -c) or (b == -c):
        return True
    else:
        return False

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

print(has_opposite_pair(a, b, c))