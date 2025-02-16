m = 1234
n = 5678

m_str = str(m)
n_str = str(n)

common_digit = False

for digit in m_str:
    if digit in n_str:
        common_digit = True
        break

if common_digit:
    print("Да")
else:
    print("Нет")