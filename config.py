"""
Module: config.py

Contains the Config class with configuration settings for the Library CLI Application.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    The Config class holds configuration settings for the application.
    """
    LIBRARY_DATA_FILE = os.getenv('LIBRARY_DATA_FILE')
    