"""
Module: main.py

This module serves as the main entry point for the Library CommandLineInterFace Application.
"""

import logging
from apps.library_app import LibraryApp

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

if __name__ == "__main__":
    app = LibraryApp()
    app.run()