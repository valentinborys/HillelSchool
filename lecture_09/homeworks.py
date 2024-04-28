# Task 1
def multiplication_table(number):
    multiplier = 1
    table = ""

    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            pass
        table += str(number) + "x" + str(multiplier) + "=" + str(result) + "\n"
        multiplier += 1

    return table


# Task 2
def sum (x, y):
    return x + y


# Task 3
def text(string):
    reversed_string = string[::-1]
    return reversed_string


# Task 4
def filter_strings(lst1):
    lst2 = []
    for string in lst1:
        if isinstance(string, str):
            lst2.append(string)
    return lst2

    print("Всі строки в списку: ", lst2)

filter_strings([1, "Test1", "Test2", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])