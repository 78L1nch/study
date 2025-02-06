# Радин Вадим
#
""""Практическая 10 Вариант 15 №2
Дана действительная матрица размером n х m, все элементы которой различны.
В каждой строке этой матрицы выбрать элемент с наименьшим значением, азатем среди них выбрать элемент с наибольшим значением. Указать индексыэтого элемента
"""
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        value = float(input(f"Введите элемент [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

min_elements = []
for i in range(n):
    min_value = matrix[i][0]
    min_index = 0
    for j in range(1, m):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = j
    min_elements.append((min_value, i, min_index))

max_of_min = min_elements[0]
for element in min_elements[1:]:
    if element[0] > max_of_min[0]:
        max_of_min = element

print("Индексы элемента с наибольшим значением среди минимальных:")
print("Строка:", max_of_min[1], "Столбец:", max_of_min[2])