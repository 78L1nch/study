x = 1


import math

a = 1
b = 1
c = -198

discriminant = b**2 - 4*a*c
y1 = (-b + math.sqrt(discriminant)) / (2*a)
y2 = (-b - math.sqrt(discriminant)) / (2*a)

y = int(y1) if y1 > 0 else int(y2)

a = 1
b = 14 - 13
c = -36

discriminant = b**2 - 4*a*c
z1 = (-b + math.sqrt(discriminant)) / (2*a)
z2 = (-b - math.sqrt(discriminant)) / (2*a)

z = int(z1) if z1 > y else int(z2)

a = 1
b = 15 - 14
c = -236

discriminant = b**2 - 4*a*c
school1 = (-b + math.sqrt(discriminant)) / (2*a)
school2 = (-b - math.sqrt(discriminant)) / (2*a)

school = int(school1) if school1 > z else int(school2)

print(f"Номер дома Петра: {x}")
print(f"Номер дома школы: {school}")