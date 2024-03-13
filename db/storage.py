"""
Module: storage.py

This module defines the Storage and DataManager classes, which are responsible for communication with the storage (JSON file) and managing data operations.
"""

import json
from settings.config import Config
from logger.library_logger import LibraryLogger

class Storage:
    """
    The Storage class provides methods for loading and saving data to a JSON file.
    """
    @staticmethod
    def load_json_data():
        """
        Load data from the JSON file.

        Returns:
            dict: Dictionary containing loaded data.
        """
        if not Config.LIBRARY_DATA_FILE:
            return {"books": [], "users": []}
        try:
            with open(Config.LIBRARY_DATA_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"books": [], "users": []}

    @staticmethod
    def save_json_data(data):
        """
        Save data to the JSON file.

        Args:
            data (dict): Data to be saved.
        """
        with open(Config.LIBRARY_DATA_FILE, "w") as file:
            json.dump(data, file)

class DataManager:
    """
    The DataManager class contains methods for managing data indirectly through the Storage class.
    """
    def __init__(self, data_key):
        """
        Initialize DataManager with a data key.

        Args:
            data_key (str): Key to identify data in the storage.
        """
        self.data_key = data_key
        self.logger = LibraryLogger

    def get_data(self):
        """
        Get data from the storage.

        Returns:
            list: List of data.
        """
        data = Storage.load_json_data()
        return data.get(self.data_key, [])

    def save_data(self, data):
        """
        Save data to the storage.

        Args:
            data (list): Data to be saved.
        """
        all_data = Storage.load_json_data()
        all_data[self.data_key] = data
        Storage.save_json_data(all_data)