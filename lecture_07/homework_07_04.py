## task 4
print("TASK 4")

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

input_string = input("Введіть текст: ")

def text(string):
    reversed_string = string[::-1]
    return reversed_string

reversed_input = text(input_string)
print("Рядок у зворотньому порядку:", reversed_input)
