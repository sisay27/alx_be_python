from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

    book1 = Book("Harry Potter","J. K. Rowling","1997")

    print(book1)
    print(repr(book1))
    print(str(book1))
    del book1


if __name__ == "__main__":
    main()