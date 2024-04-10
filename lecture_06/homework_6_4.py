# Завдання 4 - Сумуємо числа

list = [11, 2, 30, 52, 71, 8, 10, 51, -2, 6]
new_list = []

for element in list:
    if element %2 == 0:
        new_list.append(element)

sum = 0

for element in new_list:
    sum += element

print("Вхідний список:", list)
print("Список значень, які діляться на два:", new_list)
print("Сума значень, які діляться на два:", sum)

