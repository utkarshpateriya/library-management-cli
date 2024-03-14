"""
Module: book_model.py

Contains the Book class representing entities used in the Library CLI Application.
"""

class Book:
    """
    The Book class represents a book entity in the library.
    """
    def __init__(self, title, author, isbn, availability=True):
        """
        Initialize a Book object with title, author, ISBN, and availability.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            availability (bool, optional): Availability status of the book. Defaults to True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        