print("\nTask 01-03")
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat."
—— so long as I get somewhere," 
Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі """
print("\nTask 04")

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
_black_sea = 436402
print("Площа Чорного моря = " + str(_black_sea) + " км2;")

_azov_sea = 37800
print("Площа Азовського моря = " + str(_azov_sea) + " км2;")

print("Для того, щоб знайти загальну площу обох морів, потрібно знайти їх суму:")
area = _black_sea + _azov_sea
print("Площа Чорного моря + площа Азовського моря = " + str(_black_sea) + " + " + str(_azov_sea) + " = " + str(area))
print("Відповідь: разом Чорне та Азовське моря займають " + str(area) + " км2")

print("\nTask 05")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
stoks = 3
print(f"Кількість складів: {stoks}.")

product = 375291
print(f"Кількість товарів: {product} штук.")

first_second = 250449
print(f"Загальна кількість товарів на першому та другому складах: {first_second} штук.")

second_third = 222950
print(f"Загальна кількість товарів на другому та третьому складах: {second_third} штук.")

print("\nДля того, щоб знайти кількість товарів на першому складі потрібно з загальної кількості складів відняти кількість товарів, яка зберігається на другому та третьому складах.")
first_stock = product-second_third
print(f"Кількість товарів на першому складі: {first_stock} штук")

print("\nДля того, щоб знайти кількість товарів на третьому складі потрібно з загальної кількості складів відняти кількість товарів, яка зберігається на першому та другому складах.")
third_stock = product-first_second
print(f"Кількість товарів на третьому складі: {third_stock} штук")

print("\nДля того, щоб знайти кількість товарів на третьому складі потрібно з загальної кількості складів відняти кількість товарів, яка зберігається на першому та третьому складах.")
second_stock = product-first_stock-third_stock
print(f"Кількість товарів на другому складі: {second_stock} штук")
print(f"\nВідповідь: на першому складі {first_stock} товара, на другому складі {second_stock} товара, на третьому складі {third_stock} товара.")


print("\nTask 06")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
mounth = 18
monthly_payment = 1179
print("Для того, щоб знайти загальну вартість комп'ютера потрібно місячний платіж помножити на кількість місяців оплати частинами.")
print("Кількість платежів: " + str(mounth) + " місяців")
print("Місячний платіж: " + str(monthly_payment) + " грн")
computer_price = mounth * monthly_payment
print("Тоді, вартість комп'ютера дорівнює: " + str(mounth) + " * " + str(monthly_payment) +" = "+ str(computer_price) + " грн")
print(f"Відповідь: вартість комп'ютера дорівнює: {computer_price} грн")


print("\nTask 07")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"а) {8019%8}")
print(f"b) {9907%9}")
print(f"c) {2789%5}")
print(f"d) {7248%6}")
print(f"e) {7128%5}")
print(f"f) {19224%9}")



print("\nTask 08")
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 4*274
midle_pizza = 2*218
juice = 4*35
cake = 1*350
water = 3*21

print("Велика піца: " + str(big_pizza) + " грн")
print("Середня піца: " + str(midle_pizza) + " грн")
print("Сік: " + str(juice) + " грн")
print("Торт: " + str(cake) + " грн")
print("Вода: " + str(water) + " грн")
basket_sum = big_pizza + midle_pizza + juice+cake + water
print(f"Відповідь: загальна вартість: {basket_sum} грн" )



print("\nTask 09")
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo = 232
print(f"Кількість фотографій: {photo} штук")
pages = 8
print(f"Кількість сторінок: {pages} штук")
quantity_pages = photo/pages
print(f"Відповідь: Ігорю знадобиться {int(quantity_pages)} сторінок.")

print("\nTask 10")
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
print(f"Дистанція: {distance} км")
one_km = 9/100
print(f"Витрати пального на один кілометр: {one_km} літрів")
print(f"Витрати пального на всю відстань: {distance*one_km} літри")
fuel_consumption = distance*one_km
tank = 48
stations=fuel_consumption/tank
print(f"Для обчислення кількості заправок необхідно всю кількість пального поділити на ємність баку, ітого виходить: {int(stations)} заправки")
print(f"Відповідь: а) {int(fuel_consumption)} літри на всю відстань, б) {int(stations)} заправки")



