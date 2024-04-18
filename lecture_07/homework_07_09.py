## task 9
print("TASK 9")

word = input('Введіть текст з літерою "h" або "H": ').lower()
char_to_check = "h"

def compare_words(word):
    while True:
        if char_to_check in word:
            print('В тексті є літера "h" або "H"')
            break

        else:
            print('В тексті немає літери "h" або "H"')
            word = input('\nВведіть слово з літерою "h": ').lower()

compare_words(word)