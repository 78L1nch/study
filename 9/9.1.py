A = 10
q = 2
B = [9, 11, 12, 8, 13]
N = len(B)

defective_count = 0

for size in B:
    if size < A - q or size > A + q:
        defective_count += 1

if defective_count > 0:
    print(f"Количество бракованных деталей: {defective_count}")
else:
    print("Бракованных деталей нет")