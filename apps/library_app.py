"""
Module: library_app.py

This module defines the LibraryApp class, which represents a simple library management system.
"""

from utils.book_manager import BookManager
from utils.user_manager import UserManager
from utils.checkin_manager import CheckoutManager
from cli import CLI
from cli_choices.library_management_choices import UserMenuOption, BookMenuOption, HomeMenuOption

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
            CLI.display_message(f"{UserMenuOption.CREATE_USER.value}. Create User")
            CLI.display_message(f"{UserMenuOption.LIST_USER.value}. List Users")
            CLI.display_message(f"{UserMenuOption.SEARCH_USER.value}. Search User")
            CLI.display_message(f"{UserMenuOption.BACK_TO_MAIN.value}. Back to Main Menu")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == UserMenuOption.CREATE_USER.value:
                name = CLI.get_user_input("Enter the name of the user: ")
                user_id = CLI.get_user_input("Enter the user ID: ")
                self.user_manager.add_user(name, user_id)

            elif choice == UserMenuOption.LIST_USER.value:
                self.user_manager.list_users()

            elif choice == UserMenuOption.SEARCH_USER.value:
                keyword = CLI.get_user_input("Enter the keyword to search: ")
                self.user_manager.search_user(keyword)

            elif choice == UserMenuOption.BACK_TO_MAIN.value:
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
            CLI.display_message(f"{BookMenuOption.ADD_BOOK.value}. Add Book")
            CLI.display_message(f"{BookMenuOption.LIST_BOOKS.value}. List Books")
            CLI.display_message(f"{BookMenuOption.SEARCH_BOOKS.value}. Search Books")
            CLI.display_message(f"{BookMenuOption.CHECK_OUT_BOOK.value}. Check Out Book")
            CLI.display_message(f"{BookMenuOption.CHECK_IN_BOOK.value}. Check In Book")
            CLI.display_message(f"{BookMenuOption.CHECK_BOOK_AVAILABILITY.value}. Check Book Availability")
            CLI.display_message(f"{BookMenuOption.BACK_TO_MAIN_MENU.value}. Back to Main Menu")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == BookMenuOption.ADD_BOOK.value:
                title = CLI.get_user_input("Enter the title of the book: ")
                author = CLI.get_user_input("Enter the author of the book: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book: ")
                self.book_manager.add_book(title, author, isbn)

            elif choice == BookMenuOption.LIST_BOOKS.value:
                self.book_manager.list_books()

            elif choice == BookMenuOption.SEARCH_BOOKS.value:
                keyword = CLI.get_user_input("Enter the keyword to search: ")
                self.book_manager.search_books(keyword)

            elif choice == BookMenuOption.CHECK_OUT_BOOK.value:
                user_id = CLI.get_user_input("Enter the user ID: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book to check out: ")
                self.check_manager.check_out_book(user_id, isbn)

            elif choice == BookMenuOption.CHECK_IN_BOOK.value:
                user_id = CLI.get_user_input("Enter the user ID: ")
                isbn = CLI.get_user_input("Enter the ISBN of the book to check in: ")
                self.check_manager.check_in_book(user_id, isbn)

            elif choice == BookMenuOption.CHECK_BOOK_AVAILABILITY.value:
                isbn = CLI.get_user_input("Enter the ISBN of the book to check availability: ")
                self.book_manager.is_available(isbn)

            elif choice == BookMenuOption.BACK_TO_MAIN_MENU.value:
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
            CLI.display_message(f"{HomeMenuOption.USER_MENU.value}. User Menu")
            CLI.display_message(f"{HomeMenuOption.BOOK_MENU.value}. Book Menu")
            CLI.display_message(f"{HomeMenuOption.EXIT.value}. Exit")

            choice = CLI.get_user_input("Enter your choice: ")

            if choice == HomeMenuOption.USER_MENU.value:
                self.user_menu()

            elif choice == HomeMenuOption.BOOK_MENU.value:
                self.book_menu()

            elif choice == HomeMenuOption.EXIT.value:
                CLI.display_message("Exiting the Library Management System. Goodbye!")
                break

            else:
                CLI.display_message("Invalid choice. Please try again.")
            
            CLI.wait_to_continue()
            