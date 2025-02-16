n = 53042

digits = list(str(n))

digits.sort()

smallest_number_str = ''.join(digits)

smallest_number = int(smallest_number_str)

print(f"Наименьшее число из цифр {n}: {smallest_number}")