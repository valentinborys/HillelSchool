## task 10
print("TASK 10")

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

def strings_in_list(lst1):
    for string in lst1:
        if type(string) is str:
            lst2.append(string)
    print("Всі строки в списку: ", lst2)

strings_in_list(lst1)