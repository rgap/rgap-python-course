# Python Version: Python has supported object comparison since version 1.0.

# Object Comparison in Python
# Objects can be compared using the comparison operators like ==, !=, <, >, etc.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Overriding the __eq__ method to compare books by their title and author
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


# Creating two book objects
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

# Comparing objects
print(
    f"book1 is equal to book2: {book1 == book2}"
)  # Outputs: book1 is equal to book2: True
print(
    f"book1 is equal to book3: {book1 == book3}"
)  # Outputs: book1 is equal to book3: False

# Note: Object comparison in Python can be customized by overriding comparison magic methods like __eq__, __lt__, etc.
# This allows objects to be compared based on their attributes, enabling more meaningful comparisons.
