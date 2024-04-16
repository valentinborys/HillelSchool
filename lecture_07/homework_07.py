# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# # task 2
# """  Написати функцію, яка обчислює суму двох чисел.
# """
#
# x = int(input("Введіть перше число: "))
# y = int(input("Введіть друге число: "))
#
# def sum (x, y):
#     return x + y
#
# print(f"Сума двох значень: {sum(x,y)}")

# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел.
# """
#
# text = input("\nВведіть через кому список значень: ")
# average = text.split(", ")
# new_average = list(map(int, average))
#
# sum_list = sum(new_average)
# print("Сума всіх значень у списку:", sum_list)
#
# len_list = len(new_average)
#
# print("Довжина списку:", len_list)
# print("Середнє арифметичне:", sum_list/len_list)


# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# """
#
# input_string = input("\nВведіть текст: ")
#
# def text(string):
#     reversed_string = string[::-1]
#     return reversed_string
#
# reversed_input = text(input_string)
# print("Рядок у зворотньому порядку:", reversed_input)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

text = str(input("\nВведіть слова: "))
def the_most_long_word(text):
    splite_text = text.split(" ")
    longest_word = ""

    for word in splite_text:
        if  len(word) > len(longest_word):
            longest_word = word

    return longest_word

print("Найдовше слово:", the_most_long_word(text))

# # task 6
# """  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
# def find_substring(str1, str2):
#
#     return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1
#
# # task 7
# # task 8
# # task 9
# # task 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """