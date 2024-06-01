# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
print("TASK 1")
def numbers(n):
    for num in range(0, n+1):
        if num % 2 == 0:
            yield num

N = 10
for even in numbers(N):
    print(even)
print("")

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
print("TASK 2")

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = 200
for num in fibonacci(n):
    print(num)
print("")

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
print("TASK 3")

def reverse(x):
    yield ''.join(reversed(x))

result = next(reverse("Test"))
print(result)

print("")

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
print("TASK 4")
def even_numbers(n):
    current = 0
    while current <= N:
        if current % 2 == 0:
            yield current
        current += 1

n = 10
for num in even_numbers(n):
    print(num)

print("")

# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
print("TASK 5")

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Визвана функція {func.__name__} з аргументами: аргументи={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")

        return result

    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add("ЕУЫЕ")


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