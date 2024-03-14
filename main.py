"""
Module: main.py

This module serves as the main entry point for the Library CommandLineInterFace Application.
"""

from apps.library_app import LibraryManagementSystem
from utils.logger import LibraryLogger

LibraryLogger()

if __name__ == "__main__":
    app = LibraryManagementSystem()
    app.run()