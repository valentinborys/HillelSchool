# Завдання 1 - Рахування унікальних символів в строці

unique = (str(input("Введіть значення: ")))

unique_list = []

for letter in unique:
    if letter == letter:
        unique_list.append(letter.lower())

set_unique = set(unique_list)

if len(set_unique) >= 10:
    print("Кількість унікальних символів більше чи дорівнює десяти:", True)
else:
    print("Кількість унікальних символів менше десяти:", False)


# print(set_unique)