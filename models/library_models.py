"""
Module: library_models.py

Contains the Book and User classes representing entities used in the Library CLI Application.
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


class User:
    """
    The User class represents a user entity in the library.
    """

    def __init__(self, name, user_id):
        """
        Initialize a User object with name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID of the user.
        """
        self.name = name
        self.user_id = user_id