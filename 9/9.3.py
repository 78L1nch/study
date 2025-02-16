x = [1, 3, 5, 7, 9]
y = [2, 3, 6, 7, 10]
z = [3, 4, 7, 8, 11]

p, q, r = len(x), len(y), len(z)
i = j = k = 0

found = False

while i < p and j < q and k < r:
    if x[i] == y[j] == z[k]:
        print(f"Общее число: {x[i]}")
        found = True
        break
    elif x[i] < y[j]:
        i += 1
    elif y[j] < z[k]:
        j += 1
    else:
        k += 1

if not found:
    print("Общего числа нет")