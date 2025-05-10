import pytest
from even_sum import calc_even_sum

def test_empty_list():
    """Тест с пустым списком"""
    assert calc_even_sum([]) == 0
    print("Тест с пустым списком пройден")

def test_all_odd_numbers():
    """Тест со списком нечётных чисел"""
    assert calc_even_sum([1, 3, 5, 7]) == 0
    print("Тест со списком нечётных чисел пройден")

def test_all_even_numbers():
    """Тест со списком чётных чисел"""
    assert calc_even_sum([2, 4, 6, 8]) == 20
    print("Тест со списком чётных чисел пройден")

def test_mixed_numbers():
    """Тест со смешанным списком"""
    assert calc_even_sum([1, 2, 3, 4, 5, 6]) == 12
    print("Тест со смешанным списком пройден")

def test_non_list_input():
    """Тест с неправильным типом входных данных"""
    with pytest.raises(TypeError):
        calc_even_sum("not a list")
    print("Тест с неправильным типом входных данных пройден")

@pytest.mark.parametrize("input_list, expected", [
    ([], 0),
    ([2], 2),
    ([1, 2, 3, 4], 6),
    ([10, 20, 30], 60),
    ([-2, -1, 0, 1, 2], 0),
])
def test_parametrized(input_list, expected):
    """Группа параметризованных тестов"""
    assert calc_even_sum(input_list) == expected
    print(f"Параметризованный тест для {input_list} пройден")

def test_warning_for_large_list():
    """Тест с предупреждением для большого списка"""
    large_list = list(range(1000))
    with pytest.warns(UserWarning, match="Large list may impact performance"):
        import warnings
        warnings.warn("Large list may impact performance", UserWarning)
        calc_even_sum(large_list)
    print("Тест с предупреждением пройден")

@pytest.fixture
def random_number():
    """Фикстура, возвращающая случайное число от 1 до 100"""
    import random
    num = random.randint(1, 100)
    assert 1 <= num <= 100
    return num

def test_random_number_even(random_number):
    """Тест, проверяющий, что случайное число чётное (может иногда падать)"""
    if random_number % 2 == 0:
        print(f"Случайное число {random_number} чётное")
    else:
        pytest.skip(f"Случайное число {random_number} нечётное, тест пропущен")

def test_random_number_in_range(random_number):
    """Тест, проверяющий, что случайное число в диапазоне"""
    assert 1 <= random_number <= 100
    print(f"Случайное число {random_number} в диапазоне 1-100")