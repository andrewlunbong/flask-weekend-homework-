from models.book import *

book1 = Book("Rich Dad Poor Dad", "By Robert Kiyosaki", "Finance")
book2 = Book("The Great Gatsby", "By Scott Fitzgerald", "Fiction")
book3 = Book("Dune", "By Frank Herbert", "Si-Fi")
book4 = Book("Harry Potter", "By JK Rowlin", "Fantasy")


book_list = [book1, book2, book3, book4]

def add_new_books(book):
    if book not in book_list:
        book_list.append(book)

def delete_book(book_name):
    for book in book_list:
        if book.name == book_name:
            book_list.remove(book)
