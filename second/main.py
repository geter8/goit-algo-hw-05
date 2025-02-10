import re
from typing import Callable

def generator_numbers(text: str):
    # Шукаємо числа з плаваючою точкою, що відокремлені пробілами
    for match in re.finditer(r'(?<=\s)\d+\.\d+(?=\s)', text):
        yield float(match.group())  # Повертаємо знайдене число як float

def sum_profit(text: str, func: Callable):
    # Генератор надається функцією func, ітеруємо через нього і сумуємо всі числа
    return sum(func(text))  # Підсумовуємо всі числа, які знаходяться в тексті

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Викликаємо sum_profit з передачею функції generator_numbers
result = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {result}")
