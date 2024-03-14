"""
Module: choices.py

This module defines Enums representing menu options for different parts of the library management system.
"""

from enum import Enum

class UserMenuOption(Enum):
    """
    Enum representing menu options for the user menu.
    """
    CREATE_USER = '1'
    LIST_USER = '2'
    SEARCH_USER = '3'
    BACK_TO_MAIN = '0'
    
class BookMenuOption(Enum):
    """
    Enum representing menu options for the book menu.
    """
    ADD_BOOK = '1'
    LIST_BOOKS = '2'
    SEARCH_BOOKS = '3'
    CHECK_OUT_BOOK = '4'
    CHECK_IN_BOOK = '5'
    CHECK_BOOK_AVAILABILITY = '6'
    BACK_TO_MAIN_MENU = '0'
    
class HomeMenuOption(Enum):
    """
    Enum representing menu options for the main menu.
    """
    USER_MENU = '1'
    BOOK_MENU = '2'
    EXIT = '0'