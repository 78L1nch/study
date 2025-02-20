def are_all_digits_unique(N):
    num_str = str(N)
    return len(num_str) == len(set(num_str))

N = int(input("Введите четырехзначное число: "))

print(are_all_digits_unique(N))