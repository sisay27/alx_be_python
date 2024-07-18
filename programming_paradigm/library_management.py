class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"Book '{title}' has been checked out.")
                else:
                    print(f"Book '{title}' is already checked out.")
                return
        print(f"Book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' is already in the library.")
                return
        print(f"Book '{title}' is not in the library.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book_title in available_books:
                print(f"- {book_title}")
        else:
            print("No books are currently available in the library.")



library = Library()

book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_available_books()

library.check_out_book("To Kill a Mockingbird")

library.list_available_books()

library.return_book("To Kill a Mockingbird")

library.list_available_books()