"""
Module: library_app.py

This module defines the LibraryApp class, which represents a simple library management system.
"""

from utils.book_manager import BookManager
from utils.user_manager import UserManager
from utils.checkin_manager import CheckoutManager
from cli import CLI

class LibraryApp:
    """
    The LibraryApp class represents a simple library management system.
    It interacts with user and book management, as well as checkout functionalities through a command-line interface.
    """
    def __init__(self):
        """
        Initialize a new LibraryApp instance with instances of BookManager, UserManager, and CheckoutManager.
        """
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.check_manager = CheckoutManager()

    def user_menu(self):
        """
        Display and handle user-related menu options.
        """
        while True:
            CLI.display_message("\nUser Menu")
            CLI.display_message("1. Create User")
            CLI.display_message("2. List Users")
            CLI.display_message("3. Search User")
            CLI.display_message("0. Back to Main Menu")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == "1":
                name = CLI.get_user_input("Enter the name of the user: ")
                user_id = CLI.get_user_input("Enter the user ID: ")
                self.user_manager.add_user(name, user_id)

            elif choice == "2":
                self.user_manager.list_users()

            elif choice == "3":
                keyword = CLI.get_user_input("Enter the keyword to search: ")
                self.user_manager.search_user(keyword)

            elif choice == "0":
                CLI.display_message("Going back to the main menu!")
                break

            else:
                CLI.display_message("Invalid choice. Please try again.")
            
            CLI.wait_to_continue()

    def book_menu(self):
        """
        Display and handle book-related menu options.
        """
        while True:
            CLI.display_message("\nBook Menu")
            CLI.display_message("1. Add Book")
            CLI.display_message("2. List Books")
            CLI.display_message("3. Search Books")
            CLI.display_message("4. Check Out Book")
            CLI.display_message("5. Check In Book")
            CLI.display_message("6. Check Book Availability")
            CLI.display_message("0. Back to Main Menu")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == "1":
                title = CLI.get_user_input("Enter the title of the book: ")
                author = CLI.get_user_input("Enter the author of the book: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book: ")
                self.book_manager.add_book(title, author, isbn)

            elif choice == "2":
                self.book_manager.list_books()

            elif choice == "3":
                keyword = CLI.get_user_input("Enter the keyword to search: ")
                self.book_manager.search_books(keyword)

            elif choice == "4":
                user_id = CLI.get_user_input("Enter the user ID: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book to check out: ")
                self.check_manager.check_out_book(user_id, isbn)

            elif choice == "5":
                user_id = CLI.get_user_input("Enter the user ID: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book to check in: ")
                self.check_manager.check_in_book(user_id, isbn)

            elif choice == "6":
                isbn = CLI.get_user_input("Enter the ISBN of the book to check availability: ")
                self.book_manager.is_available(isbn)

            elif choice == "0":
                CLI.display_message("Going back to the main menu!")
                break

            else:
                CLI.display_message("Invalid choice. Please try again.")
            
            CLI.wait_to_continue()

    def run(self):
        """
        Run the main library management system loop.
        """
        while True:
            CLI.display_message("\nLibrary Management System")
            CLI.display_message("1. User Menu")
            CLI.display_message("2. Book Menu")
            CLI.display_message("0. Exit")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == "1":
                self.user_menu()

            elif choice == "2":
                self.book_menu()

            elif choice == "0":
                CLI.display_message("Exiting the Library Management System. Goodbye!")
                break

            else:
                CLI.display_message("Invalid choice. Please try again.")
            
            CLI.wait_to_continue()
