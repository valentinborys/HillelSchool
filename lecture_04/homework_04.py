people_records = [
        ('John', 'Doe', 28, 'Engineer', 'New York'),
        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
        ('David', 'Miller', 33, 'Software Developer', 'Austin'),
        ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
        ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
        ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
        ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
        ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
        ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
        ('Ava', 'White', 42, 'Journalist', 'San Diego'),
        ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
    ]


people_records.insert(0, ("Valentyn", "Borys", 26, "QA", "Lysychansk"))
print("\nВідповідь на 1-ше питання:", people_records)

people_change = people_records
people_change[1], people_change[5] = people_change[5], people_change[1]


print("\nВідповідь на 2-ге питання:", people_change)

x = people_change[6][2]
y = people_change[10][2]
f = people_change[13][2]

if x and y and f >= 30:
    print("\nВідповідь на 3-тє питання: всі елементи мають значення більше 30")
else:
    print("\nВідповідь на 3-тє питання: не всі елементи мають значення більше 30")


test = ["Test1", "Test2", "Test3", "Test4"]

if "Test3" in test:
    if "Test3" in test:
        test[test.index("Test3")] = "HHH"

print(test)





