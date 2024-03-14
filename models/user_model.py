"""
Module: user_model.py

Contains the User class representing entities used in the Library CLI Application.
"""

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