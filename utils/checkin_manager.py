"""
Module: checkin_manage.py

This module defines the CheckoutManager class, responsible for managing Check In/Out operations in the Library CLI Application.
"""
from utils.user_manager import UserManager
from utils.book_manager import BookManager
from cli import CLI
from models.library_models import Book, User
from logger.library_logger import LibraryLogger

class CheckoutManager:
    """
    CheckoutManager contains all the necessary utilities responsible for Check In/Out's of books.
    """
    def __init__(self):
        """
        Initialize a new CheckoutManager instance.
        """
        self.logger = LibraryLogger()

    def check_out_book(self, user_id, isbn):
        """
        Check out a book to a user based on their user ID and the book's ISBN.

        Args:
            user_id (str): The user ID of the borrower.
            isbn (str): The ISBN of the book to be checked out.
        """
        user_manager = UserManager()
        book_manager = BookManager()

        #Check if user with user_id exists
        user_data_list = user_manager.get_data()
        user = None

        for user_data in user_data_list:
            if user_data["user_id"] == user_id:
                user = User(**user_data)
        
        if user:

            #Check if the book with isbn number and availability exists
            book_data_list = book_manager.get_data()
            book = None

            for book_data in book_data_list:
                if book_data["isbn"] == isbn and book_data["availability"]:
                    book = Book(**book_data)

            if book:
                book_data = book_manager.get_data()
                for selected_book in book_data:
                    if selected_book["isbn"] == isbn:
                        selected_book["availability"] = False

                book_manager.save_data(book_data)
                CLI.display_message(f"Book '{book.title}' checked out to {user.name}.")

                # Log the check-out operation
                self.logger.log_book_checked_out(book.title, user_id)

            else:
                CLI.display_message("Book not available.")
        else:
            CLI.display_message("User not found.")

    def check_in_book(self, user_id, isbn):
        """
        Check in a book based on the user ID and ISBN.

        Args:
            user_id (str): The user ID returning the book.
            isbn (str): The ISBN of the book to be checked in.
        """
        user_manager = UserManager()
        book_manager = BookManager()

        #Check if user with user_id exists
        user_data_list = user_manager.get_data()
        user = None

        for user_data in user_data_list:
            if user_data["user_id"] == user_id:
                user = User(**user_data)
        if user:
            #Check if the book with isbn number and availability exists
            book_data_list = book_manager.get_data()
            book = None

            for book_data in book_data_list:
                if book_data["isbn"] == isbn and not book_data["availability"]:
                    book = Book(**book_data)
           
            if book:
                book_data = book_manager.get_data()
                for selected_book in book_data:
                    if selected_book["isbn"] == isbn:
                        selected_book["availability"] = True

                book_manager.save_data(book_data)             
                CLI.display_message(f"Book '{book.title}' checked in by {user.name}.")

                # Log the check-in operation
                self.logger.log_book_checked_in(book.title, user_id)

            else:
                CLI.display_message("Book not checked out.")
        else:
            CLI.display_message("User not found.")