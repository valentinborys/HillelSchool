# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def numbers(n):
    for num in range(0, n+1):
        if num % 2 == 0:
            yield num

N = 10
for even in numbers(N):
    print(even)

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = 200
for num in fibonacci(n):
    print(num)

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
def reverse(x):
    yield ''.join(reversed(x))

result = next(reverse("Test"))
print(result)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
def even_numbers(n):
    current = 0
    while current <= N:
        if current % 2 == 0:
            yield current
        current += 1

n = 10
for num in even_numbers(n):
    print(num)


# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")

        return result

    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3, 5)


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred in {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

result = divide(5, 0)

result = divide(10, 2)
print(result)