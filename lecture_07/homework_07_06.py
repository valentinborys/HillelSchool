## task 6
print("TASK 6")

"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

str1 = str(input("Введіть першу строку: "))
str2 = str(input("Введіть другу строку: "))

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

result = find_substring(str1, str2)

if result != -1:
    print("Позиція елемента:", result)
else:
    print (f"Другий рядок не є підрядником першого: {result}")