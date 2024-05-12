class Student:
    def __init__(self, name, surname, age, avarage_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_mark = avarage_mark

    def change(self, new_avarage_mark):
        self.average_mark = new_avarage_mark



student = Student("Борис", "Валентин", 26, 80)

print(f"Ім'я та прізвище: {student.name} {student.surname}")
print(f"Вік: {student.age}")
print(f"Середня оцінка: {student.average_mark}")

student.change(100)
print("")

print("Оновлені дінні:")
print(f"Ім'я та прізвище: {student.name} {student.surname}")
print(f"Вік: {student.age}")
print(f"Середня оцінка {student.average_mark}")
