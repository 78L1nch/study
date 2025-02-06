# Радин Вадим
#
""""Практическая 10 Вариант 15 №3 Для заданной квадратной матрицы найти значения k, при которых k-я ее строка
совпадает с k-м столбцом."""
N = int(input("Введите размер матрицы N: "))

matrix = []
for i in range(N):
    row = []
    for j in range(N):
        value = float(input(f"Введите элемент [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

k_values = []
for k in range(N):
    is_equal = True
    for i in range(N):
        if matrix[k][i] != matrix[i][k]:
            is_equal = False
            break
    if is_equal:
        k_values.append(k)

if k_values:
    print("Значения k, при которых k-я строка совпадает с k-м столбцом:", k_values)
else:
    print("Нет значений k, при которых k-я строка совпадает с k-м столбцом.")