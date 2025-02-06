# Радин Вадим
#Практическая 10 Вариант 15 №1 Сформировать квадратную матрицу порядка N по формуле
import math

N = int(input("Введите размер матрицы N: "))

matrix = []
for i in range(N):
    row = []
    for j in range(N):
        value = math.sin((i**2 - j**2) / N)
        row.append(value)
    matrix.append(row)

positive_count = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] > 0:
            positive_count += 1

print("Матрица:")
for row in matrix:
    print(row)
print("Количество положительных элементов:", positive_count)