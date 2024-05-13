from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius * self.radius), 2)

    def perimeter(self):
        return round((2 * math.pi * self.radius), 2)


width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

# Площа для прямокутника
area_rect = Rectangle(width, height)
print(f"Площа прямокутника: {area_rect.area()}")

# Периметр для прямокутника
perimeter_rect = Rectangle(width, height)
print(f"Периметр прямокутника: {perimeter_rect.perimeter()}")

print("")
side = int(input("Введіть сторону квадрату: "))

# Площа та периметр для квадрата
square = Square(side)
print(f"Площа квадрату: {square.area()}")
print(f"Периметр квадрату: {square.perimeter()}")


# Площа та периметр для кругу
print("")
radius = float(input("Введіть радіус кола: "))
circle = Circle(radius)
print(f"Площа кола: {circle.area()}")
print(f"Периметр/довжина кола: {circle.perimeter()}")

print("")

# Виведення через цикл:
print("Всі відповіді:")
all_answers = [area_rect.area(), perimeter_rect.perimeter(), square.area(), square.perimeter(), circle.area(), circle.perimeter()]
test = ["Площа прямокутника", "Периметр прямокутника", "Площа квадрата", "Периметр квадрата", "Площа кола", "Периметр/довжина прямокутника"]

for i in range(len(all_answers)):
    print(f"{test[i]}: {all_answers[i]}")