## task 8
print("TASK 8")

original_list = [11, 2, 30, 52, 71, 8, 10, 51, -2, 6]
new_list = []

def division(lst):
    for element in lst:
        if element % 2 == 0:
            new_list.append(element)
    total_sum = sum(new_list)
    return new_list, total_sum

even_numbers, total_sum = division(original_list)

print("Вхідний список:", original_list)
print("Список значень, які діляться на два:", even_numbers)
print("Сума значень, які діляться на два:", total_sum)