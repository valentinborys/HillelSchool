list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for element in list:
    try:
        numbers = [int(num) for num in element.split(',')]
        total_sum = sum(numbers)

        print(f'Сумма значень для строки "{element}" = {total_sum}')

    except ValueError as ve:
        print("Не можу це зробити:", ve)



