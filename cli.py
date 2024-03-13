"""
Module: cli.py

Contains the CLI class with methods for user interaction in the Library CLI Application.
"""

class CLI:
    """
    The CLI class provides methods for interacting with users through the command-line interface.
    """
    @staticmethod
    def get_user_input(message):
        """
        Get user input with a custom message.

        Args:
            message (str): The message prompt for the user.

        Returns:
            str: The input provided by the user.
        """
        return input(message)

    @staticmethod
    def display_message(message):
        """
        Display a message to the user.

        Args:
            message (str): The message to display.
        """
        print(message)

    @staticmethod
    def wait_to_continue():
        """
        Wait for the user to press Enter to continue.
        """
        input("Press Enter to continue...")