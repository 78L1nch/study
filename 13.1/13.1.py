def calculate_expression(x):
    numerator = x ** 2 - 7 * x + 10

    denominator = x ** 2 - 8 * x + 12

    if denominator == 0:
        return "Ошибка: Знаменатель равен нулю, деление невозможно."

    result = numerator / denominator
    return result


x = float(input("Введите значение x: "))

result = calculate_expression(x)

print("Результат вычисления:", result)