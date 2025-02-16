toys = input("Введите список игрушек через пробел: ").split()

N = int(input("Введите количество детских садов: "))

kindergartens = []

for i in range(N):
    toys_in_kindergarten = input(f"Введите игрушки для детского сада {i+1} через пробел: ").split()
    kindergartens.append(set(toys_in_kindergarten))

common_toys = set(toys)
for kg in kindergartens:
    common_toys = common_toys & kg
print("Игрушки, которые есть в каждом детском саду:", common_toys)

all_toys_in_kindergartens = set()
for kg in kindergartens:
    all_toys_in_kindergartens = all_toys_in_kindergartens | kg
missing_toys = set(toys) - all_toys_in_kindergartens
print("Игрушки, которых нет ни в одном детском саду:", missing_toys)