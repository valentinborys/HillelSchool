class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

library = Library()

book1 = Book("Гаррі Поттер та Філософський камінь", "Джоан Роулінг")
book2 = Book("Гаррі Поттер та Таємна кімната", "Дж. Роулінг")
book3 = Book("Гаррі Поттер і В'язень Азкабану", "Роулінг Джоан")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Отримуємо всі книги з бібліотеки і виводимо їх
print("Книги в бібліотеці:")
for book in library.get_books():
    print(f"{book.title} - {book.author}")
