num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))


max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

sum_max_min = max_num + min_num

print("Сумма большего и меньшего числа:", sum_max_min)