def input_array(size, array_name):
    """
    Функция для ввода элементов массива.

    :param size: Размер массива.
    :param array_name: Имя массива (для вывода подсказки).
    :return: Введенный массив.
    """
    array = []
    for i in range(size):
        num = int(input(f"Введите элемент {array_name}[{i}]: "))
        array.append(num)
    return array


def print_array(array, array_name):
    """
    Функция для вывода элементов массива.

    :param array: Массив для вывода.
    :param array_name: Имя массива (для вывода подсказки).
    """
    print(f"{array_name}: {array}")


def process_arrays(A, B):
    """
    Функция для обработки массивов A и B.

    :param A: Массив A.
    :param B: Массив B.
    :return: Массивы AB1 и AB2 после всех преобразований.
    """
    A.append(66)
    print_array(A, "A после добавления 66")

    if len(B) > 1:
        B.pop(1)
    print_array(B, "B после удаления второго элемента")

    if len(A) >= 3:
        A.insert(2, 22)
    else:
        print("Ошибка: массив A слишком короткий для вставки на третье место.")
    print_array(A, "A после вставки 22")

    AB1 = A + B
    print_array(AB1, "AB1 после объединения A и B")

    AB1.sort(reverse=True)
    print_array(AB1, "AB1 после сортировки по убыванию")

    AB2 = AB1[1::2]  # Индексация с 1 с шагом 2 (четные места)
    print_array(AB2, "AB2 из элементов на четных местах")

    AB2 = AB2[2:] + AB2[:2]
    print_array(AB2, "AB2 после сдвига на 2 влево")

    return AB1, AB2

def main():
    A = input_array(5, "A")
    B = input_array(8, "B")

    print_array(A, "Исходный массив A")
    print_array(B, "Исходный массив B")

    AB1, AB2 = process_arrays(A, B)

    with open("lab9_3.out", "w") as file:
        file.write(f"AB1: {AB1}\n")
        file.write(f"AB2: {AB2}\n")

    print("Результаты записаны в файл lab9_3.out")


if __name__ == "__main__":
    main()