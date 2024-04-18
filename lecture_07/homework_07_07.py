## task 7
print("TASK 7")

unique = str(input("Введіть значення: "))

unique_list = []

def funct(string):
    for element in string:
        if element.lower() not in unique_list:
            unique_list.append(element.lower())

    set_unique = set(unique_list)

    if len(set_unique) >= 10:
        print("Кількість унікальних символів більше чи дорівнює десяти:", True)
    else:
        print("Кількість унікальних символів менше десяти:", False)

funct(unique)
