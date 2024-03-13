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
        
    @staticmethod  
    def generate_log(level:str, origin: str, message: str, action:str = None):
        """
        Generate log messages with specified level, origin, message, and action.

        Args:
            level (str): The log level (e.g., INFO, WARNING, ERROR).
            origin (str): The origin of the log message (e.g., method name, class name).
            message (str): The log message.
            action (str, optional): The action related to the log message. Defaults to None.
        """
        log_str = f"[{level}][{origin}]"
        if action: log_str += f"[{action}]"
        logging.info(log_str + f" {message}")