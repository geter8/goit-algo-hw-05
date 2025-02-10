
def caching_fibonacci():
    cache = {}  # Используем словарь для кэширования
    def fibonacci(n):
        if n < 2:  # Базовый случай
            return n
        if n in cache:  # Проверяем, есть ли значение в кэше
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Кэшируем результат
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


