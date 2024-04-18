## task 5
print("TASK 5")

"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

text = str(input("Введіть слова через пробіл: "))
def the_most_long_word(text):
    splite_text = text.split(" ")
    longest_word = ""

    for word in splite_text:
        if  len(word) > len(longest_word):
            longest_word = word

    return longest_word

print("Найдовше слово:", the_most_long_word(text))