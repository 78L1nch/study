from itertools import permutations

letters = ['X', 'P', 'У', 'С', 'Т', 'Г', 'Р', 'О', 'Х', 'О', 'Т']
unique_letters = list(set(letters))  # Убираем дубликаты

for digits in permutations('0123456789', len(unique_letters)):
    mapping = {letter: digit for letter, digit in zip(unique_letters, digits)}

    xpyst = int(''.join([mapping[letter] for letter in ['X', 'P', 'У', 'С', 'Т']]))
    grohot = int(''.join([mapping[letter] for letter in ['Г', 'Р', 'О', 'Х', 'О', 'Т']]))
    pppppp = int(''.join([mapping['P']] * 12))

    if xpyst * grohot == pppppp:
        print("Найдено решение:")
        print(f"XPУСТ = {xpyst}, ГРОХОТ = {grohot}, PPPPPPPPPPPP = {pppppp}")
        print("Соответствие букв и цифр:", mapping)
        break
else:
    print("Решение не найдено.")