def count_common_elements(*lists):
# Принимает списки и возвращает количество одинаковых элементов в них.
    # Преобразуем все списки в множества
    sets = [set(lst) for lst in lists]

    # Находим пересечение всех множеств
    common_elements = set.intersection(*sets)
    return len(common_elements)
# Пример
print(count_common_elements([1, 2, 3, 4],[2, 3, 5],[0, 2, 3, 7]))
# Ответ: 2 (общие элементы 2 и 3)
input()
