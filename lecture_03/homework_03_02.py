import re

print("\nTask 01")
adwentures_of_tom_sawer = """\n
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

deleting_paragraph = adwentures_of_tom_sawer.replace("\n", " ")
print(deleting_paragraph)

print("\nTask 02")
""" Замініть .... на пробіл
"""
delete_dots = deleting_paragraph.replace(" ....", " ")
print(delete_dots)

print("\nTask 03")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
cleaned_text = ' '.join(delete_dots.split())
print(cleaned_text)

print("\nTask 04")
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = cleaned_text.count("h")
print(f"Кількість літери 'h' у тексті: {count} штук.")

print("\nTask 05")
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = cleaned_text.split()
count_start_upper = sum(1 for word in words if word[0].isupper())
print(f"Кількість слів з великої літери в тексті {count_start_upper} штук.")

print("\nTask 05")
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = cleaned_text.find("Tom")
second_position = cleaned_text.find("Tom", first_position + 1)
print(f"Слово Tom зустрічається на {second_position} позиції.")

print("\nTask 07")
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawyer = cleaned_text
adventures_of_tom_sawyer_sentences = re.split(r'(?<=[.!?]) +', adventures_of_tom_sawyer)
print(adventures_of_tom_sawyer_sentences)

print("\nTask 08")
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
lower = adventures_of_tom_sawyer_sentences[3].lower()
print(lower)

print("\nTask 09")
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False

for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith("By the time"):
        found = True
        break
if found:
    print("Речення починається з 'By the time'")
else:
    print("Речень, що починаються з 'By the time', не знайдено.")


print("\nTask 10")
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adventures_of_tom_sawyer_sentences[-1].split()
word_count_last_sentence = len(last_sentence_words)
print(f"Кількість слів у останньому реченні: {word_count_last_sentence}")