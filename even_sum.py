
def calc_even_sum(numbers):
    """
    Возвращает сумму всех чётных чисел в списке.

    Args:
        numbers: список чисел

    Returns:
        Сумма чётных чисел

    Raises:
        TypeError: если входной аргумент не является списком
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    return sum(num for num in numbers if num % 2 == 0)