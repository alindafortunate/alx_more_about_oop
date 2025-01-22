# Exercise 2: Magic Methods (str and repr) Instructions:

# Create a Book class with attributes like title, author, and pages.
# Implement both __str__ and __repr__ magic methods to provide different
#  string representations of the book object.


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"

    def __repr__(self):
        return f"{self.title} by {self.author}"


if __name__ == "__main__":

    book = Book("Introduction to Python", "Alinda Fortunate", 100)
    print(book)
    print(type(book))
    print(type(book.author))
