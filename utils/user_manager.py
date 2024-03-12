"""
Module: user_manage.py

This module defines the UserManager class, responsible for CRUD operations related to users in the Library CLI Application.
"""

from db.storage import DataManager
from models.library_models import User
from cli import CLI

class UserManager(DataManager):
    """
    UserManager contains all the necessary utilities related to the User model in the Library CLI Application.
    """

    def __init__(self):
        """
        Initialize a new UserManager instance with the data key set to "users".
        """
        super().__init__("users")

    def add_user(self, name, user_id):
        """
        Add a new user to the library data.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID of the user.
        """
        data = self.get_data()
        if self.user_is_unique(user_id):
            new_user = User(name, user_id)
            data.append(vars(new_user))
            self.save_data(data)
            CLI.display_message("User created!")

            # Log the user addition operation
            self.logger.log_user_added(self, name, user_id)
        else:
            CLI.display_message("User with user_id already exists!!")

    def list_users(self):
        """
        List all users in the library data.
        """
        data = self.get_data()
        for user_data in data:
            user = User(**user_data)
            CLI.display_message(f"Name: {user.name}, User ID: {user.user_id}")

    def user_is_unique(self, user_id):
        """
        Check if the provided user ID is unique in the library data.

        Args:
            user_id (str): The user ID to check for uniqueness.

        Returns:
            bool: True if the user ID is unique, False otherwise.
        """
        data = self.get_data()   
        user = [User(**user_data) for user_data in data if                   
               user_id in user_data["user_id"].lower()]
        if len(user) > 0:
            return False
        else:
            return True
        
    def search_user(self, keyword):
        """
        Search for users in the library data based on a keyword.

        Args:
            keyword (str): The keyword to search for in user names and user IDs.
        """
        data = self.get_data()
        results = [User(**user_data) for user_data in data if
                   keyword.lower() in user_data["name"].lower() or
                   keyword.lower() in user_data["user_id"].lower()]
        for result in results:
            CLI.display_message(f"Name: {result.name}, User ID: {result.user_id}")