"""
Module: book_manager.py

This module defines the BookManager class, which contains methods to perform CRUD operations on books
in the Library CLI Application.
"""

from db.storage import DataManager
from models.book_model import Book
from utils.cli import CLI
from utils.logger import LibraryLogger

class BookManager(DataManager):
    """
    The BookManager class contains methods required to CRUD Books in the Library CLI Application.
    """
    def __init__(self):
        """
        Initialize a new BookManager instance, inheriting from DataManager and specifying the data key as "books".
        """
        super().__init__("books")

    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.
        
        Parameters:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - isbn (str): The ISBN of the book.
        """
        data = self.get_data()
        if self.isbn_is_unique(isbn):
            new_book = Book(title, author, isbn)
            data.append(vars(new_book))
            self.save_data(data)
            CLI.display_message("Book entry created!")
            # Log the book addition operation
            message = f"A book with Title: {title}, author: {author}, isbn number: {new_book.isbn} has been added"
            self.generate_log(message, action="Book Added")
        else:
            CLI.display_message("Invalid isbn. Already assigned to other book")

    def list_books(self):
        """
        List all books in the library.
        """
        data = self.get_data()
        for book_data in data:
            book = Book(**book_data)
            CLI.display_message(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.availability}")

    def search_books(self, keyword):
        """
        Search for books in the library based on a keyword.
        
        Parameters:
        - keyword (str): The keyword to search for in book titles, authors, or ISBNs.
        """
        data = self.get_data()
        results = [Book(**book_data) for book_data in data if
                   keyword.lower() in book_data["title"].lower() or
                   keyword.lower() in book_data["author"].lower() or
                   keyword.lower() in book_data["isbn"].lower()]
        for result in results:
            CLI.display_message(f"Title: {result.title}, Author: {result.author}, ISBN: {result.isbn}, Available: {result.availability}")

    def is_available(self, isbn):
        """
        Check the availability of a book in the library based on its ISBN.
        
        Parameters:
        - isbn (str): The ISBN of the book.
        """
        data = self.get_data()
        book = [Book(**book_data) for book_data in data if                   
                   isbn.lower() in book_data["isbn"].lower()]
        if book:
            book = book[0]
            if book.availability:
                CLI.display_message(f"Book with Title: {book.title}, Author: {book.author} is available")
            else:
                CLI.display_message(f"Book with Title: {book.title}, Author: {book.author} is not available")
        else:
            CLI.display_message(f"Book with isbn: {isbn} does not exist")

    def isbn_is_unique(self, isbn):
        """
        Check if the provided ISBN is unique in the library database.
        
        Parameters:
        - isbn (str): The ISBN to check for uniqueness.
        
        Returns:
        - bool: True if the ISBN is unique, False otherwise.
        """
        data = self.get_data()
        book = [Book(**book_data) for book_data in data if                   
                   isbn.lower() in book_data["isbn"].lower()]       
        if len(book) > 0:
            return False
        else:
            return True

    def generate_log(self, message, action=None, level='info'):
        """
        Generate a log message.

        Args:
            message (str): The main content of the log message.
            action (str, optional): The action associated with the log message. Defaults to None.
            level (str, optional): The log level (e.g., 'info', 'warning', 'error'). Defaults to 'info'.
        """
        LibraryLogger.generate_log(level=level, origin="BookManager", message=message, action=action)
        