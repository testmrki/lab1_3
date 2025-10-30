# test.py
from lib import count_common_elements


def test_count_common_elements():
    """Тестирование функции count_common_elements"""

    # Тест 1: Обычный случай (из примера)
    result = count_common_elements([1, 2, 3, 4], [2, 3, 5], [0, 2, 3, 7])
    assert result == 2, f"Ожидалось 2, получено {result}"
    print("✓ Тест 1 пройден: обычный случай")

    # Тест 2: Все элементы одинаковые
    result = count_common_elements([1, 2, 3], [1, 2, 3], [1, 2, 3])
    assert result == 3, f"Ожидалось 3, получено {result}"
    print("✓ Тест 2 пройден: все элементы одинаковые")

    # Тест 3: Нет общих элементов
    result = count_common_elements([1, 2], [3, 4], [5, 6])
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Тест 3 пройден: нет общих элементов")


if __name__ == "__main__":
    test_count_common_elements()
    print("Все тесты пройдены успешно!")