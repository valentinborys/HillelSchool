## task 3
print("TASK 3")

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

text = input("Введіть через кому список значень: ")
average = text.split(", ")
new_average = list(map(int, average))

sum_list = sum(new_average)
print("Сума всіх значень у списку:", sum_list)

len_list = len(new_average)

print("Довжина списку:", len_list)
print("Середнє арифметичне:", sum_list/len_list)