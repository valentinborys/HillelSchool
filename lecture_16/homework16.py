from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        super().__init__()

# Площа
    @abstractmethod
    def area(self):
        pass

# Периметр
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self._side = side

    def area(self):
        return self._side * self._side

    def perimeter(self):
        return self._side * 4


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    def area(self):
        return round(math.pi * (self._radius * self._radius), 2)

    def perimeter(self):
        return round((2 * math.pi * self._radius), 2)


width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

area_rect = Rectangle(width, height)

# Площа та периметр прямокутника
print(f"Площа прямокутника: {area_rect.area()}")
print(f"Периметр прямокутника: {area_rect.perimeter()}")

print("")
side = int(input("Введіть сторону квадрату: "))

square = Square(side)

# Площа та периметр квадрату
print(f"Площа квадрату: {square.area()}")
print(f"Периметр квадрату: {square.perimeter()}")

print("")
radius = float(input("Введіть радіус кола: "))

circle = Circle(radius)

# Площа та периметр кола
print(f"Площа кола: {circle.area()}")
print(f"Периметр/довжина кола: {circle.perimeter()}")

print("")

# Вивід через цикл
print("Всі відповіді:")
all_answers = [area_rect.area(), area_rect.perimeter(), square.area(), square.perimeter(), circle.area(), circle.perimeter()]
test = ["Площа прямокутника", "Периметр прямокутника", "Площа квадрата", "Периметр квадрата", "Площа кола", "Периметр/довжина кола"]

for i in range(len(all_answers)):
    print(f"{test[i]}: {all_answers[i]}")
