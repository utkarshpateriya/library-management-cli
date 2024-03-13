"""
Module: library_logger.py

This module defines the LibraryLogger class, which is responsible for logging important events and operations within the Library CLI Application.
"""

import logging

class LibraryLogger:
    """
    The LibraryLogger class provides methods for logging book and user operations.
    """
    
    def __init__(self):
        """
        Initialize the LibraryLogger with logging configuration.
        """
        logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def log_book_added(self, title, author, isbn):
        """
        Log the addition of a book with its title, author, and ISBN.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        logging.info(f"Book added: Title: {title}, Author: {author}, ISBN: {isbn}")

    def log_user_added(self, name, user_id):
        """
        Log the addition of a user with their name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID of the user.
        """
        logging.info(f"User added: Name: {name}, User ID: {user_id}")

    def log_book_checked_out(self, title, user_id):
        """
        Log the checkout of a book by a user with the book's title and the user's ID.

        Args:
            title (str): The title of the book.
            user_id (str): The user ID of the user who checked out the book.
        """
        logging.info(f"Book checked out: Title: {title}, User ID: {user_id}")

    def log_book_checked_in(self, title, user_id):
        """
        Log the check-in of a book by a user with the book's title and the user's ID.

        Args:
            title (str): The title of the book.
            user_id (str): The user ID of the user who checked in the book.
        """
        logging.info(f"Book checked in: Title: {title}, User ID: {user_id}")