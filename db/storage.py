import json
from settings.config import Config
from logger.library_logger import LibraryLogger

"""
File containing classes that communicates with the Storage.
In our case it is a `.json` file in the root directory
"""
class Storage:
    """
    Static methods that directly communicates with the `.json`
    """
    @staticmethod
    def load_data():
        if not Config.LIBRARY_DATA_FILE:
            return {"books": [], "users": []}
        try:
            with open(Config.LIBRARY_DATA_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"books": [], "users": []}

    @staticmethod
    def save_data(data):
        with open(Config.LIBRARY_DATA_FILE, "w") as file:
            json.dump(data, file)

class DataManager:
    """
    Contains methods that indirectly communicates with the `.json`
    """
    def __init__(self, data_key):
        self.data_key = data_key
        self.logger = LibraryLogger

    def get_data(self):
        data = Storage.load_data()
        return data.get(self.data_key, [])

    def save_data(self, data):
        all_data = Storage.load_data()
        all_data[self.data_key] = data
        Storage.save_data(all_data)