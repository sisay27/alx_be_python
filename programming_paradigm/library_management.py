class Book:  
    def __init__(self, title, author):  
        self.title = title  
        self.author = author  
        self._is_checked_out = False  # Private attribute to track availability  

    def check_out(self):  
        if not self._is_checked_out:  
            self._is_checked_out = True  
            print(f"'{self.title}' has been checked out.")  
        else:  
            print(f"'{self.title}' is already checked out.")  

    def return_book(self):  
        if self._is_checked_out:  
            self._is_checked_out = False  
            print(f"'{self.title}' has been returned.")  
        else:  
            print(f"'{self.title}' is already available.")  


class Library:  
    def __init__(self):  
        self._books = []  # Private list to store Book instances  

    def add_book(self, book):  
        self._books.append(book)  
        print(f"Added '{book.title}' by {book.author} to the library.")  

    def check_out_book(self, title):  
        for book in self._books:  
            if book.title == title:  
                book.check_out()  
                return  
        print(f"'{title}' is not available in the library.")  

    def return_book(self, title):  
        for book in self._books:  
            if book.title == title:  
                book.return_book()  
                return  
        print(f"'{title}' is not from this library.")  

    def list_available_books(self):  
        available_books = [book for book in self._books if not book._is_checked_out]  
        if available_books:  
            print("Available books:")  
            for book in available_books:  
                print(f"{book.title} by {book.author}")  
        else:  
            print("No books available in the library.")  