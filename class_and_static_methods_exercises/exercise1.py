# Exercise 1: Class Methods for Counting Instances Instruction:

# Create a class Book with a class variable total_books to count the number of book instances created.
# Implement a class method display_total_books() to display the total number of books created.


class Book:
    total_books = []

    def __init__(self):

        Book.total_books.append(self)

    @classmethod
    def display_total_books(cls):
        print(f"Total instances created:{len(cls.total_books)}")

        # or


class Book1:
    total_books = 0  # Class variable to count instances created

    def __init__(self):
        Book1.total_books += 1  # Increment by 1 upon instance creation.

    @classmethod
    def display_total_books(cls):
        print(f"Total instances created:{cls.total_books}")


book1 = Book()
book2 = Book()
Book.display_total_books()

book3 = Book1()
book4 = Book1()
book5 = Book1()
Book1.display_total_books()
