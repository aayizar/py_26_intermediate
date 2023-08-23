"""
Агрегация
"""


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        
    def append_book(self, book):
        self.books.append(book)
        

class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author


library = Library("Центральная библиотека")

b1 = Book("Война и Мир", "Лев Толстой")
b2 = Book("Война и Мир 2", "Лев Толстой")

library.append_book(b1)
library.append_book(b2)
print(library.books)