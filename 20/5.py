def to_decimal(number, base):
    return int(number, base)

def from_decimal(number, base):
    result = ""
    while number > 0:
        result = str(number % base) + result
        number //= base
    return result if result else "0"

def add(a, b, base):
    return from_decimal(to_decimal(a, base) + to_decimal(b, base), base)

def subtract(a, b, base):
    return from_decimal(to_decimal(a, base) - to_decimal(b, base), base)

def multiply(a, b, base):
    return from_decimal(to_decimal(a, base) * to_decimal(b, base), base)

def divide(a, b, base):
    return from_decimal(to_decimal(a, base) // to_decimal(b, base), base)

def power(base_num, exponent, base):
    return from_decimal(to_decimal(base_num, base) ** to_decimal(exponent, base), base)

def sort_array(arr, base):
    arr_dec = [to_decimal(num, base) for num in arr]
    arr_dec.sort(reverse=True)
    return [from_decimal(num, base) for num in arr_dec]

base = int(input("Введите основание системы счисления (2-9): "))
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

def is_valid(number, base):
    for digit in number:
        if int(digit) >= base:
            return False
    return True

if not is_valid(num1, base) or not is_valid(num2, base):
    print("Ошибка: число содержит цифры, превышающие основание системы счисления.")
else:
    print("Сложение:", add(num1, num2, base))
    print("Вычитание:", subtract(num1, num2, base))
    print("Умножение:", multiply(num1, num2, base))
    print("Деление:", divide(num1, num2, base))
    print("Степень:", power(num1, num2, base))

    arr = input("Введите числа через пробел для сортировки: ").split()
    if all(is_valid(num, base) for num in arr):
        sorted_arr = sort_array(arr, base)
        print("Отсортированный массив:", sorted_arr)
    else:
        print("Ошибка: одно из чисел содержит цифры, превышающие основание системы счисления.")