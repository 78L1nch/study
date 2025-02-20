from insert_module import insert_into_sorted_list


def main():
    sorted_list = []
    n = int(input("Введите количество элементов в списке: "))
    for i in range(n):
        num = int(input(f"Введите элемент {i + 1}: "))
        sorted_list.append(num)

    if sorted_list != sorted(sorted_list):
        print("Ошибка: список не упорядочен по возрастанию.")
        return

    value = int(input("Введите значение для вставки: "))

    new_list = insert_into_sorted_list(sorted_list, value)

    print(f"Новый список с вставленным значением: {new_list}")


if __name__ == "__main__":
    main()