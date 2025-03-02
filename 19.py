number_str = input("Введите число: ")
p = int(input("Введите основание системы счисления (2 <= p <= 9): "))

if p < 2 or p > 9:
    print("Основание должно быть от 2 до 9.")
else:
    valid = True
    for digit_char in number_str:
        digit = int(digit_char)
        if digit >= p:
            print(f"Ошибка: цифра {digit} не может быть в системе с основанием {p}.")
            valid = False
            break

    if valid:
        decimal_number = 0
        length = len(number_str)

        for i in range(length):
            digit = int(number_str[i])
            power = length - i - 1
            decimal_number += digit * (p ** power)

        print(f"Число в десятичной системе: {decimal_number}")