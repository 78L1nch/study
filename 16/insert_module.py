def insert_into_sorted_list(sorted_list, value):
    """
    Вставляет значение в упорядоченный список, сохраняя его упорядоченность.

    :param sorted_list: Упорядоченный список чисел.
    :param value: Значение, которое нужно вставить.
    :return: Упорядоченный список с вставленным значением.
    """
    for i in range(len(sorted_list)):
        if sorted_list[i] > value:
            sorted_list.insert(i, value)
            return sorted_list
    sorted_list.append(value)
    return sorted_list