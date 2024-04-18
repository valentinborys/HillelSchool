## task 11
print("TASK 11***")

def format_date(day_input, month_input, year_input, separator):
    print(f"{day_input}{separator}{month_input}{separator}{year_input}")

day_input = input("Введіть день: ")
month_input = input("Введіть місяць: ")
year_input = input("Введіть рік: ")
separator = input("Введіть сепаратор: ")

format_date(day_input, month_input, year_input, separator)