p = float(input("Введите число p: "))
q = float(input("Введите число q: "))

a = p * q**2
b = p**2 + p * q

if a > b:
    c = a * (a - b)
elif a == b:
    c = a**3
else:
    c = p - q

d = c * (p + q)

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)