from db.storage import DataManager
from models.library_models import User
from cli import CLI

class UserManager(DataManager):
    """
    User Manager contains all the necessary utilities related to User Model.
    """
    def __init__(self):
        super().__init__("users")

    def add_user(self, name, user_id):
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
        data = self.get_data()
        for user_data in data:
            user = User(**user_data)
            CLI.display_message(f"Name: {user.name}, User ID: {user.user_id}")

    def user_is_unique(self, user_id):
        data = self.get_data()   
        user = [User(**user_data) for user_data in data if                   
               user_id in user_data["user_id"].lower()]
        if len(user) > 0:
            return False
        else:
            return True
        
    def search_user(self, keyword):
        data = self.get_data()
        results = [User(**user_data) for user_data in data if
                   keyword.lower() in user_data["name"].lower() or
                   keyword.lower() in user_data["user_id"].lower()]
        for result in results:
            CLI.display_message(f"Name: {result.name}, User ID: {result.user_id}")